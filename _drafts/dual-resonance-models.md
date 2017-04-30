---
layout: post
title: "Dual Resonance Models"
---

Resonance is one of the overarching themes of Physics. It's a simple, recurring pattern whose basic idea is crystal clear: when provided with energy a system oscillates only at a series of fixed "natural" frequencies; when driven by an oscillating input it absorbs more energy from it the closer the input frequency is to one of his natural frequencies. A system capable of oscillation therefore responds more strongly to a perturbation that is in tune with one of the notes it can play. Resonance is the reason behind why sometimes furniture starts vibrating only when a specific note is played on an instrument (electric bass players will understand) - it can happen your cupboard vibrates at a frequency close to a F#, and when and only when you poke it with that note it's going to absorb energy from sound and amplify its otherwise insignificant wobbling until it's practically rattling.

The standard prototype of resonance is the driven damped harmonic oscillator, but we don't need to be this explicit. Resonances all follow a universal pattern: if you drive the system at various frequencies \\(\omega\\), and plot the "response" \\(I(\omega)\\) as a function of the driving frequency, then you'll find peaks of increased response centered around the resonant frequencies; moreover these peaks are Lorentzian functions, meaning that if \\(\omega\\) is close to the natural frequency \\(\Omega\\) then:

$$ I(\omega) \sim \frac{1}{ (\omega - \Omega)^2 } $$

or, at least that's in the ideal case. A system without any sort of friction or in general some way to disperse energy will have an infinite response if you hit it just at the resonant frequency, which is clearly unrealistic. Accounting for the possibility of energy loss you end up with a broadening of the above into an actual Lorentzian peak:

$$ I(\omega) \sim \frac{ 1}{(\omega-\Omega)^2 + (\Gamma/2)^2 } $$

\\(\Gamma\\)'s a constant called the width of the resonance - pretty much because it's literally the width of the peak in the graph (the two points where \\(I(\omega)\\) is half its max value are \\(2\Gamma\\) apart)

{% include image.html name="resonanceplot.png" caption="The response profile about a resonance. On the left, the ideal case, on the right, in the presence of some kind of damping, which results in a broadening of the peak.." %}

