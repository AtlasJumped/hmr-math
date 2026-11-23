"""Checks: Thm4 (true links -> true whole), Thm11 (kappa), Reiter duality for suspects (Thm12), join of contradicting ideas (Thm9/14),
N15 insight bound, Thm14 ratio, pebbling (M12), Thm17 numerics."""
import itertools, random, math
from common import *
rng = random.Random(777)
res = {}
def rec(name, ok, ex=None, cnt=1):
    r = res.setdefault(name, [0, 0, None]); r[0] += cnt
    if not ok:
        r[1] += 1
        if r[2] is None: r[2] = ex
def labeled_posets(n):
    S = set()
    for P in gen_natural(n):
        for perm in itertools.permutations(range(n)):
            nb = [0]*n
            for i in range(n):
                m = 0
                for j in range(n):
                    if P[i] >> j & 1: m |= 1 << perm[j]
                nb[perm[i]] = m
            S.add(tuple(nb))
    return S
def is_dag(n, arcs):
    indeg = [0]*n; adj = [[] for _ in range(n)]
    for a, b in arcs:
        if a == b: return False
        adj[a].append(b); indeg[b] += 1
    st = [i for i in range(n) if indeg[i] == 0]; k = 0
    while st:
        x = st.pop(); k += 1
        for y in adj[x]:
            indeg[y] -= 1
            if indeg[y] == 0: st.append(y)
    return k == n

# ---- Thm 4: if every link maps to a relation, every relation maps to a relation
for (a, b) in [(1,1),(2,2),(3,3),(4,3),(4,4),(5,3)]:
    for M in gen_natural(a):
        cm = covers(M)
        for T in gen_natural(b):
            for rho in itertools.product(range(b), repeat=a):
                if all(T[rho[y]] >> rho[x] & 1 for x, y in cm):
                    ok = all(T[rho[i]] >> rho[j] & 1 for i in range(a) for j in range(a) if M[i] >> j & 1)
                    rec("Thm4: all links true => all R(M) relations true", ok, (M, T, rho))
# ---- Thm 11 and Reiter duality
LP = {n: labeled_posets(n) for n in range(1, 5)}
def kappa(n, arcs):
    arcs = list(arcs)
    for k in range(len(arcs)+1):
        for rem in itertools.combinations(range(len(arcs)), k):
            if is_dag(n, [arcs[i] for i in range(len(arcs)) if i not in rem]): return k
def minimal_conflict_arcs(n, arcs):
    arcs = list(arcs); S = set()
    for k in range(1, len(arcs)+1):
        for sub in itertools.combinations(arcs, k):
            if not is_dag(n, sub) and all(is_dag(n, sub[:i]+sub[i+1:]) for i in range(k)):
                S.update(sub)
    return S
def min_repair_arcs(n, arcs):
    arcs = list(arcs); S = set(); m = len(arcs)
    # inclusion-minimal sets whose removal makes it acyclic
    good = []
    for k in range(m+1):
        for rem in itertools.combinations(range(m), k):
            if any(set(g) <= set(rem) for g in good): continue
            if is_dag(n, [arcs[i] for i in range(m) if i not in rem]): good.append(rem)
    for g in good: S.update(arcs[i] for i in g)
    return S
def check_claims(n, arcs, posets):
    kap = kappa(n, arcs)
    falses = [sum(1 for (a, b) in arcs if not (P[b] >> a & 1)) for P in posets]
    rec("Thm11: every possible world makes >= kappa claims false; some makes exactly kappa", min(falses) == kap, (n, arcs, kap, min(falses)))
    if kap > 0 and len(arcs) <= 10:
        rec("Thm12 (Reiter duality): arcs in a minimal conflict = arcs in some minimal repair", minimal_conflict_arcs(n, arcs) == min_repair_arcs(n, arcs), (n, arcs))
for n in (2, 3, 4):
    allarcs = [(i, j) for i in range(n) for j in range(n) if i != j]
    for mask in range(1 << len(allarcs)):
        arcs = [allarcs[i] for i in range(len(allarcs)) if mask >> i & 1]
        if n == 4 and len(arcs) > 9: continue
        check_claims(n, arcs, LP[n])
