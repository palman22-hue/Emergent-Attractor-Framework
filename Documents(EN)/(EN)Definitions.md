# Definitions

**Definition 1 (Emotional State Space).**  
An agent has an emotional state \( e \in [-1,1]^d \), where \(d\) is the number of emotional dimensions.

**Definition 2 (Emotional Entropy).**  
For each component \(e_j\), define:


\[
p_j = \frac{e_j + 1}{2}
\]


and the Shannon entropy:


\[
H_j(e_j) = -\left[p_j \log p_j + (1 - p_j)\log(1 - p_j)\right].
\]


The total emotional entropy of an agent is:


\[
S(e) = \frac{1}{d}\sum_{j=1}^d H_j(e_j).
\]



**Definition 3 (System Entropy).**  
For a system of \(N\) agents with states \(e^{(1)},\dots,e^{(N)}\), define:


\[
\bar{S} = \frac{1}{N}\sum_{i=1}^N S\big(e^{(i)}\big).
\]



**Definition 4 (Attractor Field).**  
An attractor field is defined by a vector \(a \in [-1,1]^d\) and an update rule:


\[
T_a(e) = (1 - \gamma)e + \gamma a,
\]


with \( \gamma \in (0,1] \) the field strength.

**Definition 5 (Voluntary Alignment vs Forced Uniformity).**  
A system exhibits **voluntary alignment** when agents move toward an attractor through a combination of social interaction, attractor influence, and noise, while preserving variation.  
A system exhibits **forced uniformity** when agents are strongly and directly pushed toward a single state \(u\), with minimal opposing variation.
