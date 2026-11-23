#!/usr/bin/env python3
"""Compute V2 size measures on the HMR claim graph. Uses only V2's definitions:
R = number of related (ancestor, descendant) pairs under the allowed links (math page, 'proved' table);
a contradiction at the roots blocks the join and loses the crossing term; economy = R per starting claim."""
import json, csv, itertools, sys
from graph_data import NODES, EDGES
nodes={}
for line in NODES.strip().splitlines():
    i,k,p,t=line.split('|',3); assert i not in nodes,i; nodes[i]=dict(id=i,kind=k,page=p,text=t)
edges=[]
for line in EDGES.strip().splitlines():
    for e in line.split(';'):
        e=e.strip()
        if not e: continue
        st,ty=e.split('|'); s,d=st.split('>'); assert s in nodes and d in nodes,(s,d); assert ty in('cs','ch','cn','as','op')
        edges.append((s,d,ty))
assert len(set((s,d) for s,d,_ in edges))==len(edges)
LEVELS={'strictest':{'cs'},'strict':{'cs','ch','cn'},'lenient':{'cs','ch','cn','as'},'potential':{'cs','ch','cn','as','op'}}
def build(types,extra=()):
    ch={n:set() for n in nodes}; pa={n:set() for n in nodes}
    for s,d,t in list(edges)+list(extra):
        if t in types: ch[s].add(d); pa[d].add(s)
    return ch,pa
def topo(ch,pa):
    indeg={n:len(pa[n]) for n in nodes}; q=[n for n in nodes if indeg[n]==0]; out=[]
    while q:
        n=q.pop(); out.append(n)
        for c in ch[n]:
            indeg[c]-=1
            if indeg[c]==0: q.append(c)
    assert len(out)==len(nodes),'cycle'; return out
def anc(ch,pa):
    A={}
    for n in topo(ch,pa):
        s=set()
        for p in pa[n]: s|=A[p]; s.add(p)
        A[n]=s
    return A
def stats(types,extra=(),drop_x=True):
    ch,pa=build(types,extra); A=anc(ch,pa)
    live=[n for n in nodes if not (drop_x and nodes[n]['kind']=='X' and not ch[n] and not pa[n])]
    R=sum(len(A[n]) for n in live)
    h={}
    for n in topo(ch,pa): h[n]=1+max((h[p] for p in pa[n]),default=-1)
    # weak components
    comp={}
    for n in live:
        if n in comp: continue
        st=[n]; comp[n]=n
        while st:
            x=st.pop()
            for y in ch[x]|pa[x]:
                if y not in comp: comp[y]=n; st.append(y)
    sizes={}
    for n in live: sizes.setdefault(comp[n],[]).append(n)
    def Rof(ms): ms=set(ms); return sum(len(A[n]&ms) for n in ms)
    comps=sorted(([len(v),Rof(v),sorted(v)] for v in sizes.values()),reverse=True)
    roots=[n for n in live if not pa[n] and ch[n]]
    stated=[n for n in roots if nodes[n]['kind']=='A']; imp=[n for n in roots if nodes[n]['kind']=='I']
    eff=[n for n in roots if nodes[n]['kind'] not in 'AI']
    return dict(n=len(live),links=sum(len(ch[n]) for n in live),R=R,h=max(h[n] for n in live),
        pieces=len(comps),pieces_gt1=sum(1 for c in comps if c[0]>1),largest_n=comps[0][0],largest_R=comps[0][1],
        isolated=sum(1 for c in comps if c[0]==1),roots_stated=len(stated),roots_import=len(imp),roots_effective_unproved=len(eff),
        eff_list=eff,comps=comps,A=A,ch=ch,pa=pa)
out={}
real=[n for n in nodes if nodes[n]['kind']!='X']
a_stated=sum(1 for n in nodes if nodes[n]['kind']=='A'); n_imp=sum(1 for n in nodes if nodes[n]['kind']=='I')
print('nodes (excluding open work items):',len(real),' stated starting claims a =',a_stated,' imported established results =',n_imp)
print('kinds:',{k:sum(1 for n in nodes if nodes[n]['kind']==k) for k in 'AIDTNRCX'})
print('edges by type:',{t:sum(1 for e in edges if e[2]==t) for t in ('cs','ch','cn','as','op')})
for name,types in LEVELS.items():
    s=stats(types); out[name]={k:v for k,v in s.items() if k not in('A','ch','pa','comps','eff_list')}
    # n counted among nodes that take part (non-isolated) too
    part=s['n']-s['isolated']
    out[name].update(participating=part,econ_stated=round(s['R']/a_stated,1),econ_all_roots=round(s['R']/(s['roots_stated']+s['roots_import']+s['roots_effective_unproved']),1),R_per_claim=round(s['R']/max(part,1),2))
    print(f"\n== {name}: n={s['n']} participating={part} links={s['links']} R={s['R']} h={s['h']} pieces(all)={s['pieces']} pieces(>1 claim)={s['pieces_gt1']} isolated={s['isolated']} largest piece n={s['largest_n']} R={s['largest_R']}")
    print(f"   roots with consequences: stated {s['roots_stated']}, imports {s['roots_import']}, unproved non-assumption roots {s['roots_effective_unproved']} {s['eff_list'][:12]}")
    print(f"   economy R/a(stated {a_stated}) = {out[name]['econ_stated']}; R/(all roots) = {out[name]['econ_all_roots']}; R per participating claim = {out[name]['R_per_claim']}")
    for c in s['comps'][:6]:
        if c[0]>1: print('   piece n=%d R=%d: %s'%(c[0],c[1],' '.join(c[2][:14])+(' ...' if c[0]>14 else '')))
