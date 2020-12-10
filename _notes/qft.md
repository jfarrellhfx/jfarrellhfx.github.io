---
subject: Quantum Field Theory
title: Typesetting Slash Notation
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

---
<!--more-->


Right now, I am just testing by ability to typeset math nicely and do it all from markdown!  Here is a numbered equation:

$$\begin{equation}
    \int_a^bf(x) \d^2 x = \oint \d x.
\end{equation}$$

And here is a not numbered equation!

$$
\nabla^2f(x,y,z) = \pdv{}{x}f+\pdv{}{y}f + \pdv{}{z}f.
$$