This resonance thing is not only for collapsing bridges or [breaking glasses](https://www.youtube.com/watch?v=17tqXgvCN0E), it's pretty much at the heart of particle physics. It is such a powerful idea that sometimes people call particles "resonances" instead of particles. (...)

A relativistic particle will always satisfy the mass-shell condition, which is

$$ m^2 = E^2 - (\vec p)^2 =: P^2 $$

where \\(E\\) is the energy, \\(p\\) is the linear momentum, and I can tidy up the notation by using four momentum \\(P^\mu = (E,\vec p) \\). That should be about as much relativity as we will need. So, each species of particle (where species are distinguished by all their quantum numbers, like charge and colour and so on) has a definite, invariable value for the mass \\(m\\), and actual instances of particles of that species must have four-momentum such that \\(P^2 = m^2 \\). Any relativistic theory of particles (like the standard model, but not necessarily) has a set of possible particles each with its given mass, and the set of masses is the mass spectrum of the theory. What is fascinating is that ultimately the masses are natural frequencies of the particle theory, which is to be seen as an oscillating system! So when you give energy to the system, it starts oscillating in its natural frequencies, that is to say you have created the corresponding particles.

(picture)

If so, and if our general analysis above applies, then these natural frequencies should be also *resonant* frequencies. To test this, we need to *drive* our particle theory at a specific mass (whatever this means) and then study how the "response" changes as a function of the driving mass. The most natural way to do it is to smash things together, an ingenious technique whose invention predates that of the wheel. For example, we can smash an electron and a positron together, and then get a muon and an antimuon as final products, or \\( e^- e^+ \rightarrow \mu^- \mu^+ \\). But how do you ensure you'll get \\(\mu\mu\\) as final product? Easy: you don't. You just do the experiment lots of times and ignore all events except the ones where you get exactly \\(\mu\mu\\). Now, we want to remain completely agnostic on the microscopic physics and all we can say is that after the collision of the \\(ee\\) pair, some unknown "stuff" is happening in the particle theory, which then breaks apart into a muon-antimuon pair. We can represent this in a spacetime diagram (**not** a Feynman diagram!):

{% include image.html name="eemumu.png" caption="" %}

Hopefully, this is the intended meaning of "driving" the system with an input. But what is the "input mass" at which we're perturbing the particle theory? A good candidate is the invariant mass, a.k.a. the centre-of-mass energy, of the \\(ee\\) pair. If their 4-momenta are \\(P_1\\) and \\(P_2\\), then the total 4-momentum is \\( P = P_1 + P_2 \\), which by conservation of 4-momentum (which is conservation of energy + conservation of linear momentum) must also be \\(P = P_3 + P_4\\) where those are the momenta of the final muons. The square of \\(P\\) is a Lorentz invariant

$$ s := (P_1 + P_2)^2 = (P_3 + P_4)^2 $$

\\(\sqrt s\\) is the centre-of-mass energy; it means that, once we have moved to the frame in which the temporary "blob" between \\(ee\\) and \\(\mu\mu\\) is stationary, then the "blob" contains energy \\(\sqrt s\\). It is the driving frequency.

Now that we know how to sing to the particle theory, how do we know whether it likes our music? What is the "response"? Well, we live in a quantum mechanical world, and quantum mechanical observables are probabilities. The response is thus gauged by the probability for the \\(ee \rightarrow \mu\mu\\) process to happen, which is measurable by counting the fraction of \\(ee\\) collisions that end up in \\(\mu\mu\\). This probabilty can then be plotted against the parameters of the collision (like \\(\sqrt s\\)).

{% include image.html name="zxsec.gif" caption="A plot of the cross-section (proportional to the probability) as a function of \(\sqrt s\) for various \(ee\rightarrow\) outcomes; we are interested in the \(\mu\mu\) curve." %}

And when you do plot it in the range \\(40 - 120 GeV\\) you'll find something interesting: a resonance peak! It has the Lorentzian profile we discussed earlier, centered on about \\(91 GeV\\) and with a width \\( \Gamma \sim 2.4 GeV \\). This resonance corresponds to nothing else than the \\(Z^0\\) boson, whose mass is indeed \\(\sim 91 GeV\\). Since the Z is a particle that exists in the standard model, its mass is a natural and so resonant energy for the standard model, and if you tickle the latter around the Z-boson mass you will measure an enhanced response. And in general, you'll find resonance peaks at all masses of possible particles, which is why particle and resonance tend to be used as synonyms in particle physics.

(picture)

## Particles = Poles

One way to understand why the existence of a particle induces a resonance in a quantum mechanical theory is to picture it in terms of virtual processes. Basically, all possible *classical* ways for \\(ee\\) to turn into \\(\mu\mu\\), except you don't care about satisfying the mass-shell condition \\(E^2 - \vec p^2 = m^2 \\), you're *off-shell*. The intermediate off-shell particles that appear in all of these possible history (each making their humble contribution to the truth, so to speak) are called virtual. Every virtual history has its own "strength", the quantum amplitude, a complex number. If you have a series of histories called \\(1,2,3,\ldots\\) each bringing its amplitude \\(A_1, A_2, A_3, \ldots \\) you can compute the total quantum amplitude for the process as the sum of the amplitudes:

$$ A = A_1 + A_2 + A_3 + \ldots $$

and finally, the probability is proportional to \\( \|A\|^2 \\), the norm squared of the total amplitude. That's more or less the heart of quantum mechanics, and surely all you need to know about QM for this.

Now, with this clear, it's important to note that while virtual particles can be as off shell as they want (i.e., the amplitude contribution is still positive), they *like* being close to being on-shell, close to real particles, and in fact the amplitude from a virtual particle \\(p\\) with 4-momentum \\(P^\mu\\) is something like

$$ A_p \sim \frac{1}{P^2 - m^2} $$

(or at least that's true for bosons).

Seen as a function of \\(P^2\\), this amplitude has a singularity at \\(m^2\\), in fact it is a meromorphic function with a simple pole there. The quantum amplitude has a spike where the four-momentum of the virtual would-be-particle corresponds to that of a real particle. Again, normal modes of oscillation map to resonances! And to verify this is actually a standard type of resonance, we need to consider the observable response which is actually the probability. In the modulus squared close to the pole the spike will dominate over all other contributions and \\( \|A\|^2 \sim \|A_p\|^2 \\), and so sufficently close to the pole the probability will go like

$$ |A|^2 \sim \frac{1}{(P^2 - m^2)^2 } $$

which is a pure resonance profile exactly like the ones we introduced earlier.

Now, going back to the \\(ee \rightarrow \mu\mu\\) thing. This surely will include contributions from virtual histories where the electron-positron pair annihilates to produce a virtual particle which travels a bit in spacetime and then decomposes into a muon-antimuon pair. This sector of the amplitudes is called the **s-channel**, because the s variable introduced before is the \\(P^2\\) of the virtual particle, since by conservation of momentum \\(P = P_1 + P_2 \\). Thus, we expect that the amplitude for \\(ee \rightarrow \mu\mu \\) is (very roughly) a sum of the amplitudes of possible species of virtual particle in the s-channel, something **very schematically** like this

$$ A = \frac{\text{constant}_1}{s - m_1^2} + \frac{\text{constant}_2}{s - m_2^2} + \frac{\text{constant}_3}{s - m_3^2} + \ldots $$

and when \\(s\\) nears an \\(m_i\\), that amplitude becomes dominating and in a probability-vs-\\(s\\) plot you will observe a resonance peak. 

So real particles map to poles in the amplitude. In fact, the form of the amplitude I gave right now is most surely pretty wrong *except* for the poles; its behaviour away from them can be complicated and hard to control but the salient feature is that there is a simple pole at any particle mass, and so a resonance in the probability.

## Width and decay

Question: this explains \\( 1 / (s - m^2 ) \\) resonances, with no width \\( \Gamma \\), no smoothing, while the Z-resonance plot does display a not insignificant broadening. How does the resonance get smoothed into a Lorentzian? It comes from the fact that the corresponding real particle is unstable. If a particle decays with probability per unit time \\(\Gamma\\), then we also have to consider *higher-order* virtual processes where the virtual particle does decay and then recompose just in time to end up where we want to end up. This modifies the final amplitude; it does not delete the pole but moves it just a bit (by \\(-m\Gamma\\) to be precise) in the imaginary direction in the \\(s\\) plane. This means that we, living in our world of real quantities, will miss the pole and so we will not measure a singularity, but we will still feel its effect as a significant, but finite enhancement of the response. It's not hard to see you get a Lorentzian peak in this case, with width equal to \\(\Gamma\\) itself, though in this context it is better known as the [Breit-Wigner distribution](https://en.wikipedia.org/wiki/Relativistic_Breit%E2%80%93Wigner_distribution).

Anyway, let us ignore this higher-order effect for now, since it adds an unnecessary complication.

## Regge theory

Let's move to a completely different subject. Back in the day, people started discovering a lot of particles that interacted through the strong force, which we now call hadrons. They can be bosons, called mesons, or fermions, called baryons. There were a *lot* of them, and people were discovering them by the dozen. Apart from the nucleons, a couple of mesons, like the pions or long kaons for example, were relatively long-lived (because of approximate symmetries actually) but most of these are very unstable. They are discovered essentially only by noticing their corresponding resonances in plots of probabilities. It was uncomfortable to see nature had to offer so many new family members, it was hard to believe they were fundamental. Nowadays after a cursory look at the wiki page you could find yourself smiling at the naivety of these prehistoric physicists, who couldn't figure out hadrons were just bound states in a quantum field theory called Quantum Chromodynamics whose fundamental degrees of freedom are quarks and gluons - it looks really obvious a posteriori that the vast variety of hadrons are just composites of smaller particles in all various combinations.

I am going to try to argue here that this was **not obvious** at all. In fact, I would like to try to convince the reader that the physics strongly hinted in a completely different direction, that all of the people involved in this story are absolutely brilliant, and that the fact that ultimately QCD ended up being the correct solution was a shocking surprise.

It makes complete sense to start from what *they* had available. They found that hadrons could be classified by a bouquet of symmetries (exact and approximate) and the quantum numbers that these symmetries assigned to hadrons. But they also found that, fixing all quantum numbers except the mass and spin (mass and spin are quantum numbers for the Poincaré simmetry!) one found a sequence of *multiple* particles of increasing mass and spin, with the spin increasing by \\(1\\) each step. So for example, there is the standard \\(\rho\\) meson, spin 1, better called \\(\rho(770)\\) because the mass is about 770 MeV, and then you find an \\(a_2(1320)\\) meson, with spin 2, larger mass and all the same other quantum numbers as the \\(\rho\\), and then a spin-3 meson \\(\rho_3(1690)\\) and so on and so on. They were all arranged in such *trajectories*.

This very much looks like excitations of a quantum bound system, because it is. In quantum mechanics, almost always bound states have a discrete spectrum. The \\(\rho(770)\\) would be the lowest rung of the ladder (consistently with the constraint of the other quantum numbers). Giving it energy, you jump to the next rung, which is the \\(a_2(1320)\\), increasing both the spin and the internal energy (= mass). But being a bound state *in general* is not very useful, because it does not necessarily mean it's a bound state of point particles interacting through some force. Bound state could be literally anything, any kind of beast with a discrete energy spectrum. At the time, the fact that the would-be standard model was a local quantum field theory, so a theory of fundamental **point** particles, was unknown, and as I said, unexpected at least for the strong sector. QFT was very successful with electrodynamics but it struggled to explain the spectrum of hadrons; to understand why we need to bring out some numbers. Considering a hadron trajectory has two variables, the spin \\(J\\) and the mass-squared \\(M^2\\), it would be interesting to plot those together.

(plot)

The trajectories are linear! Actually *affine*, not linear, but experimentalists say linear if they see a line - they're a practical breed. These angular momentum - squared mass lines are called *Regge trajectories*. The fascinating thing is that the slope \\(\alpha'\\), aptly named Regge slope, is a universal constant for all mesons and baryons. Not only: there is always a primary, or mother trajectory with y-intercept \\(\alpha_0\\):

$$ J = \alpha_0 + \alpha' M^2 $$,

where \\(\alpha_0\\) is yet another universal constant, and the mother is accompained by a tower of "daughter" trajectories shifted by an integer:

$$ J = \alpha_0 + \alpha' M^2 - n$$


$$  n = 1,2,3,\ldots $$

The daughters are interesting, but let's concentrate on the mother which is already something magical. The equation \\( J = \alpha_0 + \alpha' M^2 \\) should be read as specifying the angular momentum as an analytic function \\(\alpha(M^2)\\) of the mass squared. Particles appear whenever J hits a non-negative integer, and the mass-squared at which you hit the integer is the mass-squared of the particle. Makes sense. 