LP5 = labeled_posets(5)
allarcs = [(i, j) for i in range(5) for j in range(5) if i != j]
for t in range(150):
    arcs = [e for e in allarcs if rng.random() < 0.3]
    check_claims(5, arcs, LP5) if len(arcs) <= 10 else None
# ---- Join of contradicting ideas: exists poset containing both iff union acyclic; direct conflict => impossible
for n in (3, 4):
    L = sorted(LP[n])
    for C in L:
        ca = [(j, i) for i in range(n) for j in range(n) if C[i] >> j & 1]
        for D in L:
            da = [(j, i) for i in range(n) for j in range(n) if D[i] >> j & 1]
            joinable = any(all(P[b] >> a & 1 for a, b in ca+da) for P in LP[n])
            rec("Join: two ideas on shared referents can be joined iff union of claims acyclic", joinable == is_dag(n, ca+da), (C, D))
            direct = any((b, a) in set(da) for a, b in ca)
            if direct: rec("Join: a-before-b in C and b-before-a in D => no joint pattern", not joinable, (C, D))
# ---- N15 insight: J(y) >= n(C)n(D) for first thought resting on two side-by-side parts
def check_insight(P):
    n = len(P)
    for Cm in range(1, 1 << n):
        for Dm in range(1, 1 << n):
            if Cm & Dm: continue
            if pc(Cm)*pc(Dm) == 0: continue
            # side by side: no relation across, no common later thought
            ok = True
            for c in range(n):
                if Cm >> c & 1:
                    for d in range(n):
                        if Dm >> d & 1 and (P[c] >> d & 1 or P[d] >> c & 1): ok = False
            if not ok: continue
            if any(all(P[z] >> c & 1 for c in range(n) if Cm >> c & 1 and False) for z in range(n)): pass
            common = any(any(P[z] >> c & 1 for c in range(n) if Cm >> c & 1) and any(P[z] >> d & 1 for d in range(n) if Dm >> d & 1) for z in range(n))
            # CAUTION: "no common later thought" for the pair-level J; require for all cross pairs
            allfree = True
            for c in range(n):
                if Cm >> c & 1:
                    for d in range(n):
                        if Dm >> d & 1 and any(P[z] >> c & 1 and P[z] >> d & 1 for z in range(n)): allfree = False
            if not allfree: continue
            # y rests on all of C and D (past of y = downset generated by C u D)
            S = Cm | Dm
            for x in range(n):
                if S >> x & 1: S |= P[x]
            # J(y): pairs in past(y), apart, no common later thought before y (inside P)
            J = 0
            for i in range(n):
                for j in range(i+1, n):
                    if S >> i & 1 and S >> j & 1 and not (P[i] >> j & 1 or P[j] >> i & 1):
                        if not any(P[z] >> i & 1 and P[z] >> j & 1 for z in range(n)): J += 1
            rec("N15: J(y) >= n(C) n(D) for y resting on side-by-side C, D", J >= pc(Cm)*pc(Dm), (P, Cm, Dm, J))
for n in range(2, 6):
    for P in gen_natural(n): check_insight(P)
# ---- Thm14 ratio: k parts each a line of n: apart k n(n-1)/2, one line kn(kn-1)/2, ratio -> k
for k in (2, 3, 5):
    for n in (5, 50, 500):
        apart = k*n*(n-1)//2; one = k*n*(k*n-1)//2
        rec("Thm14: ratio one-line/apart = (kn-1)/(n-1) -> k (k=2,3,5; n=5..500)", abs(one/apart - (k*n-1)/(n-1)) < 1e-12 and (n < 500 or abs(one/apart-k) < k/(n-1)+1e-9), (k, n))
