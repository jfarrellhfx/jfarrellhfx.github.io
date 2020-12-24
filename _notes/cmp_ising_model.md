---
subject: Condensed Matter Physics
title: Ising Model
order: 1
layout: note
excerpt_separator: <!--more-->
fontsize: 12pt
header-includes: |
    \usepackage[margin=1in]{geometry}
    \usepackage{physics}
    \renewcommand{\d}{\mathrm{d}}
    \usepackage{libertine}
    \usepackage[libertine]{newtxmath}
    \newcommand{\e}{\mathrm{e}}
---
<!--more-->


## Ising Model in *d* = 0
Let's consider a system with only two degrees of freedom, which we'll call $s_1$ and $s_2$.  They are *spins*, so they only take on the values $s = 1$ and $s = -1$.  To specify a system you just need to give values for $s_1$ and $s_2$.

Imagine the spins have magnetic moments of $\mu_B = 1$ (just so we don't have to put it in the formulas), and also imagine that there is a uniform magnetic field of magnitude $B$ along the same axis as the spins.  Then the energy has two parts --- an interaction between the two spins, and an interaction between each spin and the external field:

$$\begin{equation}
 E(s) = -J s_1 s_2 - B(s_1+s_2).
\end{equation}$$

It's useful to define some additional constants:

$$\begin{align}K = \beta J, \nonumber\\
h = \beta B.\nonumber
\end{align}$$

with $\beta= 1 / k_b T$ as usual.

To solve the problem, we'll need to work out the partition function, which will be:

$$\begin{align}
    Z &= \e ^ {-\beta E(s_1,s_2)} \nonumber\\
      &= \sum_{s_1,s_2} \e ^ {Ks_1s_2 + h (s_1 + s_2)}. \nonumber
\end{align}$$

In this case, the sums over $s_1$ and $s_2$ are just over two values , $s_1 = 1$ and $s_2 = -1$.  So we get:

$$\begin{equation}
    Z(K,h) = 2 \cosh(2 h) \e ^K + 2 \e^{-K}.
\end{equation}$$

To get a sense of the physics, we'll use the partition function to calculate some averages of quantities (I mean *thermal* averages).  For example, consider the (*spin*-averaged) magnetization, $M = (s_1 + s_2)/2$.  We take thermal average by working out:

$$\begin{align}
    \langle M \rangle &= \frac1Z \sum_{s_1,s_2} M \e^{-E(s)} \nonumber\\
    &= \frac1Z \sum_{s_1,s_2}\frac12 (s_1 + s_2)\e^{Ks_1s_2+h(s_1+s_2)} \nonumber
\end{align}$$