# --- HMR's own content only: pairs where the descendant is not an import and ancestor is not an import
for name in ('strict','lenient'):
    s=stats(LEVELS[name]); own=sum(len([a for a in s['A'][n] if nodes[a]['kind']!='I']) for n in real)
    out[name]['R_excluding_import_ancestors']=own; print(f"{name}: R not counting imported results as ancestors = {own}")
# --- contradiction at the roots, derived: {A4,A5,A6,A7 via T_rule} + P1 cannot all hold given I_bg (math page 'No space in the large')
s=stats(LEVELS['strict']); A=s['A']
def desc(x): return {n for n in nodes if x in A[n]}|{x}
grow=desc('T_rule'); space=desc('P1'); both=grow&space
print('\n== root conflict (T_rule family vs P1, by Brightwell-Georgiou):')
print('  strict: claims resting on the growth family',len(grow),'; on P1',len(space),'; on both',len(both),sorted(both))
blocked=len(grow-space)*len(space-grow); print('  crossing term a join would add if all of one preceded the other (upper bound, n*n):',blocked)
sus={'A4','A5','A6','A7','P1'}; clean=[n for n in real if not (A[n]&sus) and n not in sus]
Rclean=sum(len(A[n]&set(clean)) for n in clean); print('  unrestricted reading (warrant lost above every suspect A4,A5,A6,A7,P1): claims left',len(clean),' R left',Rclean,'of',s['R'])
out['conflict']=dict(on_growth=len(grow),on_P1=len(space),on_both=sorted(both),blocked_crossing_upper=blocked,clean_claims=len(clean),R_clean=Rclean)
sl=stats(LEVELS['lenient']); Al=sl['A']; gl={n for n in nodes if 'T_rule' in Al[n]}; sp={n for n in nodes if 'P1' in Al[n]}
print('  lenient: on both',sorted(gl&sp)); out['conflict']['lenient_on_both']=sorted(gl&sp)
# --- fragility (V2 false-part count): D for each strict link
base=s['R']; D=[]
for (u,v,t) in edges:
    if t in LEVELS['strict']:
        e2=[e for e in edges if e!=(u,v,t)]
        ch,pa=build(LEVELS['strict']); ch[u].discard(v); pa[v].discard(u); A2=anc(ch,pa)
        D.append((base-sum(len(A2[n]) for n in real),u,v))
D.sort(reverse=True); print('\n== bracing: cost D of a false strict link: max',D[0],' median',D[len(D)//2][0],' links with D=1:',sum(1 for d in D if d[0]==1),'of',len(D))
print('  top 8 most load-bearing strict links:',[(d,u+'>'+v) for d,u,v in D[:8]])
multi=sum(1 for n in real if len(s['pa'][n])>=2); print('  claims with 2+ direct strict supports:',multi)
out['bracing']=dict(max_D=D[0],median_D=D[len(D)//2][0],top=D[:8])
# --- false starting claim: 1+f
f=sorted(((len(desc(r))-1,r) for r in nodes if nodes[r]['kind']=='A'),reverse=True); print('  claims resting on each stated starting claim (strict):',f)
out['rest_on_assumption']=f
# --- work items: certify each open work item's links (and nothing else) on top of strict and of lenient
print('\n== open work items ranked by gain in R if their links were certified')
items=[n for n in nodes if nodes[n]['kind']=='X']; rank=[]
for x in items:
    ex=[(s_,d,'cs') for (s_,d,t) in edges if t=='op' and (s_==x or d==x)]
    r1=stats(LEVELS['strict'],ex)['R']-out['strict']['R']; r2=stats(LEVELS['lenient'],ex)['R']-out['lenient']['R']
    rank.append((r2,r1,x,nodes[x]['text']))
for r in sorted(rank,reverse=True): print('  +%d on lenient, +%d on strict: %s %s'%r)
out['work_items']=sorted(rank,reverse=True)
allx=[(s_,d,'cs') for (s_,d,t) in edges if t=='op' and (nodes[s_]['kind']=='X' or nodes[d]['kind']=='X')]
r=stats(LEVELS['lenient'],allx,drop_x=False); print('  all nine work items closed on top of lenient: n=%d R=%d h=%d'%(r['n'],r['R'],r['h']))
out['all_items_on_lenient']=dict(n=r['n'],R=r['R'],h=r['h'])
r=stats(LEVELS['potential'],drop_x=False); print('  everything on the pages true and linked (potential): n=%d R=%d h=%d pieces=%d'%(r['n'],r['R'],r['h'],r['pieces']))
out['potential_all']=dict(n=r['n'],R=r['R'],h=r['h'],pieces=r['pieces'])
# reference shapes for scale
n=len(real); print('\n== scale: a single line of',n,'claims would hold',n*(n-1)//2,'pairs; a fan',n-1)
json.dump(out,open('hmr_results.json','w'),indent=1,default=str)
json.dump(dict(nodes=list(nodes.values()),edges=[dict(src=a,dst=b,type=t) for a,b,t in edges]),open('hmr_graph.json','w'),indent=1)
with open('hmr_nodes.csv','w',newline='') as fh:
    w=csv.writer(fh); w.writerow(['id','kind','page','claim']); [w.writerow([v['id'],v['kind'],v['page'],v['text']]) for v in nodes.values()]
with open('hmr_edges.csv','w',newline='') as fh:
    w=csv.writer(fh); w.writerow(['from','to','type']); [w.writerow(e) for e in edges]
