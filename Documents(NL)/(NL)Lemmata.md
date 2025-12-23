## Lemmata

**Lemma 1 (Maximale entropie rond 0).**  
Voor elke component \(e_j \in [-1,1]\) is de entropie \(H_j(e_j)\) maximaal wanneer \(e_j = 0\), d.w.z. \(p_j = 0{,}5\).

*Bewijsidee:*  
De binaire Shannon‑entropie \(H(p)\) is maximaal bij \(p=0{,}5\). Omdat \(p_j = (e_j+1)/2\), correspondeert \(p_j=0{,}5\) met \(e_j = 0\).

---

**Lemma 2 (Attractorveld verlaagt entropie ten opzichte van willekeurige beginsituaties).**  
Zij \(a \in [-1,1]^d\) een vaste attractor met relatief lage entropie \(S(a)\).  
Voor een verzameling willekeurige initiële toestanden \(e^{(i)}_0\) met hogere gemiddelde entropie geldt voor kleine \(\gamma > 0\) en voldoende tijdstappen dat:


\[
\bar{S}(t) \to S(a)
\]


en dus \(\bar{S}(t)\) daalt in de tijd.

*Bewijsidee:*  
De iteratie van \(T_a\) is een contractie richting \(a\). De entropie van de toestanden convergeert naar de entropie van \(a\), die per aanname lager is dan die van de startverdeling.

---

**Lemma 3 (Gecontroleerde variatie en sociale interactie verhogen veerkracht).**  
In een systeem met vrijwillige alignment (interactie + attractorveld + ruis) blijft er variatie in toestanden bestaan rond de attractor, waardoor het systeem kan reageren op verstoringen zonder de attractor te verlaten.

*Bewijsidee:*  
De sociale term trekt agents naar elkaar, de attractor trekt naar \(a\), en ruis introduceert beperkte variatie. Hierdoor ontstaat een cluster rond \(a\) met niet‑nul spreiding, wat adaptiviteit mogelijk maakt.

---

**Lemma 4 (Geforceerde uniformiteit verlaagt variatie).**  
In een dynamiek met sterke geforceerde uniformiteit naar één toestand \(u\) geldt dat de spreiding van de toestanden rond \(u\) in de tijd afneemt tot bijna nul.

*Bewijsidee:*  
Een sterke contractie naar een vaste toestand reduceert elk verschil tussen agents; in de limiet zijn alle toestanden gelijk aan \(u\), variatie verdwijnt.