What is unusual is that this function is a line. For example, if you take the case of a bound state of two particles interacting with a \\(1/r\\) potential, so essentially the hydrogen atom, you will find a tower of excited states, but the Regge trajectory will be something like \\( J = \alpha(M^2) = - 1 + \text{constant} (M - M_0)^{-1/2} \\). Yuck. In fact, no bound system known at the time could result in a linear Regge trajectory.

Why the hell are mesons arranged on these trajectories? Why are they universal? It barely makes sense. ...

## the Gamma amplitude

Physics is a palace.

QFTists believed the palace had to be built. So they began making plans for foundations that would have allowed the construction of an edifice that would reach up to where they wanted to go, which is to match with experiments.

The S-matricists believed the palace was already there, but needed to be explored. So they tried to break in from the last floor's window hoping to be able to make their way down from there. The window were linear Regge trajectories, and people hoped combining these with the understanding of particles as resonances would prove fruitful in investigating the microscopic structure of... whatever the strong sector was.

Take one mother Regge trajectory. Consider just bosons, so mesons. These are an infinite set of particles with spin \\( J = 0,1,2,3,...\\) and increasing mass \\( M_J^2 = (J-\alpha_0)/\alpha' \\), and also we ignore their decay. Smashing two particles together, the response should display a resonance for *each* of these values of \\(s = M_J^2\\). Thus the quantum amplitude for the process should have, as a function of \\(s\\) an infinite array of poles, at the values \\(s = M_J^2\\), right?

What famous meromorphic function has such an array of poles? Right off the bat you'd say something like \\( 1/\sin(\pi z) \\), but that doesn't work: it has poles at all integer values of \\(z\\), we just want non-negative. The solution is spoilt in the title and is of course the [Gamma function](https://en.wikipedia.org/wiki/Gamma_function). Gamma realizes an analytic generalization (with a few special properties) of the integer factorial:

$$ \Gamma(n) = (n-1)! $$

and extends the factorial's recursive relation to complex arguments:

$$ \Gamma(z+1) = z \Gamma(z)$$

Playing around with these two facts it is very easy to see Gamma is divergent only at the non-positive integers \\(z = 0, -1, -2, -3, \ldots\\). In fact, these are actually simple poles for the Gamma function, and the only poles (there is no sneaky magic going on off-real axis). So... what if we tried

$$ A(s) \sim \Gamma(-\alpha(s)) $$

That seems to do the trick: it has a pole whenever \\(\alpha(s)\\) strikes a non-negative integer, which means \\(s\\) struck the corresponding \\(M_J^2\\), which is the resonance of the spin-J particle of the Regge tower.


- Gamma amplitude
- Beta function
- duality
- string theory
