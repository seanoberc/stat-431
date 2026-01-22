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

