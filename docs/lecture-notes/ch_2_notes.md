---
layout: default
title: Chapter 2
---

$\int_0^1 x^2\,dx = \frac{1}{3}$

### Relationship between $Y$ and $X = (x_1, x_2, \cdots, x_p)$:
- $\hat{y} = (x'x)^{-1} \cdot x'y$

$$
\begin{aligned}
MSE_{test} &= E\left[Y_0 - \hat{f}(x_0)\right]^2 \\
&= E\left[f(x_0) + \varepsilon - \hat{f}(x)\right]^2 \\
&= E\left[E[\hat{f}(x_0)] - \hat{f}(x) - E[\hat{f}(x_0)] + f(x_0) + \varepsilon\right]^2 \\
&= E\left[\left(E[\hat{f}(x_0)] - \hat{f}(x_0)\right) + \left(f(x_0) - E[\hat{f}(x_0)]\right) + \varepsilon\right]^2 \\
&= E\left[\hat{f}(x_0) - E[\hat{f}(x_0)]\right]^2 + \left[f(x_0) - E[\hat{f}(x_0)]\right]^2 + E\left[\varepsilon^2\right] \\
&= Var(\hat{f}(x_0)) \quad + \quad Bias^2(\hat{f}(x_0)) \quad + \quad Var(\varepsilon))
\end{aligned}
$$
