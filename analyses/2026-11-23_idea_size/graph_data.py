# HMR claim graph, coded by one reader (Fable helper) from the live pages on 2026-11-23:
# math.html.body, physics.html.body, hmr.html.body. Health and other pages NOT coded.
# kinds: A assumption (stated starting claim) | I import (established result, cited) |
#        D definition | T result | N numerical result | R HMR reading | C conjecture/in progress | X open work item
# edge types: cs certified (script-checked, recomputed, or established with source)
#             ch certified by hand proof or directly from a definition
#             cn numerical runs within the stated range
#             as asserted (HMR reading / proposed meaning)
#             op open (conjecture, in progress)
NODES = """
A1|A|math|Reality is the thinking of one Universal Intelligence
A2|A|math|One element: a thought, which has only relations
A3|A|math|One relation, builds on: acyclic, finite past
A4|A|math|Only the pattern counts: birth order of unrelated thoughts is irrelevant
A5|A|math|No reaching across: next thought depends only on what it builds on
A6|A|math|Liking: every next thought has a chance, and chances are UI's liking
A7|A|math|No possible birth has chance zero (hypothesis of the rule theorem)
M1|A|math|About: a thought can be about another thought (reference, not derived)
M2|A|math|A part of the pattern has a bounded live set
M3|A|math|Every claim carries a range (domain)
P1|A|phys|A very large pattern of thoughts is spacetime-like
P2|A|phys|One thought is one unit of volume
P3|A|phys|Each crossing relation carries one bit, s = ln 2
P4|A|phys|Relations carry no structure beyond themselves
P5|A|phys|Quantum theory is borrowed: hbar, positive energy, locality
P6|A|phys|Energy crossing a boundary is recorded as new crossing relations
HF|A|hmr|Fascia is the body's primary system for health
I_counts|I|math|Counts of finite orders 1,1,2,5,16,63,318
I_birk|I|math|Birkhoff arithmetic of ordered sets
I_rs|I|math|Rideout and Sorkin 1999 classical sequential growth
I_bg|I|math|Brightwell and Georgiou 2010: no spacelike large-scale limit
I_bl|I|math|Brightwell and Luczak 2011 order-invariant measures
I_mors|I|math|Martin, OConnor, Rideout, Sorkin 2001 posts and renewal
I_bell|I|phys|Bell bound 2; measured 2.42 (Hensen 2015)
I_s94|I|phys|Sorkin 1994 pairs interfere, triples do not; Sinha 2010
I_craig|I|phys|Craig et al 2007 strong positivity gives 2 sqrt 2
I_mm|I|math|Myrheim-Meyer: related share fixes dimension
I_bhs|I|phys|Bombelli, Henson, Sorkin 2009 random scatter marks no frame; unlimited direct relations
I_brg|I|phys|Brightwell and Gregory 1991 longest chain is proper time
I_bart|I|phys|Barton et al 2019 horizon molecules gamma = sqrt3/10
I_bek|I|phys|Bekenstein black hole entropy A/4
I_unruh|I|phys|Unruh temperature (Bisognano-Wichmann 1975, Unruh 1976)
I_ray|I|phys|Raychaudhuri equation 1955
I_jac|I|phys|Jacobson 1995 Einstein equation of state
I_hl|I|phys|Hamilton and Lisle 2008 river model
I_adgs|I|phys|Ahmed, Dodelson, Greene, Sorkin 2004 Lambda about 1/sqrtN
I_john|I|phys|Johnston 2009 field on a causal set
I_gr|I|phys|General relativity standard results (extra radius GM/3c2, area theorem, clocks)
I_exp|I|math|Exponential family identities
I_gibbs|I|math|Relative entropy inequality
I_peb|I|math|Pebble game on derivation graphs
I_codata|I|phys|CODATA 2022 constants
I_vas|I|phys|Vasileiou 2013 no energy dependence of light speed
I_fein|I|phys|Fein 2019 interference above 25,000 amu
I_west|I|phys|Westphal 2021 gravity of 90 mg spheres
I_law|I|math|Lawvere 1969 fixed-point theorem
I_lind|I|math|Lindemann 1882 pi transcendental
I_wallis|I|math|Central binomial asymptotics give pi
I_clt|I|math|Central limit theorem rounds off grid walks
D_state|D|math|A state is a finite set of thoughts with came-before, acyclic
D_birth|D|math|Birth: attend to S; new thought after S and its past
T_blaws|T|math|Six laws of birth
T_grow|T|math|Every finite pattern can be grown from the void
T_tense|T|math|Three tenses: before, after, unrelated; time is order not a line
D_time|D|math|Time between thoughts is the longest chain
T_sizes|T|math|Four sizes of a thought; a uniform block acts as one thought
T_ops|T|math|Operators beside, then, inside, paired with their counts
T_then|T|math|R(C then D) = R(C)+R(D)+n(C)n(D); beside adds nothing
T_rsum|T|math|R equals sum of pasts and sum of futures
T_num|T|math|Number is order forgotten
T_prime|T|math|Inside does not commute; prime patterns
T_proc|T|math|Exponential growth only with parallel offspring
T_rule|T|math|Four conditions fix the rule family lambda(w,m)
T_simple|T|math|Simplest case p^m (1-p)^(n-w)
T_attn|T|math|The rule said as attention with weights t_k
T_family|T|math|The t_k are free: a family, not one law
T_cost|T|math|Chance of a pattern history p^links (1-p)^pairs apart
T_attract|T|math|Chance of building on a thought 1-(1-p)^(1+f)
T_pull|T|math|Two thoughts pull as a product
T_action|T|math|cost = -ln chance; chance = e^-cost
R_action|R|math|UI drawn to what it likes is least action in another vocabulary
R_temp|R|math|Temperature is how strictly UI follows its liking
T_complex|T|math|Complex p: pairs of histories interfere, triples do not (toy)
C_qlike|C|math|UI's liking is of the quantum kind
T_trans|T|math|Together carries through chains; apart holds pair by pair
R_tens|R|math|A pattern of thoughts is a tensegrity
T_mirror|T|math|Simplest rule cannot tell a pattern from its reverse
T_mm|T|math|Share of related pairs gives dimension; 1 in 10 in ours
T_line|T|math|Simplest rule: related share climbs to 100 percent
T_blind|T|math|Family sees only two counts; blind to shape
T_bell|T|math|Ordinary-chance rule cannot be the whole law (Bell)
T_nospace|T|math|No rule of the family has a spacetime-like limit
C_drop3|C|math|The condition to give up is the third, or go quantum
T_w|T|math|Rules keeping conditions 1,2,4 are reference chance times w(next)/w(now)
T_wsimple|T|math|Simplest rule is p=1/2 reweighted by w
R_wlike|R|math|w is how much UI likes a pattern
T_post|T|math|A post closes: earlier acts through one number; renewal formula
R_post|R|math|HMR completion is a post
C_bb|C|math|The Big Bang was a post (first complete self-model closing)
T_postfreq|T|math|How often a post happens
T_return|T|math|After closure rules are drawn toward the simplest rule
R_return|R|math|Each closed moment is a return to ground
D_ref|D|math|Reference map rho; grounded when rho(m) before m
D_idea|D|math|Idea = claims, matching, domain
T_trace|T|math|A pattern is its histories up to swaps
T_process|T|math|Process holds the law and the unborn candidates; pattern does not fix law
D_open|D|math|Open stage and commit
D_truth|D|math|Truthful, untruthful, undecided
D_faith|D|math|Truthful idea and faithful idea
D_warr|D|math|Warranted: rests on truthful thoughts, or checked directly
T_perm|T|math|Truth is permanent
T_base|T|math|The base layer cannot err
T_small|T|math|Smallest truthful thought; smallest thought that could be false
T_large|T|math|Largest truthful idea is one layer behind
D_dev|D|math|Ignorance, honest mistake, deliberate lie, slip
C_selfdec|C|math|Self-deception needs a part's own liking
T_lie|T|math|A lie is larger than the truth
T_errc|T|math|Errors combine; a liar with a false belief can say something true
T_nopref|T|math|Version 1 rule cannot prefer truth
D_emo|D|math|Feeling, mood, gain, surprise
T_mood|T|math|Mood rises with gain at a rate equal to spread of feeling
T_fsum|T|math|Feelings sum to ln w; expected feeling never negative
R_suffer|R|math|Suffering is a signal the model is wrong
C_named|C|math|Named emotions live in the gap between expected and delivered
D_cons|D|math|Consistent: some possible pattern satisfies all claims
T_kappa|T|math|Inconsistent idea is false by at least kappa claims in every world
T_susp|T|math|Suspects are claims in a smallest repair; warrant lost above them
T_noclose|T|math|An inconsistent idea cannot be closed with warrant
T_nojoin|T|math|Contradicting ideas cannot be joined; join exists iff no circle
T_keep|T|math|Consistent parts keep full size
T_depth|T|math|Cost of a contradiction depends on depth
T_1k|T|math|k parts held apart hold about 1/k
T_range|T|math|Ranges soften a contradiction
C_closemean|C|math|Closure must be read at the level of meaning
T_f1|T|math|An idea with a false part is not wholly true
T_f2|T|math|A false thought removes warrant of exactly 1+f thoughts
T_f3|T|math|A second chain or direct check keeps truth
T_whole|T|math|True parts with true links give a true whole; joins can fail
T_D|T|math|A false link costs D relations, bounded
T_surv|T|math|A relation survives iff a chain avoids the false link
T_fpred|T|math|A failed prediction implies a false link on every chain to it
T_shape|T|math|Fan costs 1, line costs k(n-k), braced costs 1
R_hline|R|math|HMR's own narrative is close to a line
D_healthy|D|math|Healthy: consistent, grounded, braced, correctable, growing
D_good|D|math|Good: UI likes the pattern more with the thought
R_notmost|R|math|The liked model is the true one, not the most connected
D_live|D|math|Live set of a part
T_demand|T|math|Demand of an idea: line 2, tree h+2
R_wm|R|math|Demand is working memory
D_train|D|math|Train of thought, pause, rumination, tip of the tongue
T_lose|T|math|Newest thought is easiest to lose (simplest rule)
R_persp|R|math|Perspective: only the latest thoughts are seen directly
T_recall|T|math|Recall is a new thought about an old one and can be false
T_insight|T|math|Insight joins at least n(C)n(D) pairs
T_hist|T|math|Number of histories never falls under birth
T_enid|T|math|-ln chance(pattern) = cost - ln e(P)
R_energy|R|math|cost minus ln liking is the energy-like quantity
T_nomem|T|phys|Version 1 family cannot remember: late shape independent of early
T_rules|T|phys|So no memory, no recurring idea, no particle, no about from that law
R_onereq|R|phys|Memory, particle, and about are one requirement on the law
N_seven|N|phys|Seven shape-seeing rules: none gives lasting memory with a dimension
N_copy|N|phys|Copy rules remember (0.4 to 0.9)
N_lines|N|phys|Shapes carry themselves forward in lines of descent
N_freeze|N|phys|Local copying freezes, does not store
N_bit|N|phys|A two-way bit, one for the whole pattern
N_copydim|N|phys|Copy rules hold no dimension
N_copycost|N|phys|Copy rules break conditions 2 and 3
C_store|C|phys|A refreshed local store is the next lead
N_K|N|phys|K rule: steady exponential growth, rates
N_Kdim|N|phys|K rule: share falls as n^(-1/K); no dimension
T_Kimp|T|phys|No rule with bounded direct parents grows a frame-free space
T_req|T|phys|Focus must be unlimited and depend on nearness
N_bal|N|phys|A liking for the 1-in-10 balance is not enough
C_infl|C|phys|Inflation is growth after closure
T_phase|T|phys|Only the geometric part of weights survives a closed moment
C_pair|C|phys|The matched-pair family may keep phases
U_causet|T|phys|Thoughts in order are a causal set
U_vol|T|phys|V = N l0^4 defines the first distance
U_gamma|T|phys|A surface is crossed by gamma A / l0^2 relations, gamma = sqrt3/10
U_S|T|phys|Boundary entropy S = s gamma A / l0^2
U_l0|T|phys|l0 = 2 sqrt(s gamma) Planck lengths = 0.693
U_units|T|phys|t0, m0, G = 1/(4 s gamma), 4.34 thoughts per Planck volume
U_counts|T|phys|Electron, atom, second, universe in first distances
U_two|T|phys|nC x nS = 1/(2 s gamma) for every object (identity)
R_two|R|phys|Every object is two numbers of distance
U_step|T|phys|One link is 0.66 to 0.90 of t0
U_disp|T|phys|Matter adds GM/3c2 of radial distance (standard GR)
R_disp|R|phys|Matter displaces distance
U_merge|T|phys|Merging horizons gain a cross term 8 pi gamma r1 r2 / l0^2
R_trade|R|phys|The whole is more than its parts with a trade-off
U_flat|T|phys|A flat empty region has N^2/20 related pairs and no weight
G1|T|phys|Grid ruled out; scatter is random and frame-free; c = l0/t0
G3|T|phys|Accelerated observer sees Unruh temperature
G4|T|phys|Coherence displaces distance: s dN = dQ/T
G5|T|phys|Curvature is the acceleration of the relation count
G6|T|phys|Einstein equations with G = c^3 l0^2/(4 hbar s gamma)
G6v|T|phys|Evenly spread energy drops out of the equations
C_vac|C|phys|Empty space carries no weight
G_fin|T|phys|Finite count: no point of infinite density
L_cone|T|phys|Light cone is the order of building; c is an exchange rate
L_free|T|phys|Free fall is the longest chain
R_most|R|phys|Free fall is the path of most thoughts
L_slow|T|phys|Slower time fits the count; denser thought does not
DE|T|phys|Lambda about 1/sqrtN: 4e-122 against measured 2.8e-122 (borrowed)
DE_w|T|phys|Dark energy amount should wander over cosmic time
R_de|R|phys|Dark energy is the universe continuing to model itself
Q_rung|T|phys|Quantum theory is one rung above chance
Q_lim|T|phys|One rung up with strong positivity scores at most 2.83
R_cond|R|phys|UI's rule carries the strong positivity condition
R_ent|R|phys|Entanglement: joined in UI's pattern stays joined
GK_two|T|phys|Patterns are counted; the order is one and its properties are averages
C_gk|C|phys|Gravity is not the kind of thing that is quantized
C_f1|C|phys|Form 1: the order is undecided between records
C_f2|C|phys|Form 2: definite order with an inner state
TC_clash|T|phys|Claims A, B, C of physics cannot all hold
TC_range|T|phys|Tested ranges of A,B and C are 18 powers of ten apart
R_tccost|R|phys|The clash costs physics the whole join, not the tested body
C_free|C|phys|HMR does not have to hold all three
R_meas|R|phys|A measurement is a commit
C_commit|C|phys|A commit is the making of a record
R_dm|R|phys|Dark matter: look where the local-horizon assumption fails
R_planck|R|phys|Nothing finer than about two first distances
P_field|T|phys|A quantum field on a spacetime-shaped pattern has particle-like ripples
C_part|C|phys|A particle is a shape in the order that lasts and recurs
R_bb|R|phys|Big Bang: first complete self-model closing and igniting
R_fine|R|phys|Constants are rules UI held fixed, chosen
R_arrow|R|phys|Time runs one way because maturation does
R_consc|R|phys|Consciousness is fundamental
S_fan|T|math|HMR's mechanics picks the fan as first shape
S_shuf|T|math|n! shuffles of the fan: first form of turning
S_orbit|T|math|Sphere and 2 pi d0 follow only if flat space is assumed
S_pic|T|math|pi comes out of counted two-way choices
R_pi|R|math|pi is the signature of the first boundary
BB_fix|T|math|S* = F(S*) has no finite solution
BB_law|T|math|No complete two-valued self-model exists
C_three|C|math|Closure forces: partial, undecided, or alternation
PX_zeno|T|math|Zeno paradoxes cannot arise
PX_super|T|math|Supertask paradoxes cannot arise
PX_hotel|T|math|Hilbert hotel and Galileo paradox cannot arise
PX_ban|T|math|Banach-Tarski type paradoxes cannot arise
PX_self|T|math|Self-containing paradoxes cannot arise
MP1|C|math|Prediction: Riemann hypothesis
MP2|C|math|Prediction: P versus NP
MP3|C|math|Prediction: Navier-Stokes
MP4|C|math|Prediction: Yang-Mills mass gap
MP5|C|math|Prediction: Hodge
MP6|C|math|Prediction: Birch and Swinnerton-Dyer
MP7|C|math|Reading of Poincare
H_emerge|R|hmr|Physical reality emerges from UI
H_coh|R|hmr|UI's changes trend toward coherence
H_laws|R|hmr|Laws of physics are the stable rules of a shared world
H_body|R|hmr|Living bodies are vessels; each human is an instance of UI
H_nocontra|R|hmr|HMR contradicts no established science
H_values|R|hmr|HMR Values: how to live
H_east|R|hmr|East and West describe one reality
H_health|R|hmr|Holistic health model: fascia-first care
H_perfect|R|hmr|Health is measured against an ideal body defined by physics
H_proto|R|hmr|Fascia health protocol
H_mental|R|hmr|Mental health model: baseline for body, reality, and values
H_test|C|hmr|A body model derived from HMR can simulate and help reverse disease
X_law|X|open|A rule of growth that yields space (three dimensions, steady)
X_q|X|open|A quantum rule for births
X_mem|X|open|A law with a rewritable memory in one place (about, derived)
X_bit|X|open|The bit derived from the rule of growth
X_lev|X|open|Levels: the law carried from single thoughts to human minds
X_w|X|open|UI's own liking and HMR's values written in the mathematics
X_part|X|open|One pure number: a lasting pattern with a period (mass ratio)
X_coh|X|open|One number for coherence
X_inv|X|open|Inversion: a part that carries a model of itself (life)
"""
EDGES = """
A2>D_state|ch; A3>D_state|ch; D_state>D_birth|ch; D_birth>T_blaws|ch; D_birth>T_grow|cs; I_counts>T_grow|cs
D_state>T_tense|ch; A4>T_tense|ch; T_tense>D_time|ch; D_state>T_sizes|ch; D_state>T_ops|cs; I_birk>T_ops|cs
T_ops>T_then|cs; D_state>T_rsum|cs; T_ops>T_num|cs; T_ops>T_prime|cs; D_birth>T_proc|ch
D_birth>T_rule|cs; A4>T_rule|cs; A5>T_rule|cs; A6>T_rule|cs; A7>T_rule|cs; I_rs>T_rule|cs
T_rule>T_simple|cs; T_rule>T_attn|cs; T_rule>T_family|cs; T_simple>T_cost|cs; T_simple>T_attract|cs
T_attract>T_pull|cs; T_cost>T_action|cs; T_action>R_action|as; A6>R_action|as; T_action>R_temp|as
T_simple>T_complex|ch; I_s94>T_complex|cs; T_complex>C_qlike|op; T_bell>C_qlike|op
D_state>T_trans|cs; T_trans>R_tens|as; T_cost>T_mirror|cs; D_state>T_mm|cs; I_mm>T_mm|cs
T_simple>T_line|ch; T_rule>T_blind|cs; T_rule>T_bell|cs; I_bell>T_bell|cs; T_rule>T_nospace|cs; I_bg>T_nospace|cs
T_nospace>C_drop3|op; T_bell>C_drop3|op; T_nomem>C_drop3|op; T_nopref>C_drop3|op
T_rule>T_w|cs; I_bl>T_w|cs; T_w>T_wsimple|ch; T_simple>T_wsimple|ch; T_w>R_wlike|as; A6>R_wlike|as
T_rule>T_post|cs; I_mors>T_post|cs; T_post>R_post|as; R_post>C_bb|op; A1>C_bb|op; BB_law>C_bb|op
T_simple>T_postfreq|cn; T_post>T_postfreq|cn; T_post>T_return|cs; T_return>R_return|as
M1>D_ref|ch; D_state>D_ref|ch; D_ref>D_idea|ch; M3>D_idea|ch
D_birth>T_trace|cs; A4>T_trace|cs; T_trace>T_process|ch; T_family>T_process|ch
A6>D_open|ch; D_birth>D_open|ch; D_ref>D_truth|ch; D_truth>D_faith|ch; D_truth>D_warr|ch
D_truth>T_perm|ch; T_blaws>T_perm|ch; D_truth>T_base|ch; D_truth>T_small|ch; T_tense>T_small|ch
D_truth>T_large|ch; D_truth>D_dev|ch; D_idea>D_dev|ch; D_dev>C_selfdec|op; D_dev>T_lie|ch; D_dev>T_errc|ch
T_blind>T_nopref|ch; D_truth>T_nopref|ch
T_w>D_emo|ch; A6>D_emo|ch; D_emo>T_mood|cs; I_exp>T_mood|cs; D_emo>T_fsum|ch; I_gibbs>T_fsum|ch
T_fsum>R_suffer|as; D_emo>C_named|op
D_idea>D_cons|ch; D_cons>T_kappa|cs; D_truth>T_kappa|cs; T_kappa>T_susp|cs; D_warr>T_susp|cs; T_susp>T_noclose|ch
D_cons>T_nojoin|cs; T_then>T_nojoin|cs; T_nojoin>T_keep|ch; T_susp>T_depth|ch; T_nojoin>T_depth|ch
T_nojoin>T_1k|cs; T_nojoin>T_range|ch; D_idea>T_range|ch; T_post>C_closemean|op; D_cons>C_closemean|op
D_truth>T_f1|ch; D_warr>T_f2|cs; D_warr>T_f3|cs; D_truth>T_whole|cs; D_warr>T_D|cs; T_rsum>T_D|cs
T_D>T_surv|cs; D_truth>T_fpred|ch; T_D>T_shape|cs; T_shape>R_hline|as
D_cons>D_healthy|ch; D_warr>D_healthy|ch; T_shape>D_healthy|ch; T_perm>D_healthy|ch; T_insight>D_healthy|ch
T_w>D_good|ch; A6>D_good|ch; T_line>R_notmost|as; T_mm>R_notmost|as; D_good>R_notmost|as
M2>D_live|ch; D_state>D_live|ch; D_live>T_demand|cs; I_peb>T_demand|cs; T_demand>R_wm|as
D_live>D_train|ch; D_open>D_train|ch; T_attract>T_lose|ch; D_live>T_lose|ch
D_state>R_persp|as; R_persp>T_recall|ch; D_truth>T_recall|ch; T_then>T_insight|cs
T_trace>T_hist|cs; T_cost>T_enid|ch; T_trace>T_enid|ch; T_w>T_enid|ch; T_enid>R_energy|as
T_blind>T_nomem|ch; T_nomem>T_rules|ch; D_ref>T_rules|ch; T_rules>R_onereq|as
D_birth>N_seven|cn; D_birth>N_copy|cn; N_copy>N_lines|cn; N_copy>N_freeze|cn; N_copy>N_bit|cn
N_copy>N_copydim|cn; T_mm>N_copydim|cn; N_copy>N_copycost|cn; T_rule>N_copycost|cn; N_bit>C_store|op; N_freeze>C_store|op
D_birth>N_K|cn; T_proc>N_K|cn; N_K>N_Kdim|cn; T_mm>N_Kdim|cn; I_bhs>T_Kimp|ch; N_K>T_Kimp|ch; T_Kimp>T_req|ch
T_mm>N_bal|cn; T_w>N_bal|cn; N_K>C_infl|op; C_bb>C_infl|op; T_post>T_phase|ch; T_complex>T_phase|ch; T_phase>C_pair|op
D_state>U_causet|cs; I_rs>U_causet|cs; P1>U_vol|ch; P2>U_vol|ch; U_causet>U_vol|ch
U_vol>U_gamma|cs; I_bart>U_gamma|cs; U_gamma>U_S|ch; P3>U_S|ch; U_S>U_l0|cs; I_bek>U_l0|cs
U_l0>U_units|cs; I_codata>U_units|cs; U_units>U_counts|cs; U_units>U_two|cs; U_two>R_two|as
U_units>U_step|cs; I_brg>U_step|cs; D_time>U_step|cs; I_gr>U_disp|cs; U_disp>R_disp|as
U_gamma>U_merge|cs; I_gr>U_merge|cs; U_merge>R_trade|as; T_then>R_trade|as
T_mm>U_flat|cs; U_vol>U_flat|cs
P4>G1|ch; U_vol>G1|ch; I_bhs>G1|cs; I_vas>G1|cs
P5>G3|cs; I_unruh>G3|cs; G1>G3|ch; P6>G4|ch; G3>G4|ch; U_S>G4|ch; I_ray>G5|cs; U_gamma>G5|ch
G4>G6|ch; G5>G6|ch; I_jac>G6|cs; U_l0>G6|ch; G6>G6v|ch; G6v>C_vac|op; U_flat>C_vac|op
U_vol>G_fin|ch; P1>L_cone|cs; D_state>L_cone|cs; D_time>L_free|cs; P1>L_free|cs; I_brg>L_free|cs
L_free>R_most|as; U_vol>L_slow|ch; L_free>L_slow|ch; I_gr>L_slow|cs
U_vol>DE|cs; I_adgs>DE|cs; DE>DE_w|cs; DE>R_de|as; A1>R_de|as
I_s94>Q_rung|cs; I_bell>Q_rung|cs; Q_rung>Q_lim|cs; I_craig>Q_lim|cs; Q_lim>R_cond|as; T_bell>R_cond|as
I_bell>R_ent|as; A1>R_ent|as
D_state>GK_two|ch; U_vol>GK_two|ch; GK_two>C_gk|op; G6>C_gk|op; I_jac>C_gk|op; C_gk>C_f1|op; C_gk>C_f2|op
D_cons>TC_clash|ch; I_gr>TC_clash|ch; I_fein>TC_range|cs; I_west>TC_range|cs
TC_clash>R_tccost|as; TC_range>R_tccost|as; T_depth>R_tccost|as; T_range>R_tccost|as
TC_clash>C_free|op; C_f1>C_free|op; C_f2>C_free|op
D_open>R_meas|as; R_meas>C_commit|op; T_rules>C_commit|op
G4>R_dm|as; U_units>R_planck|as; U_gamma>R_planck|as
P1>P_field|cs; I_john>P_field|cs; R_onereq>C_part|op; N_lines>C_part|op
A1>R_bb|as; A1>R_fine|as; T_return>R_fine|as; A1>R_arrow|as; T_hist>R_arrow|as; A1>R_consc|as
D_state>S_fan|ch; S_fan>S_shuf|ch; I_wallis>S_pic|cs; I_clt>S_pic|cs
S_pic>R_pi|as; I_lind>R_pi|as; A1>R_pi|as
D_birth>BB_fix|cs; I_law>BB_law|cs; BB_law>C_three|op; BB_fix>C_three|op
A3>PX_zeno|ch; A3>PX_super|ch; D_state>PX_hotel|ch; U_vol>PX_ban|ch; A3>PX_self|ch
A1>MP1|op; D_state>MP1|op; A1>MP2|op; D_state>MP2|op; A1>MP3|op; D_state>MP3|op; A1>MP4|op; D_state>MP4|op
A1>MP5|op; D_state>MP5|op; A1>MP6|op; D_state>MP6|op; A1>MP7|op; D_state>MP7|op
A1>H_emerge|as; D_state>H_emerge|as; A6>H_coh|as; A1>H_coh|as; H_emerge>H_laws|as; T_return>H_laws|as
H_emerge>H_body|as; H_emerge>H_nocontra|as; G6>H_nocontra|as; H_coh>H_values|as; H_body>H_values|as
H_emerge>H_east|as; HF>H_health|as; H_body>H_health|as; HF>H_perfect|as; H_health>H_proto|as
H_health>H_mental|as; H_values>H_mental|as; H_perfect>H_test|op; H_health>H_test|op
D_birth>X_law|op; A4>X_law|op; A6>X_law|op; T_req>X_law|op; X_law>P1|op; X_law>P4|op; X_law>C_infl|op; X_law>C_bb|op; X_law>C_gk|op
T_complex>X_q|op; T_phase>X_q|op; Q_lim>X_q|op; X_q>P5|op; X_q>C_qlike|op; X_q>X_law|op; X_q>C_commit|op
N_bit>X_mem|op; N_copy>X_mem|op; C_store>X_mem|op; X_mem>M1|op; X_mem>C_part|op; X_mem>C_commit|op
X_law>X_bit|op; X_bit>P3|op; X_bit>P6|op
T_sizes>X_lev|op; D_live>X_lev|op; X_lev>R_wm|op; X_lev>H_body|op; X_lev>C_selfdec|op; X_lev>H_mental|op
A6>X_w|op; D_good>X_w|op; X_w>H_values|op; X_w>H_coh|op; X_w>X_coh|op
X_mem>X_part|op; X_q>X_part|op; C_part>X_part|op
X_coh>C_vac|op; X_coh>H_health|op
X_mem>X_inv|op; BB_law>X_inv|op; X_inv>H_body|op
"""
