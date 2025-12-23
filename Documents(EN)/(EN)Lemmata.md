# Lemmas

**Lemma 1 (Maximum Entropy at Zero).**  
For each component \(e_j \in [-1,1]\), the entropy \(H_j(e_j)\) is maximal when \(e_j = 0\), i.e. when \(p_j = 0.5\).

*Proof idea:*  
Binary Shannon entropy \(H(p)\) is maximal at \(p = 0.5\). Since \(p_j = (e_j+1)/2\), this corresponds to \(e_j = 0\).

---

**Lemma 2 (Attractor Fields Reduce Entropy Relative to Random Initial States).**  
Let \(a \in [-1,1]^d\) be an attractor with relatively low entropy \(S(a)\).  
For a set of random initial states \(e^{(i)}_0\) with higher average entropy, and for small \(\gamma > 0\), the system satisfies:


\[
\bar{S}(t) \to S(a)
\]


as \(t \to \infty\).  
Thus, \(\bar{S}(t)\) decreases over time.

*Proof idea:*  
The iteration of \(T_a\) is a contraction toward \(a\). Entropy converges to the entropy of \(a\), which is lower than that of the initial distribution.

---

**Lemma 3 (Controlled Variation and Social Interaction Increase Resilience).**  
In a system with voluntary alignment (interaction + attractor + noise), variation persists around the attractor, enabling the system to respond to perturbations without leaving the attractor basin.

*Proof idea:*  
Social interaction pulls agents toward each other, the attractor pulls toward \(a\), and noise introduces limited variation.  
This produces a cluster with non‑zero spread, enabling adaptivity.

---

**Lemma 4 (Forced Uniformity Eliminates Variation).**  
In a system with strong forced uniformity toward a single state \(u\), the spread of states around \(u\) decreases to nearly zero.

*Proof idea:*  
A strong contraction toward a fixed point eliminates differences between agents; in the limit, all states equal \(u\).
