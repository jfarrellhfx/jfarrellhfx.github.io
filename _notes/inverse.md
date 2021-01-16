---
title: Derivitive of Inverse Functions
subject: Calculus
show_excerpt: false
excerpt_separator: <!--more-->
layout: note
---
This note explains how to take the derivative of an inverse function.
## Statement:

Take a function $f$, and let $g = f^{-1}$.  Then we can compute its derivative using:

$$
\begin{gather*}
f(g(x)) = x\\
\implies \dv{}{x}f(g(x)) = 1\\
\implies f'(g(x))g'(x) = 1.
\end{gather*}
$$

So that, remembering $g=f^{-1}$, we get:

$$
\begin{equation}
\label{eq:inverse}
\boxed{g'(x) = \frac1{f\left(f^{-1}(x)\right)}.}
\end{equation}
$$

## An Example:

You can use Eq. ($\ref{eq:inverse}$) this to work out the derivatives of the inverse trigonometric functions.   As an example:
$$
\begin{align}
\dv{}{x}\arccos x &= \frac1{-\sin(\arccos(x))}, \nonumber\\
&= \frac{-1}{\sqrt{1-x^2}}.
\end{align}
$$
