---
layout: post
title: "Dual Resonance Models"
---

Resonance is one of the overarching themes of Physics. It's a simple, recurring pattern whose basic idea is crystal clear: when provided with energy a system oscillates only at a series of fixed "natural" frequencies; when driven by an oscillating input it absorbs more energy from it the closer the input frequency is to one of his natural frequencies. A system capable of oscillation therefore responds more strongly to a perturbation that is in tune with one of the notes it can play. Resonance is the reason behind why sometimes furniture starts vibrating only when a specific note is played on an instrument (electric bass players will understand) - it can happen your cupboard vibrates at a frequency close to a F#, and when and only when you poke it with that note it's going to absorb energy from sound and amplify its otherwise insignificant wobbling until it's practically rattling.

The standard prototype of resonance is the driven damped harmonic oscillator, but we don't need to be this explicit. Resonances all follow a universal pattern: if you drive the system at various frequencies \\(\omega\\), and plot the "response" \\(I(\omega)\\) as a function of the driving frequency, then you'll find peaks of increased response centered around the resonant frequencies; moreover these peaks are Lorentzian functions, meaning that if \\(\omega\\) is close to the natural frequency \\(\Omega\\) then:

$$ I(\omega) \sim \frac{1}{ (\omega - \Omega)^2 } $$

or, at least that's in the ideal case. A system without any sort of friction or in general some way to disperse energy will have an infinite response if you hit it just at the resonant frequency, which is clearly unrealistic. Accounting for the possibility of energy loss you end up with a broadening of the above into an actual Lorentzian peak:

$$ I(\omega) \sim \frac{ (\Gamma / 2)^2}{(\omega-\Omega)^2 + (\Gamma/2)^2 } $$

\\(\Gamma\\)'s a constant called the width of the resonance - pretty much because it's literally the width of the peak in the graph (the two points where \\(I(\omega)\\) is half its max value are \\(2\Gamma\\) apart)

(graph)

This resonance thing is not only for collapsing bridges or [breaking glasses](https://www.youtube.com/watch?v=17tqXgvCN0E), it's pretty much at the heart of particle physics. It is such a powerful idea that sometimes people call particles "resonances" instead of particles. (...)

A relativistic particle will always satisfy the mass-shell condition, which is

$$ m^2 = E^2 - (\vec p)^2 =: P^2 $$

where \\(E\\) is the energy, \\(p\\) is the linear momentum, and I can tidy up the notation by using four momentum \\(P^\mu = (E,\vec p) \\). That should be about as much relativity as we will need. So, each species of particle (where species are distinguished by all their quantum numbers, like charge and colour and so on) has a definite, invariable value for the mass \\(m\\), and actual instances of particles of that species must have four-momentum such that \\(P^2 = m^2 \\). Any relativistic theory of particles (like the standard model, but not necessarily) has a set of possible particles each with its given mass, and the set of masses is the mass spectrum of the theory. What is fascinating is that ultimately the masses are natural frequencies of the particle theory, which is to be seen as an oscillating system! So when you give energy to the system, it starts oscillating in its natural frequencies, that is to say you have created the corresponding particles.

(picture)

If so, and if our general analysis above applies, then these natural frequencies should be also *resonant* frequencies. To test this, we need to *drive* our particle theory at a specific mass (whatever this means) and then study how the "response" changes as a function of the driving mass. The most natural way to do it is to smash things together, an ingenious technique whose invention predates that of the wheel. For example, we can smash an electron and a positron together, and then get a muon and an antimuon as final products, or \\( e^- e^+ \rightarrow \mu^- \mu^+ \\). But how do you ensure you'll get \\(\mu\mu\\) as final product? Easy: you don't. You just do the experiment lots of times and ignore all events except the ones where you get exactly \\(\mu\mu\\). Now, we want to remain completely agnostic on the microscopic physics and all we can say is that after the collision of the \\(ee\\) pair, some unknown "stuff" is happening in the particle theory, which then breaks apart into a muon-antimuon pair. We can represent this in a spacetime diagram (**not** a Feynman diagram!):

(diagram)

Hopefully, this is the intended meaning of "driving" the system with an input. But what is the "input mass" at which we're driving the particle theory? A good candidate is the invariant mass, a.k.a. the centre-of-mass energy, of the \\(ee\\) pair. If their 4-momenta are \\(P_1\\) and \\(P_2\\), then the total 4-momentum is \\( P = P_1 + P_2 \\), which by conservation of 4-momentum (which is conservation of energy + conservation of linear momentum) must also be \\(P = P_3 + P_4\\) where those are the momenta of the final muons. The square of \\(P\\) is a Lorentz invariant

$$ s := (P_1 + P_2)^2 = (P_3 + P_4)^2 $$

\\(\sqrt s\\) is the centre-of-mass energy; it means that, once we have moved to the frame in which the temporary "blob" between \\(ee\\) and \\(\mu\mu\\) is stationary, then the "blob" contains energy \\(\sqrt s\\). It is the driving frequency.

Now that we know how to sing to the particle theory, how do we know whether it likes our music? What is the "response"? Well, we live in a quantum mechanical world, and quantum mechanical observables are probabilities. The response is thus gauged by the probability for the \\(ee \rightarrow \mu\mu\\) process to happen, which is measurable by counting the fraction of \\(ee\\) collisions that end up in \\(\mu\mu\\). This probabilty can then be plotted against the parameters of the collision (like \\(\sqrt s\\)).

{% include image.html name="zxsec.gif" caption="A plot of the cross-section (proportional to the probability) as a function of \(\sqrt s\) for various \(ee\rightarrow\) outcomes; \(\mu\mu\) is the lowermost one." %}


