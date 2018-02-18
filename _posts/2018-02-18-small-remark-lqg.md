---
layout: post
title: "A small remark on Loop Quantum Gravity."
date: 2018-02-18
---

I just want to make this post as quick as possible. There is something that I believe anyone should see, perhaps even if you aren't interested in quantum gravity at all. First of all, because it's an unintentionally limpid lesson on a foundational point in theoretical physics, and also because it's tragically hilarious.

So, [as everybody knows](http://rantonels.github.io/a-geometric-proof-of-hawking-radiation-through-imaginary-time/), black holes emit radiation at a temperature

$$ T_H = 1/(8\pi G M)\,.$$

To reduce this to minimum complexity I'm going to use natural units ($$ c = \hbar = k_B = 1$$). So, this is the famous result of Hawking. The beauty of it is that it is part of semiclassical gravity, an intermediate step between classical and quantum gravity that doesn't face the daunting challenges of the latter. In some sense, semiclassical gravity stops exactly one step earlier than where the infamous nonrenormalizability of gravity appears and makes the whole thing unpredictive. What this means is that it is **true no matter what**, independently on your preferred choice of completion into a full theory of quantum gravity.

Which means semiclassical predictions are an important check for a candidate theory: if you fail to reproduce them, go home.

More interesting than temperature is entropy. Identifying internal energy and black hole mass, the first law of thermodynamics gives the following entropy for a black hole:

$$ S_{BH} = \frac{A}{4G} \,.$$

The BH stands both for Bekenstein-Hawking and for Black Hole, an extraordinary coincidence. On the right hand side is the **event horizon area**. So, let me pedantically break this down into *two* distinct statements:

- The entropy of a black hole is proportional to its event horizon area.
- The proportionality factor is [one nat](https://en.wikipedia.org/wiki/Nat_(unit)) per four Planck areas.

Now this is not completely exact, since it's only semiclassical and not fully quantum-gravitational. But it's incredibly close to true for even moderately large black holes, because the first subleading correction is logarithmic - basically you have something like this

$$ S_\text{true} = S_{BH} + \text{const} \cdot \log S_{BH} + \ldots \,,$$

so the error in the semiclassical approximation is very small. The small subleading correction are very interesting for quantum gravitists, and subject of considerable controversy in string theory, but if you can get your theory to spit out the first term correctly, you're already in a very good place.

The above is what you would call a macroscopic calculation of the entropy. A microscopic count would start from a complete description of the black hole as a mechanical system of a very large number of "components" and recompute these thermodynamic quantities from scratch. The leading part of the entropy **must match** with the BH macroscopic count.

Ok. Now that this is clarified, let's see what **Loop Quantum Gravity** does with all of this. We follow Rovelli's [own (text?)book](https://www.amazon.com/dp/B00AKE1R5I/) on the matter. Attesting the humility of the endeavour, the book is simply titled *Quantum Gravity*. I prefer to use this review book as reference instead of the original papers because papers can be wrong or reflect an incomplete or in-progress understanding. A book celebrates results in your field you are supposedly proud of, strips them of all the hardship and confusion that were necessary to get there, and presents them clearly so that the reader can appreciate them as self-contained products.

So if you grab a copy of the book, and scan the contents, it actually looks like an amazing read. There is a lot of pages dedicated to conceptual issues in classical gravitation, a good deal of philosophical remarks on how quantum gravity should be approached, a review of Hamiltonian GR, and then the actual mathematics of LQG starts. LQG actually has a very challenging structure and in full honesty I barely understand a tiny speck of it. But don't worry, because **it doesn't matter**. Check this out:

Go to the section *Derivation of the Bekenstein-Hawking entropy*. Also visit the surrounding pages for added hilarity, but that's optional. Here's a translation of the actual derivation:

- Our quantum state of the geometry at some time is some "s-knot" object. It has subcomponents such as edges and vertices. You can also add handles and buttons and coffee pots, it works exactly the same. It doesn't actually matter at all what the s-knot is.
- The number of intersection of vertices/edges/anything with the horizon is proportional to the area of the horizon.
- Only those components that intersect the horizon matter for the count of the entropy, for some unknown reason. This breaks the equivalence principle and background-independence that we spent two hundred and forty pages explaining and defending.
- The entropy of the BH is the sum of the entropies of the intersecting components, so it's proportional to the area of the horizon.
- As for the actual value, this is apparently just a bunch of spins and after some calculation we get

$$ S_{BH} = \frac{1}{\gamma} \frac{\log 2}{4\pi \sqrt 3} A $$

and $$\gamma$$ is a number known as the Barbero-Immirzi parameter. We don't know what it is, but if we set it to $$\gamma = \frac{\log 2}{\pi \sqrt{3}}$$ we recover the BH entropy.

Let me repeat this even more succintly, hopefully not insulting anyone's intelligence. You need to prove that X is proportional to Y, and that X/Y = this value. You assume that X is proportional to Y, and then find that X/Y = some number, and set some number = that value.

This constitutes the entirety of all quantitative results in Loop Quantum Gravity.
