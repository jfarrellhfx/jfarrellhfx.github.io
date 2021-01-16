---
layout: post
title: "Math on the Web"
tag: Computer Stuff
excerpt_separator: <!--more-->
---
To be able to type $\LaTeX$ equations in websites, you need to add a few lines of `html` to the heading of your page.  I use the configuration given below.

First, tell your webpage where to find `MathJax`:
```html
<script type="text/javascript" id="MathJax-script" async
  src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js">
</script>
```

<!--more-->

But, *before that* (which is important), we need to configure it.  I like it to be able to use symbols and environments from `amsmath`, so I include the tag `tags: ams`. Additionally, one drawback of writing $\LaTeX$ on the web like this is that `MathJax` doesn't understand that many packages; many convenient macros from packages like `physics` are not accessible.  Still, we can partially fix it by defining our own macros --- and I was surprised how few I really used regularly.
```html
<script>
MathJax = {
  tex: {
    inlineMath: [['$', '$'], ['\\(', '\\)']],
    displayMath: [ ['$$','$$'], ['\[','\]'] ],
    tags: 'ams',
    macros: {
        d: '{\\mathrm{d}}',
        pdv: ['{\\frac{\\partial #1}{\\partial #2}}', 2],
        vbi: ["\\boldsymbol{#1}", 1],
        vb: ["\\mathbf{#1}", 1],
        vu: ["\\hat{\\mathbf{#1}}", 1],
        vui: ["\\hat{\\boldsymbol{#1}}", 1],
        e: "{\\mathrm{e}}",
        i: "{\\mathrm{i}}",
        dv: ["{\\frac{d #1}{d #2}}", 2],
    },
  },
  svg: {
    fontCache: 'global'
  }
};
</script>
```

e.g.   To get a numbered equation, I write:
```html
$$
 \begin{equation}
 \left( \i \gamma^\mu \partial_\mu - m \right) \psi = 0.
 \end{equation}
$$
```
which renders as:

$$
 \begin{equation}
 \left( \i \gamma^\mu \partial_\mu - m \right) \psi = 0.
 \end{equation}
$$

Note that `html` wants the `$$ $$` around the `\begin{equation} ... \end{equation}`--- it needs to know you're trying to type $\LaTeX$.
