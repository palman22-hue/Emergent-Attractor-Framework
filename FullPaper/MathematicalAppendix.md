# Mathematical Appendix  
**Formal Extensions and Proof Sketches**

This appendix provides additional mathematical detail supporting the definitions, lemmas, and theorem presented in the main text.

---

## 1. Entropy Properties

**Proposition 1 (Concavity of Entropy).**  
The binary Shannon entropy function  


\[
H(p) = -[p \log p + (1-p)\log(1-p)]
\]

  
is strictly concave on \(p \in (0,1)\).  
Therefore, for any convex combination of states, entropy is maximized at \(p=0.5\).

---

## 2. Convergence Under Attractor Dynamics

**Proposition 2 (Contraction Mapping).**  
The update rule  


\[
T_a(e) = (1-\gamma)e + \gamma a
\]

  
is a contraction mapping with contraction constant \((1-\gamma)\).  
Thus, repeated application yields convergence:  


\[
\lim_{t \to \infty} T_a^t(e_0) = a.
\]



---

## 3. System Entropy Evolution

**Lemma (Entropy Flow).**  
Let \(\bar{S}(t)\) denote average system entropy.  
If attractor entropy \(S(a)\) is lower than initial entropy, then:  


\[
\bar{S}(t) \to S(a).
\]



---

## 4. Stability Analysis

**Lyapunov Function Candidate.**  
Define  


\[
V(e) = \|e - a\|^2
\]

  
as a Lyapunov function.  
Then:  


\[
V(T_a(e)) = (1-\gamma)^2 V(e),
\]

  
showing exponential convergence toward \(a\).

---

## 5. Noise and Resilience

**Proposition 3 (Variance Preservation).**  
With additive bounded noise \(\eta_t\), the system converges not to a single point but to a distribution around \(a\).  
Variance is proportional to noise amplitude, ensuring non-zero spread.

---

## 6. Forced Uniformity Limit

**Proposition 4 (Degenerate Basin).**  
Under strong compression toward \(u\), the attractor basin collapses to a point.  
Variance tends to zero, eliminating resilience.

---

## 7. Summary

These mathematical results formalize the intuition:  
- Voluntary alignment → convergence with preserved variance.  
- Forced uniformity → convergence with collapsed variance.  
