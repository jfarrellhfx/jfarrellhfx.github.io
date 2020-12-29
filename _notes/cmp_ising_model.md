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
    \usepackage{physics}
---
<!--more-->
The source for these notes is Chapter (2) of Shankar's Book *Quantum Field Theory for Condensed Matter Physics*.

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
    \langle M \rangle &= \frac1Z \sum_{s_1,s_2} M \e^{-E(s)}, \nonumber\\
    &= \frac1Z \sum_{s_1,s_2}\frac12 (s_1 + s_2)\e^{Ks_1s_2+h(s_1+s_2)}, \nonumber\\
    &= \frac12\frac1Z \pdv{Z}{h}, \nonumber\\
    &= \frac12 \frac1Z \pdv{\ln Z}{h}. \nonumber\\
\end{align}$$

Or, if we define free energy $F$ by:

$$\begin{equation}
  F(K,h) \equiv \e ^{- \beta F},
\end{equation}$$

then we can write:

$$\begin{equation}
    \langle M \rangle = \frac12 \pdv{}{h}\left( -\beta F \right).
\end{equation}$$

For us, $-\beta F = \ln \left( 2 \cosh(2 h)\e ^K + 2 \e ^{-K} \right)$, so we get:

$$\begin{equation}
    \langle M \rangle \frac{\sinh(2h)}{\cosh(2h) + \e^{-2K}}.
\end{equation}$$

If we wanted instead the *thermal* average of a *particular* spin (instead of the spin-average), we need to add a source term to the Boltzmann weight.  The idea is to couple each spin to its own magnetic field --- the source term is $h_1 s_1 + h_2 s_2$, and it gives the partition function:

$$\begin{equation}
\label{eq:source_terms}
 Z = \sum \e ^ {K s_1 s_2 + h_1 s_1 + h_2 s_2} \equiv \e^{-\beta F}.
\end{equation}$$

We can check that as $h \rightarrow \infty$ and $K \rightarrow \infty$, $\langle M \rangle \rightarrow 1$.  This makes sense, since in the limit of strong fields, the spins should be completely aligned.

### Correlators

Taking single spatial derivatives of the free energy in (\ref{eq:source_terms}) with respect to the $h_i$ is the same as taking a thermal average of the corresponding spin, because basically, the derivative just brings down a factor of $s_i$ from the exponential.  *e.g.*

$$\begin{equation}
    \langle s_1 \rangle = \frac{1}{Z} \sum_{s_11, s_2} s_1 \e ^ {K s_1 s_2 + h_1 s_1 + h_2 s_2} = \pdv{(-\beta F)}{h_1} = \pdv{\ln Z}{h_1}
\end{equation}$$

And, similarly, taking two mixed derivatives with respect to, say, $h_1$ and $h_2$ is *kind of*  like taking an average of the product $s_1 s_2$.  But it's not quite --- we actually get (using the product rule):
$$\begin{align}
    \pdv{^2}{h_1 \partial h_2}(-\beta F) &= \pdv{}{h_1} \left( \frac1Z \pdv{Z}{h_2} \right) \nonumber\\
                                         &= \frac1Z\pdv{^2}{h_1 \partial h_2} - \frac{1}{Z^2}\pdv{Z}{h_1} \pdv{Z}{h_2} \nonumber\\
                                         &= \langle s_1 s_2 \rangle - \langle s_1 \rangle \langle s_2 \rangle
\end{align}$$

This kind of thing comes up often, motivating a definition:


<div class = "definition"><b>Definition: Connected Correlation Function</b><br>
The <i>connected correlation function</i> $\langle s_1 s_2 \rangle_c$ is defined as:
$$\begin{equation}
 \langle s_1s_2 \rangle_c = \langle s_1 s_2 \rangle - \langle s_1 \rangle \langle s_2 \rangle
\end{equation}$$
</div>
