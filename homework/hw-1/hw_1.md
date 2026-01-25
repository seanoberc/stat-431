---
title: Homework 1
author: Sean Oberc
date: 2026-01-21
geometry: margin-1in
---

$$
\begin{alignedat}{1}
MSE_{test} &= E\left[Y_0 - \hat{f}(x_0)\right]^2 \\
&= E\left[f(x_0) + \epsilon - \hat{f}(x)\right]^2 \\
&= E\left[E[\hat{f}(x_0)] - \hat{f}(x) - E[\hat{f}(x_0)] + f(x_0) + \epsilon\right]^2 \\
&= E\left[\left(E[\hat{f}(x_0)] - \hat{f}(x_0)\right) + \left(f(x_0) - E[\hat{f}(x_0)]\right) + \epsilon\right]^2 \\
&= E\left[\hat{f}(x_0) - E[\hat{f}(x_0)]\right]^2 + \left[f(x_0) - E[\hat{f}(x_0)]\right]^2 + E\left[\epsilon^2\right] \\
&= Var\left(\hat{f}(x_0)\right) \qquad + \qquad Bias^2\left(\hat{f}(x_0)\right) \qquad + \quad Var\left(\epsilon \right)
\end{alignedat}
$$

<!-- LaTeX code for Question 3. (a) -->
$$
x_0 = (0,0,0)
$$

$$
d_i = \sqrt{(x_{i1}-0)^2 + (x_{i2}-0)^2 + (x_{i3}-0)^2}
$$

$$
\begin{aligned}
d_1 &= \sqrt{0^2+3^2+0^2} = 3 \\
d_2 &= \sqrt{2^2+0^2+0^2} = 2 \\
d_3 &= \sqrt{0^2+1^2+3^2} = \sqrt{10} \\
d_4 &= \sqrt{0^2+1^2+2^2} = \sqrt{5} \\
d_5 &= \sqrt{(-1)^2+0^2+1^2} = \sqrt{2} \\
d_6 &= \sqrt{1^2+1^2+1^2} = \sqrt{3}
\end{aligned}
$$

**(b) Prediction for $K=1$:**

$$
\text{Nearest neighbor is Observation 5 (distance } \sqrt{2}\text{), whose class is Green.}
$$

$$
\hat{Y} = \text{Green}
$$

**(c) Prediction for $K=3$:**

$$
\text{Three nearest neighbors are Obs. 5 (Green), Obs. 6 (Red), Obs. 2 (Red).}
$$

$$
\hat{Y} = \text{Red}
$$

**(d) Choice of $K$:**

$$
\text{If the Bayes decision boundary is highly nonlinear, we expect the best } K \text{ to be small,}
$$

$$
\text{because smaller } K \text{ gives a more flexible classifier that can follow complex boundaries.}
$$