# ---- pebbling (black pebble game, free placement on sources)
def pebble_number(P, goals=None):
    n = len(P); cv = covers(P)
    preds = [0]*n
    for a, b in cv: preds[b] |= 1 << a
    if goals is None: goals = [i for i in range(n) if all(not (P[j] >> i & 1) for j in range(n))]
    gm = sum(1 << g for g in goals)
    def feasible(k):
        from collections import deque
        start = (0, 0); seen = {start}; dq = deque([start])
        while dq:
            S, G = dq.popleft()
            if G == gm: return True
            moves = []
            for x in range(n):
                if S >> x & 1: moves.append(S & ~(1 << x))
                elif (preds[x] & ~S) == 0 and pc(S) < k: moves.append(S | 1 << x)
            for T in moves:
                G2 = G | (T & gm)
                st = (T, G2)
                if st not in seen: seen.add(st); dq.append(st)
        return False
    k = 1
    while not feasible(k): k += 1
    return k
def tree(h):  # in-tree: leaves at bottom, root = unique maximum; h = height in edges
    # nodes by level; build below-masks via natural labeling: leaves first
    n = 2**(h+1)-1; below = [0]*n
    # heap indexing: node i children 2i+1,2i+2; leaves are largest indices. relabel reversed to be natural
    rev = lambda i: n-1-i
    bl = [0]*n
    for i in range(n-1, -1, -1):
        m = 0
        for c in (2*i+1, 2*i+2):
            if c < n: m |= 1 << rev(c) | bl[c]
        bl[i] = m
    return tuple(bl[n-1-j] for j in range(n))
for n in range(1, 9):
    line = tuple((1 << i)-1 for i in range(n))
    rec("Pebble: a line needs 2 live thoughts (n>=2; 1 for n=1)", pebble_number(line) == (1 if n == 1 else 2), (n, pebble_number(line)))
for h in (1, 2, 3):
    T = tree(h)
    rec("Pebble: full binary in-tree of height h (edges) needs h+2 (h=1,2,3)", pebble_number(T) == h+2, (h, pebble_number(T)))
    rec("Pebble (alt): same tree needs h+1 pebbles?  [expected FAIL; shows exact constant]", pebble_number(T) == h+1, (h, pebble_number(T)))
for n in range(1, 7):
    for P in gen_natural(n):
        cv = covers(P); indeg = [0]*n
        for a, b in cv: indeg[b] += 1
        pn = pebble_number(P)
        rec("Pebble: max Hasse in-degree + 1 <= pebbling number <= n (all posets n<=6)", max(indeg)+1 <= pn <= n, (P, pn))
# ---- Thm17 numerics
for t in range(2000):
    m = rng.randint(2, 8)
    p = [rng.random()+1e-3 for _ in range(m)]; s = sum(p); p = [x/s for x in p]
    r = [rng.random()*3+1e-3 for _ in range(m)]
    z = sum(pi*ri for pi, ri in zip(p, r)); r = [ri/z for ri in r]      # averaging (harmonic) property
    Z = lambda b: sum(pi*ri**b for pi, ri in zip(p, r))
    V = lambda b: sum(pi*ri**b*math.log(ri) for pi, ri in zip(p, r))/Z(b)
    b = rng.random()*2; h = 1e-5
    dlnZ = (math.log(Z(b+h))-math.log(Z(b-h)))/(2*h)
    dV = (V(b+h)-V(b-h))/(2*h)
    q = [pi*ri**b/Z(b) for pi, ri in zip(p, r)]
    var = sum(qi*math.log(ri)**2 for qi, ri in zip(q, r)) - V(b)**2
    rec("Thm17: Z(1)=1, V=dlnZ/db, dV/db=Var>=0, V(0)<=0<=V(1)", abs(Z(1)-1) < 1e-9 and abs(dlnZ-V(b)) < 1e-5 and abs(dV-var) < 1e-4 and var > -1e-12 and V(0) <= 1e-12 and V(1) >= -1e-12, (p, r, b))
for k, (cnt, bad, ex) in res.items():
    print(("PASS" if bad == 0 else "FAIL"), cnt, k, "" if bad == 0 else (bad, ex))
