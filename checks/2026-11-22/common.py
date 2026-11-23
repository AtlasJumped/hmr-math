import random, itertools
from functools import lru_cache
pc = lambda x: bin(x).count("1")

def gen_natural(n):
    """All naturally labeled posets on n elements (i<j whenever a<b). below[i]=bitmask of elements strictly below i.
    Every poset is isomorphic to at least one. Counts: 1,2,7,40,357,4824,96428."""
    if n == 0:
        yield (); return
    for P in gen_natural(n-1):
        m = n-1
        # all down-sets of P as past of new element
        for S in range(1 << m):
            ok = True
            for j in range(m):
                if S >> j & 1 and (P[j] & ~S):
                    ok = False; break
            if ok:
                yield P + (S,)

def closure_from_edges(n, edges):
    below = [0]*n
    # natural labeling not assumed: do Warshall-like on bitmasks
    above_adj = [[] for _ in range(n)]
    for (a, b) in edges:
        below[b] |= 1 << a
    changed = True
    while changed:
        changed = False
        for i in range(n):
            m = below[i]
            new = m
            x = m
            while x:
                j = (x & -x).bit_length()-1
                new |= below[j]
                x &= x-1
            if new != m:
                below[i] = new; changed = True
    return tuple(below)

def covers(P):
    n = len(P); out = []
    for i in range(n):
        for j in range(n):
            if P[i] >> j & 1:
                # j<i; cover if no k with j<k<i
                if not any((P[i] >> k & 1) and (P[k] >> j & 1) for k in range(n)):
                    out.append((j, i))
    return out

def R(P): return sum(pc(m) for m in P)
def above_count(P):
    n = len(P); return [sum(1 for i in range(n) if P[i] >> x & 1) for x in range(n)]

def beside(C, D):
    n = len(C)
    return tuple(C) + tuple(m << n for m in D)
def then(C, D):
    n = len(C); full = (1 << n)-1
    return tuple(C) + tuple((m << n) | full for m in D)

def lin_ext(P):
    """number of linear extensions via DP over downsets (works for any labeling)."""
    n = len(P)
    cur = {0: 1}
    for _ in range(n):
        nxt = {}
        for S, c in cur.items():
            for x in range(n):
                if not (S >> x & 1) and (P[x] & ~S) == 0:
                    T = S | 1 << x
                    nxt[T] = nxt.get(T, 0) + c
        cur = nxt
    return cur[(1 << n)-1]

def extensions(P):
    n = len(P); res = []
    def rec(S, seq):
        if len(seq) == n: res.append(tuple(seq)); return
        for x in range(n):
            if not (S >> x & 1) and (P[x] & ~S) == 0:
                seq.append(x); rec(S | 1 << x, seq); seq.pop()
    rec(0, []); return res

def random_poset(n, p, rng):
    below = []
    for i in range(n):
        m = 0
        for j in range(i):
            if rng.random() < p: m |= 1 << j | below[j]
        below.append(m)
    # note: this closure gives transitively closed natural labeling
    return tuple(below)

def canon(P):
    n = len(P); best = None
    for perm in itertools.permutations(range(n)):
        # perm[old]=new
        newbelow = [0]*n
        for i in range(n):
            m = 0
            for j in range(n):
                if P[i] >> j & 1: m |= 1 << perm[j]
            newbelow[perm[i]] = m
        t = tuple(newbelow)
        if best is None or t < best: best = t
    return best
