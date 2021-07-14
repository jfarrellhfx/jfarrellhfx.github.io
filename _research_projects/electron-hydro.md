---
title: Computational Electron Hydrodynamics
layout: page
order: 1
date: 2020-12-24
excerpt_separator: <!--more-->
---
- *Supervisors: Prof. Thomas Scaffidi & Prof. Nicolas Grisouard*
- *Supported by a NSERC Undergraduate Student Research Award*

In usual circumstances, collections of electrons moving in a solid do not experience hydrodynamic behaviour; any viscosity or convection is destroyed by strong scattering off of impurities in the crystal lattice or quantized lattice vibrations called "phonons".  Still, in  materials like graphene, the length scale associated with this "momentum relaxing" scattering can be made large enough that hydrodynamic behaviour persists, meaning that the electron gas can be described by the Navier-Stokes Equations.

I used a finite-volume method to simulate a viscous electron gas moving in one dimension in a field effect transistor.  With certain boundary conditions, this setup experiences an instability: small perturbations to the steady state grow and oscillate at a certain frequency.  Depending on the length of the channe, this frequency can reach the range of TeraHertz, a region of the electromagnetic spectrum for which no good sources or detectors currently exist.

<center>
<div class = "fig">
<video width = "100%" muted controls loop src="/research_projects/basic_animation.mp4">
</video>
</div>
</center>

<!--more-->
The above movie gives the density profile (left panel) and momentum density (right panel) plotted over the length of the channel
