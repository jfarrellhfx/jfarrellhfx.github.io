---
title: Computational Electron Hydrodynamics
layout: page
order: 1
date: 2020-12-24
excerpt_separator: <!--more-->
---
- **Supervisors:** *[Prof. Thomas Scaffidi](https://sites.google.com/view/thomasscaffidi/home) & [Prof. Nicolas Grisouard](https://sites.physics.utoronto.ca/nicolasgrisouard)*
- *Supported by an NSERC Undergraduate Student Research Award*

In usual circumstances, collections of electrons moving in a solid do not experience hydrodynamic behaviour; any viscosity or convection is destroyed by strong scattering off of impurities in the crystal lattice or quantized lattice vibrations called "phonons".  Still, in  materials like graphene, the length scale associated with this "momentum relaxing" scattering can be made large enough that hydrodynamic behaviour persists, meaning that the electron gas can be described by the Navier-Stokes Equations.

For [*Farrell, Grisouard, Scaffidi (2021)*](http://arxiv.org/abs/2112.07683), I used a finite-volume method to simulate a viscous electron gas moving in one dimension in a field effect transistor.  With certain boundary conditions, this setup experiences an instability: small perturbations to the steady state grow and oscillate at a certain frequency.  Depending on the length of the channel, this frequency can reach the range of TeraHertz, a region of the electromagnetic spectrum for which few good sources or detectors currently exist.


<div style="margin-top:10px;margin-bottom:10px">
<center>
<video width = "75%" muted autoplay loop src="/research_projects/out.webm">
</video>
</center>
</div>


<!--more-->
The above movie gives the density profile (left panel) and momentum density (right panel) plotted over the length of the channel
