## Definities

**Definitie 1 (Emotieruimte).**  
Een agent heeft een emotionele toestand \( e \in [-1,1]^d \), waarbij \(d\) het aantal emotiedimensies is.

**Definitie 2 (Emotionele entropie).**  
Voor elke component \(e_j\) definiëren we:


\[
p_j = \frac{e_j + 1}{2}
\]


en de Shannon‑entropie:


\[
H_j(e_j) = -\left[p_j \log p_j + (1 - p_j)\log(1 - p_j)\right].
\]


De totale emotionele entropie van een agent:


\[
S(e) = \frac{1}{d}\sum_{j=1}^d H_j(e_j).
\]



**Definitie 3 (Systeementropie).**  
Voor een systeem van \(N\) agents met toestanden \(e^{(1)},\dots,e^{(N)}\) definiëren we:


\[
\bar{S} = \frac{1}{N}\sum_{i=1}^N S\big(e^{(i)}\big).
\]



**Definitie 4 (Attractorveld).**  
Een attractorveld wordt gegeven door een vector \(a \in [-1,1]^d\) en een update:


\[
T_a(e) = (1 - \gamma)e + \gamma a,
\]


met \( \gamma \in (0,1] \) de veldsterkte.

**Definitie 5 (Vrijwillige alignment vs geforceerde uniformiteit).**  
We noemen een dynamiek **vrijwillige alignment** als agents in interactie staan met elkaar en een attractorveld, met behoud van variatie en ruis.  
We noemen een dynamiek **geforceerde uniformiteit** als alle agents sterk en direct naar één (bijna) uniforme toestand worden geduwd, met minimale tegenwerkende variatie.
