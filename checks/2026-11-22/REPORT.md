# Theorem checks on finite patterns (brute force)

Scripts: `common.py`, `check1.py` (run `python3 check1.py 7`, 18 s, output `out1_n7.txt`), `check2.py` (5 s, output `out2.txt`). Python only, no web.

**Method.** A pattern is a finite partial order. Every partial order is isomorphic to a naturally labeled one, so I enumerate all naturally labeled orders (counts 1, 2, 7, 40, 357, 4824, 96428 for n = 1..7; 63 unlabeled at n = 5 confirmed). "Link" = cover relation. R = number of related pairs. Random samples: 150 to 300 per theorem at n = 10 to 20 (histories counted only to n = 13, because the count is a sum over down-sets). Theorem numbers are from R2 section 3, with the R1 numbers (R1_math) in brackets.

## Results

| Theorem | Exact statement tested | Range | Result |
|---|---|---|---|
| Then law [V1, R1 Thm 14 proof] | R(C then D) = R(C)+R(D)+n(C)n(D), "then" = ordinal sum | all pairs, n(C)+n(D) <= 7 (216,309); 300 random, sizes 5 to 10 | PASS |
| Beside law | R(C beside D) = R(C) + R(D) | same pairs (216,009) | PASS |
| Identity | R = sum of what each x rests on = sum of f(x) = related pairs | all orders n <= 7, 300 random n 10 to 20 | PASS |
| Thm 6 / R1 Thm 7: warrant | false b: thoughts losing warrant (b and all above) number 1 + f(b) | all orders n <= 7, every b (708,178 cases); random n 10 to 20 | PASS |
| Thm 6 / R1 Thm 8: damage of a false link | cut link (u,v), rebuild: D = R(M) - R(M minus link) obeys 1 <= D <= (1+|past u|)(1+f(v)) | all orders n <= 7, every link (653,516 cases); random n 10 to 20 | PASS |
| R1 Thm 8.3 | lost pairs have a <= u, v <= c; a pair is kept iff some chain avoids the link | n <= 7; explicit paths n <= 6 | PASS |
| Fan | One premise under n - 1 unrelated consequences: a false link costs exactly 1 | n = 2 to 20 | PASS |
| Line | chain of n, false link after k-th: cost k(n-k); max floor(n^2/4) | n = 2 to 20, all k | PASS |
| Joint cost | C with one top, D with one bottom, one link: cutting loses exactly n(C)n(D) | n(C)+n(D) <= 7 (946 pairs) | PASS |
| Thm 15 / R2 Thm 12 (first half): histories never fall | births on any down-set S: e(P+x) >= e(P), equal iff S is all of P | all P n <= 6, every S; 300 random n=7; 320 random at n = 10 to 13 | PASS |
| Thm 1 | histories form one swap-class; their intersection is the pattern; history set determines pattern | all n <= 6; labeled n <= 4 (counts 1,3,19,219 match) | PASS |
| Thm 4 | links true => all relations true | all M, T up to 4 x 4 and 5 x 3 with every map (46,525 maps) | PASS |
| Thm 8 / R1 Thm 11 (kappa) | claims as a digraph: every world makes >= kappa claims false (kappa = fewest to drop for no cycle); some world exactly kappa | all claim sets n <= 3; n = 4 with <= 9 claims; 150 random at n = 5 (4,234 cases) | PASS |
| R1 Thm 12 (suspects) | claims in a minimal conflict = claims in a minimal repair (Reiter) | same sets with <= 10 claims (3,610 cases) | PASS |
| Thm 9 / R1 Thm 14: contradictory ideas cannot be joined | joint pattern exists iff union of claims acyclic; a<b in C and b<a in D => none | all labeled pairs n = 3, 4 (48,322 pairs; 30,164 with a direct conflict) | PASS |
| Thm 9 cost, tested form | glue at z: R = R(C)+R(D)+below_C above_D + below_D above_C | n(C)+n(D)-1 <= 7, every z pair (34,596) | PASS |
| N15 insight | y on side-by-side C, D: J(y) >= n(C)n(D) | all orders n <= 5, every C, D (12,872) | PASS |
| R1 Thm 14 ratio | k lines of n: apart kn(n-1)/2, one line kn(kn-1)/2; ratio (kn-1)/(n-1) -> k | k = 2, 3, 5; n = 5, 50, 500 | PASS |
| M12 pebbling | black pebble game on links, goal all tops: line 2 (n=1: 1); full binary tree of height h needs h+2 | lines n <= 8; trees h = 1, 2, 3 | PASS |
| M12 bounds | max direct-parent count + 1 <= pebbling number <= n | all orders n <= 6 (5,231) | PASS |
| Thm 17 | Z(1)=1, V=d ln Z/d beta, dV/d beta = variance >= 0, V(0) <= 0 <= V(1) | 2,000 random sets (numeric) | PASS |

**No FAIL in any theorem.** My first Thm 1 test failed because I tested the wrong claim (histories of different patterns are disjoint; false, one linear order is a history of many patterns). The right claim, that the history set determines the pattern, passes.

## Readings fixed

- Damage: the false link must be a link (cover relation). D counts every relation whose chains all use it, the link included. "Past(u)" means thoughts strictly below u.
- Warrant loss 1 + f is a set definition, so that PASS only shows the code matches the definition.
- Thm 15: a birth is a new top thought resting on any down-set.
- Thm 9 cost "about n(above a in C) x n(above b in D)" is vague. With one shared thought, those pairs are unrelated, so I found no reading where that product is the loss. The exact glue formula and the "then" term n(C) n(D) both hold. For contradictions I tested only that no join exists, not a count.

## Not tested

- Thm 5 (one layer behind): needs the model-theory definitions, not just orders.
- Lie larger than the report, recall, thm 13: definitional.
- 2^(n^2/4) growth: asymptotic (Kleitman and Rothschild), not testable at n <= 7.
- K-parent n^(-1/K): mean-field argument, simulation only.
- Pebbling trees checked only to h = 3.

## Summary (60 words)

Every checkable claim on finite patterns held. This covers the then law, the damage costs (fan 1, line k(n-k), up to n^2/4), warrant loss of 1 + f, histories never falling, and the contradiction join. Pebbling (line 2, tree h+2) also held. Checks ran on all orders to 7 elements plus random samples at 10 to 20. Several claims are definitional or not checkable this way.
