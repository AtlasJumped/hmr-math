"""Exhaustive checks: then law, identities, damage theorems, Theorem 15, Theorem 1, glue formula."""
import sys, random, time
from common import *
NMAX = int(sys.argv[1]) if len(sys.argv) > 1 else 6
rng = random.Random(12345)
res = {}
def rec(name, ok, ex=None, cnt=0):
    r = res.setdefault(name, [0, 0, None]); r[0] += cnt
    if not ok:
        r[1] += 1
        if r[2] is None or sum(len(x) if hasattr(x,'__len__') else 1 for x in ex) < sum(len(x) if hasattr(x,'__len__') else 1 for x in r[2]): r[2] = ex

# ---------- A. then law and beside law, all pairs with n(C)+n(D) <= NMAX
polys = {n: list(gen_natural(n)) for n in range(0, NMAX+1)}
for a in range(0, NMAX+1):
    for b in range(0, NMAX+1-a):
        for C in polys[a]:
            for D in polys[b]:
                T = then(C, D)
                # independent count: relations of closure of Hasse edges of combined construction
                E = covers(T)
                T2 = closure_from_edges(len(T), E)
                ok = (R(T) == R(C)+R(D)+a*b) and T2 == T
                rec("then law R(C then D)=R(C)+R(D)+n(C)n(D)", ok, (C, D), 1)
                B = beside(C, D)
                rec("beside law R=R(C)+R(D)", R(B) == R(C)+R(D), (C, D), 1)
                # joint link: C with unique max u, D with unique min v, one link: loss of cutting = n(C)n(D)
                if a and b:
                    cm = [i for i in range(a) if all(not (C[j] >> i & 1) for j in range(a))]
                    dm = [i for i in range(b) if D[i] == 0]
                    if len(cm) == 1 and len(dm) == 1:
                        J = beside(C, D)
                        J2 = closure_from_edges(a+b, covers(J) + [(cm[0], a+dm[0])])
                        cut = R(J2) - R(J)
                        rec("joint: one link between top-unique C and bottom-unique D adds exactly n(C)n(D)", cut == a*b, (C, D), 1)
# random 10..20
for t in range(300):
    a = rng.randint(5, 10); b = rng.randint(5, 10)
    C = random_poset(a, rng.random()*0.5, rng); D = random_poset(b, rng.random()*0.5, rng)
    T = then(C, D)
    rec("then law R(C then D)=R(C)+R(D)+n(C)n(D)", R(T) == R(C)+R(D)+a*b and closure_from_edges(a+b, covers(T)) == T, (C, D), 1)

# ---------- B. identity R = sum of pasts = sum of futures = number of pairs; R=(# comparable pairs)
for n in range(0, NMAX+1):
    for P in polys[n]:
        pasts = sum(pc(m) for m in P)
        futs = sum(above_count(P))
        pairs = sum(1 for i in range(n) for j in range(n) if P[j] >> i & 1)
        rec("R = sum |past(x)| = sum f(x) = #comparable pairs", pasts == futs == pairs == R(P), (P,), 1)
for t in range(300):
    n = rng.randint(10, 20); P = random_poset(n, rng.random()*0.4, rng)
    rec("R = sum |past(x)| = sum f(x) = #comparable pairs", sum(pc(m) for m in P) == sum(above_count(P)) == R(P), (P,), 1)

