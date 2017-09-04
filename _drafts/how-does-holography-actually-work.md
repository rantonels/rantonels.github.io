---
layout: post
title: "How does the holographic principle actually work?"
cover: cigarbw.jpg
---

This post hopefully manages to undo the ugliness of a blog about holography with no post yet entirely dedicated to it.

Holography is somewhat coming back in style in popular science, 


The holographic principle comes as a beautiful surprise in the quest for quantum gravity. Mostly because it makes *into* a quest what was supposed to be a long, boring hike. The problems that theoretical physics has successfully solved in the previous century have certainly turned out to involve a certain amount of powerful and unexpected machinery to some extent - in fact, symmetries have been the guiding light to the completion of the Standard Model, **but** it is also clear that Nature has been disappointingly conservative in involving exoticity. To explain strong interactions, our imaginations have explored innovative and elegant new models (including the embryo of string theory), and then it turned out to be explained by fairly mundane (relatively speaking) fundamental physics, not much different than quantum electrodynamics. In fact, it is QED with a few numbers changed. It was just essentially a matter of pushing through with accelerator experiment, jumping from one approximate symmetry to another, and just counting up all the fields you need to throw into this yet another quantum field theory. All of the Standard Model is a quantum field theory. Compared to what people where cooking up, that's *slightly* disappointing.

Holography confidently announces that this will not be the case with quantum gravity. It's not going to bestamp collecting. It's going to be **awesome**. It's going to be weird and counter-intuitive. It's **not** going to be *yet another quantum field theory*™. Here is why:

## Locality is false.

A respectable relativistic quantum field theory must be, amongst other things, a **local** theory. What this means is that near thing influence near things, i.e. there is no magic "action at a distance" of any sort. In other, more useful words, to describe the state of a local system, you can split space into tiny pieces and describe its state in each of these pieces independently. This might sound completely obvious, but it absolutely isn't. It is a property that a theory can or can not have. All QFTs have it. Now, consider a local theory set in a box of $$d$$-dimensional space, with side length $$ L $$. Let's split it as we said into tiny pieces, for example cubes of some small side length $$a$$. In each tiny cube, your local theory can be in a certain number of states $$ N $$. This might be infinite, but it's not really a problem - you can make it finite by discretizing some things, like in a field theory the points in space at which the field takes value (e.g. using the centre of the tiny cube) or discretizing the values the field can take. You can then take all the limits and regularizations you want (like $$a\rightarrow 0$$) at the end to make this continuous again - it doesn't matter, it only adds an additive constant to the entropy and it's not what we're looking for here.

So there's $$ N $$ possible states in each tiny cube. Also, since it's local, you can choose the state in each tiny cube independently, and in addition, there are $$ (L / a)^d $$ tiny cubes. Thus, there are

$$  N^{L^d a^{-d}} $$

states for the local theory in the box. Again, do what you want with $$ N $$ and $$ a $$, I don't care, what matters is that the number of states goes as 

$$ \exp( \mathrm{const} \cdot L^d ) $$

But if you recall your statmech, the total number of possible states is nothing else than the exponential of the entropy (using units with $$ k_B = 1 $$), so...

$$ S = \mathrm{const} \cdot L^d + \ldots $$

Or, in other words, the entropy is proportional to the $$ d $$-dimensional volume of the box. 

This should sound incredibly obvious. It's intuitive, right? Double the space, double the entropy, whatever what lives on space is. Yet, if the holographic principle is to be true, this has to be wrong. The HP says that a 3-dimensional *gravitational* theory must be **equal** to a 2-dimensional *local* theory. (Or you could generalize with $$d+1$$-dimensional gravity and a $$d$$-dimensional local theory). Since they are **equal**, and the states correspond, they have the same number of states, and so the same entropy. The 2D theory has an entropy that goes as an area:

$$ S \sim L^{2} $$

so the gravitational theory must too. But if the latter also *was* local, that would have to be $$ S \sim L^{3} $$, which cannot be. Hence, gravity is **non-local**.

How is this non-locality manifest? What goes wrong with the above argument in the case of gravity? One proposal is that there is an [inherent fuzziness at the Planck scale](/is-the-planck-length-the-minimum-possible-length/) that makes it impossible to localize stuff to smaller lengths; but that's not enough: just make the tiny cubes with $$ a = l_P $$ and that still gives you $$ S \sim L^3 $$. There's something much bigger going on. 

Take our gravitational theory, and discretize it on tiny cubes of side $$ l_P $$. Let's brutally simplify our theory as carrying one bit (two states, 0 and 1) for each tiny cube. You can literally do anything with bits: you want $$ N $$ states per cube? Use $$ \log_2 N $$ bits. It won't change the argument, so let's use one. Now if we want these bits to actually carry useful information (that can be stored *and* retrieved), close bits should be able to interact. If you're not convinced, imagine storing a bit of information in the spin of a particle: to distinguish the states and read the information, you have to couple the particle to something in such a way that the two states have different energies. Same here, we couple each bit to nearby bits. Now, it's clear by dimensional analysis that the coupling energy difference must be $$ \sim E_P$$, so let's take without loss of generality that two neighbouring bits with the same value have zero energy and different values have some energy of the order of the Planck energy.

Now, take some region of linear size $$ L $$. That has $$ n \sim (L/l_P)^3 $$ cubies. Since this is a gravitational theory, however, if the energy inside the region is large enough collapse into a black hole will happen, destroying our precious bits. The maximum energy before a black hole is formed is given by the famous Schwarzschild criterion, that in Planck units and ignoring numerical constants is

$$ E_\mathrm{MAX} \sim \left(\frac{L}{l_P} \right) E_P $$

which means we cannot actually have more than

$$ f  \sim \frac{L}{l_P} $$

facets between different-valued bits without the whole thing getting Schwarzschilded up. The surprising point is that *most* states are bad. In the large-size limit, the vast majority of states will have about 50% 0 and 50% 1; which means roughly 50% of the facets will carry energy. This means the energy of the average state is of order $$ (L/l_P)^3 E_P $$ and will be vastly larger than $$ E_\mathrm{MAX} $$.

How many "good" states remain there? It turns out it's about

$$ \exp S \sim \exp \left( \mathrm{const} \left( \frac{L}{l_P} \right)^2 \right)  $$

so entropy scales as the *surface area*, not as the volume, of the region, and is thus much smaller than it would be if gravity were local.

Black holes are direct manifestations of non-locality. The formation of a black hole is itself a global phenomenon. For example, imagine being in space, at centre of a very large shell of incoming radiation, whose total energy is enough to make a black hole much larger than you are. There comes a point where the radiation has fallen inside its Schwarzschild radius, but you cannot realize that with only local measurements, whose result is that spacetime is flat and empty around you. However, you are already doomed to hit the singularity - therefore by definition you are already inside an event horizon. At the moment the radiation crosses its Schwarzschild radius, the horizon has *already* formed some time before, right where you were, and has now grown to engulf the shell, and you had no idea. In fact, you would think everything is perfectly fine until your last moment before meeting the singularity. Not only: even if you had an array of local observers, from you to outside the Schwarzschild radius, none of them would be able to tell a horizon has formed and passed with local measurements. The *existence* itself of the black hole is non-local information.

## The Universe is discrete
