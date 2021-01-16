---
subject: Condensed Matter Physics
title: Quantum Theory of the Harmonic Solid
order: 1
date: 2020-01-03
layout: note
excerpt_separator: <!--more-->
fontsize: 12pt
header-includes: |
    \usepackage[margin=1in]{geometry}
    \usepackage{physics}
    \renewcommand{\d}{\mathrm{d}}
    \usepackage{libertine}
    \usepackage[libertine]{newtxmath}
---
<!--more-->
## Classical Theory of the Harmonic Crystal
Before we deal with the quantum case, it is a good idea to understand the theory of the harmonic crystal at a classical level.  The main idea is that we are going to suppose we have a crystal in its *equilibrium state* --- that means there is no net force on any of the ions.  We can write the potential energy of the lattice as:

## The Thing

Take a function $f$, and let $g = f^{-1}$.  Then we can compute its derivative using:
$$
f(g(x)) = x \\
\implies \dv{}{x}f(g(x)) = 1\\
\implies f'(g(x))g'(x) = 1
$$
So that, remembering $g=f^{-1}$, we get:
$$
\begin{equation}
\label{eq:inverse}
\boxed{g'(x) = \frac1{f\left(f^{-1}(x)\right)}.}
\end{equation}
$$

## An Example

You can use Eq. ($\ref{eq:inverse}$) this to work out the derivatives of the inverse trigonometric functions.   As an example:
$$
\begin{align}
\dv{}{x}\arccos x &= \frac1{-\sin(\arccos(x))}, \nonumber\\
&= \frac{-1}{\sqrt{1-x^2}}.
\end{align}
$$