# ---------- C. damage theorems
def check_damage(P, name_sfx=""):
    n = len(P); f = above_count(P); RP = R(P)
    # Theorem 7: false b -> unwarranted = {x: b<=x}; size 1+f(b)
    for b in range(n):
        unw = [x for x in range(n) if x == b or (P[x] >> b & 1)]
        rec("Thm7: false thought removes warrant of exactly 1+f thoughts", len(unw) == 1 + f[b], (P, b), 1)
    for (u, v) in covers(P):
        E = [e for e in covers(P) if e != (u, v)]
        P2 = closure_from_edges(n, E)
        D = RP - R(P2)
        bound = (1 + pc(P[u])) * (1 + f[v])
        rec("Thm8.2: 1 <= D(l) <= (1+|past u|)(1+f(v))", 1 <= D <= bound, (P, (u, v), D, bound), 1)
        # exact: D = # pairs (a,c), a<=u, v<=c with every chain using l ; also 8.1 trivial (closure of remaining links)
        lost = 0
        for c in range(n):
            for a in range(n):
                if P[c] >> a & 1 and not (P2[c] >> a & 1): lost += 1
        rec("Thm8.3: relation keeps certificate iff a chain avoids l (lost pairs all have a<=u, v<=c)",
            all(((a == u) or (P[u] >> a & 1)) and ((c == v) or (P[c] >> v & 1)) for c in range(n) for a in range(n) if P[c] >> a & 1 and not (P2[c] >> a & 1)), (P, (u, v)), 1)
        # fan check: P with one element below all others, others pairwise unrelated
