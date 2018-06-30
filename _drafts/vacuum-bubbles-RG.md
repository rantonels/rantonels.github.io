---
layout: post
title: "Are vacuum bubbles renormalisation flows?"
---

Why not? In this paper

[**AdS Vacuum Bubbles, Holography and dual RG Flows**, Riccardo Antonelli, Ivano Basile (Pisa, Scuola Normale Superiore), Alessandro Bombini (INFN, Padua & Padua U.). Jun 6, 2018. 26 pp., arXiv:1806.02289 \[hep-th\]](https://arxiv.org/abs/1806.02289)

we've argued for this particular viewpoint. I'll try now to give an idea of the context and motivation behind our conjecture.

# A curious universe

Holography, or AdS/CFT specifically, is a strange and counterintuitive story, and most of it I think boils down to anti-de Sitter (AdS) spacetime being profoundly weird. To picture **life in AdS**, imagine first living in hyperbolic space, such as the one depicted in the Poincaré disk below:

{% include image.html name="hept.jpg" caption="I would have just shown Escher's *Circle limit III* if it wasn't for those meddling copyright laws. I made this picture, do what you want with it." %}

As you might know, while the boundary of hyperbolic space might be depicted at a finite distance from the centre, this is an illusion and the boundary is **infinitely far away** in terms of distances measured by a hyperbolic inhabitant. Hyperbolic space is infinite much like the normal Euclidean plane.

But AdS adds a twist, involving the time dimension too in the hyperbolic-ness[^1]. There is a **time dilation** between you at the centre and someone far away, and the sign of this time dilation is where the magic lies. 

Imagine standing at the center of the disk, and sending your friend to walk to the boundary at a constant speed. He, of course, walks and walks forever, as the distance is simply infinite, and he never sees the boundary get any closer.

But to you, things are a bit different. Because of the time dilation, you actually see your friend speed up the farther he is from you. In fact, you see him go faster and faster and live longer and longer stretches of his infinite life of straight travel to the boundary. In fact, in a finite time (measured by you) he actually *reaches* the boundary. Of course, he's lived infinite years then, but that's no big deal. He might decide to come back to you. So he does the same trip in reverse, slowing down, and reaches you in the same amount of finite time.

He can now tell you all about the boundary at infinity, and you had to wait for a relatively small time for this information.

This fact is deeply troubling, but it is a nearly unescapable consequence of the negative curvature of AdS, corresponding to its negative cosmological constant. It means essentially that the boundary of AdS, even though it is ``at infinity'', should be ascribed at least *some* physicality, as it is **able to interact** with the AdS, also known as the *bulk*.

This isn't how the story of AdS/CFT went, but one could argue that a posteriori that this peculiarity is an essential ingredient, maybe the whole point of the correspondence. The boundary can receive and send gravitational waves, so in some sense there is a dependence of physics in the bulk from *conditions on the boundary*, or... **boundary conditions**. 

The AdS/CFT correspondence states that there is a different theory, the infamous CFT, that lives on the boundary (so in one dimension less) and is related to the bulk in this weird way: the way the bulk reacts to boundary perturbations is mapped to the physics of the corresponding perturbation in the CFT. This constitutes the holographic dictionary, and the bulk and boundary are interpreted as translations of the same physics in different language.

# Zooming out

Quick question: is the standard model scale-invariant? Namely, does it look more or less the same if you "zoom out" a bit?

No. Why? Well, at the very least, with all the particles there are in it with their great variety of masses, each mass defines a characteristic length scale in the Compton wavelength:

$$\lambda_C = \frac{h}{mc}$$,

so certainly *something* has to be different if I zoom out but this distance stays the same. 

Indeed let's say we start from a very zoomed in (and so, high-energy) perspective, say, at the scale of hundreths of femtometres. When you look at it at these small sizes, the SM realises the so-called quark-gluon plasma, where these two classes of particles stream freely in a colourful soup.

As you zoom out - and so, inevitably, cool down - this situation begins morphing. The colour force begins getting stronger and the soup starts becoming inhomogeneous, thickening in some granules that turn into colourless lumps, getting smaller and tighter with the zooming. These are the hadrons. Zoom out further and most hadrons decay until you're left essentially with protons, neutrons and electrons/positrons, plus some photons bouncing around. The nucleons condense into nuclear matter and we have now a fluid of nuclei and electrons/positrons.

When we zoom past the electron compton wavelength, we lose the ability to create electron/positron pairs, and in fact all pairs that already exist start annihilating, and we are left only with the excess electrons. They are now "frozen": we cannot really change their number, make more or destroy them, though we can move them around and excite them. They create the electronic shells around nuclei, and we are left with neutral atoms.

Zoomed out to this point, we're only left with the shrinking neutral specks of mass that are atoms, and photons. About the atoms, are they *really* here? Meaning, are they truly degrees of *freedom*? Again we cannot really create or destroy them with our very low energy. We can excite them, or ionize them, but we're quickly losing the minimum energy to even do that. We can make them move, but soon the minimum energy in the quantum of sound, the phonon, flies past us too. There is no freedom left for us.

Except for photons. Photons continue to always exist, and they seem unaffected by the zooming - no matter how low the energy, you can always make one. At some point, nothing is discernible anymore but free electrodynamics. Nothing more will happen through zooming - we've reached a fixed point.

**This is renormalisation.** [^2] It's just zooming out. You start from a very zoomed in perspective, called the ultraviolet (UV), you slowly zoom out and observe the theory morphing (that's the renormalisation group, or RG flow), and finally when you zoom infinitely far you reach the infrared (IR).

Under RG, the standard model flows in the IR into free (i.e., no charges) electrodynamics. This theory is a fixed point of the zooming out because it is scale-invariant - it looks like itself at all scales. It is therefore an (extremely trivial) example of a **conformal field theory**, or CFT.

It's the case in the vast majority of cases that most theories or systems, no matter how complicated or alien, will flow to some CFT in the IR. (To be fair, most of the times the CFT is empty, but that still counts).

[^1]: I can't say *hyperbolicity* because that's a completely different thing which in the following paragraphs I show to be false for AdS, precisely because of the hyperbolic*ness* of the geometry. Language doesn't help here.

[^2]: if I hear that crap about hiding infinities under the carpet I will **gut you like a fish**.