for n in range(2, 21):
    fan = tuple([0] + [1]*(n-1))
    ok = True
    for (u, v) in covers(fan):
        E = [e for e in covers(fan) if e != (u, v)]
        D = R(fan) - R(closure_from_edges(n, E)); ok &= (D == 1)
    rec("Fan: a false link costs exactly 1 relation (n=2..20)", ok, (n,), 1)
    line = tuple((1 << i)-1 for i in range(n))
    ok = True; mx = 0
    for k in range(1, n):  # false link after the k-th thought
        E = [e for e in covers(line) if e != (k-1, k)]
        D = R(line) - R(closure_from_edges(n, E)); ok &= (D == k*(n-k)); mx = max(mx, D)
    rec("Line: false link after k-th costs k(n-k)", ok, (n,), 1)
    rec("Line: max cost = floor(n^2/4)", mx == n*n//4, (n, mx), 1)
for n in range(0, NMAX+1):
    for P in polys[n]: check_damage(P)
for t in range(150):
    n = rng.randint(10, 20); check_damage(random_poset(n, rng.random()*0.4, rng))
# 8.3 pairwise path check (explicit chains), n<=6
def reach_avoid(P, a, c, edge):
    n = len(P); E = [e for e in covers(P) if e != edge]
    adj = {}
    for x, y in E: adj.setdefault(x, []).append(y)
    st = [a]; seen = {a}
    while st:
        x = st.pop()
        if x == c: return True
        for y in adj.get(x, []):
            if y not in seen: seen.add(y); st.append(y)
    return False
for n in range(2, min(NMAX, 6)+1):
    for P in polys[n]:
        for (u, v) in covers(P):
            P2 = closure_from_edges(n, [e for e in covers(P) if e != (u, v)])
            for c in range(n):
                for a in range(n):
                    if P[c] >> a & 1:
                        rec("Thm8.3 explicit: related pair certified iff a chain of links avoids l", reach_avoid(P, a, c, (u, v)) == bool(P2[c] >> a & 1), (P, (u, v), a, c), 1)

# ---------- D. Theorem 15 (histories never fall; equal iff new thought rests on every existing one)
def check_t15(P):
    n = len(P); e0 = lin_ext(P)
    # all down-sets S as the set of things the new thought rests on (its past)
    for S in range(1 << n):
        if all((P[j] & ~S) == 0 for j in range(n) if S >> j & 1):
            Q = P + (S,)
            e1 = lin_ext(Q)
            full = (S == (1 << n)-1)
            rec("Thm15: e never falls under a birth", e1 >= e0, (P, S, e0, e1), 1)
            rec("Thm15: e unchanged iff new thought rests on all existing", (e1 == e0) == full, (P, S, e0, e1), 1)
for n in range(0, min(NMAX, 6)+1):
    for P in polys[n]: check_t15(P)
if NMAX >= 7:
    for P in rng.sample(polys[7], 300): check_t15(P)
for t in range(100):
    n = rng.randint(10, 14); check_t15(random_poset(n, 0.1 + rng.random()*0.4, rng)) if False else None
for t in range(40):
    n = rng.randint(10, 13); P = random_poset(n, 0.2 + rng.random()*0.4, rng)
    e0 = lin_ext(P)
    for _ in range(8):
        # random down-set: pick random element set, close downward
        S = 0
        for x in range(n):
            if rng.random() < 0.3: S |= 1 << x | P[x]
        Q = P + (S,); e1 = lin_ext(Q)
        rec("Thm15: e never falls under a birth", e1 >= e0, (P, S), 1)
        rec("Thm15: e unchanged iff new thought rests on all existing", (e1 == e0) == (S == (1 << n)-1), (P, S), 1)

# ---------- E. Theorem 1: histories of a pattern are connected by swaps of unrelated neighbors; intersection = pattern
for n in range(1, min(NMAX, 6)+1):
    for P in polys[n]:
        exts = extensions(P); S = set(exts)
        # connectivity under adjacent swap of unrelated
        seen = {exts[0]}; st = [exts[0]]
        while st:
            L = st.pop()
            for i in range(n-1):
                x, y = L[i], L[i+1]
                if not (P[y] >> x & 1) and not (P[x] >> y & 1):
                    M = L[:i] + (y, x) + L[i+2:]
                    assert M in S
                    if M not in seen: seen.add(M); st.append(M)
        conn = (seen == S)
        # intersection of extensions = pattern
        inter = [0]*n
        for i in range(n): inter[i] = (1 << n)-1
        for L in exts:
            pos = {x: k for k, x in enumerate(L)}
            for i in range(n):
                m = 0
                for j in range(n):
                    if pos[j] < pos[i]: m |= 1 << j
                inter[i] &= m
        rec("Thm1: histories of a pattern are one swap-class; intersection of histories = pattern", conn and tuple(inter) == P, (P,), 1)
# distinct patterns give distinct classes (labeled, n<=4): extension sets disjoint
for n in range(1, 5):
    allP = set()
    for P in polys[n]:
        # all relabelings
        for perm in itertools.permutations(range(n)):
            nb = [0]*n
            for i in range(n):
                m = 0
                for j in range(n):
                    if P[i] >> j & 1: m |= 1 << perm[j]
                nb[perm[i]] = m
            allP.add(tuple(nb))
    # injectivity: the set of histories determines the pattern (distinct labeled patterns, distinct history sets)
    sets = {}; ok = True
    for P in allP:
        key = frozenset(extensions(P))
        if key in sets and sets[key] != P: ok = False
        sets[key] = P
    rec("Thm1: the set of histories determines the pattern (distinct labeled patterns, n<=4)", ok, (n, len(allP)), len(allP))
    known = {1: 1, 2: 3, 3: 19, 4: 219}
    rec("labeled poset counts 1,3,19,219 (n=1..4) match known values", len(allP) == known[n], (n, len(allP)), 1)

# ---------- F. gluing at one shared element: crossing term formula
for a in range(1, 5):
    for b in range(1, 5):
        if a+b-1 > NMAX: continue
        for C in polys[a]:
            for D in polys[b]:
                for zc in range(a):
                    for zd in range(b):
                        # glue C[zc] with D[zd]: elements C then D minus zd mapped to zc
                        idx = {}
                        for j in range(b):
                            idx[j] = zc if j == zd else a + (j if j < zd else j-1)
                        edges = [(j, i) for i in range(a) for j in range(a) if C[i] >> j & 1]
                        edges += [(idx[j], idx[i]) for i in range(b) for j in range(b) if D[i] >> j & 1]
                        G = closure_from_edges(a+b-1, edges)
                        belowC = pc(C[zc]); aboveC = above_count(C)[zc]
                        belowD = pc(D[zd]); aboveD = above_count(D)[zd]
                        cross = R(G) - R(C) - R(D)
                        # transitivity: gluing adds below_C*above_D + below_D*above_C pairs
                        rec("Glue at one element z: R(G)=R(C)+R(D)+below_C(z)above_D(z)+below_D(z)above_C(z)", cross == belowC*aboveD + belowD*aboveC, (C, D, zc, zd), 1)

for k, (cnt, bad, ex) in res.items():
    print(("PASS" if bad == 0 else "FAIL"), cnt, k, "" if bad == 0 else (bad, ex))
