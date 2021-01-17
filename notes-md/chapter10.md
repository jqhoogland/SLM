# Chapter 10
## One-Dimensional Maps

------------------------------------------------------------

## 10.0 Introduction

New class of systems with **discrete** time

Known as:
- Difference equations
- Recursion relations
- Iterated maps
- simply **maps**

**Orbit** of a point, $x_0$: the sequence of numbers determined from
starting at $x_0$ and iterating the application of the one-dimensional
map.

How do maps arise?
1. Tools for studying differential equations (e.g. Poincare and Lorenz
   map)
2. Models of natural phenomenon (e.g. certain cases of digital
   electronics, economics, non-overlapping generations in ecology)
3. Simple examples of chaos (maps capable of much wilder behavior).

Maps are easier to simulate on computers.

------------------------------------------------------------

## 10.1 Fixed Points and Cobwebs

Does point refer to $f: x_{n+1}=f(x_n)$ or to the difference equation
($x_{n+1}=bf(x_n)$) in its entirety?
- We'll use it for both

#### Fixed points and Linear Stability

This is the same as what we already did for the Lorenz map.
**Stable** means the absolute value of eigenvalues, $|\lambda|$ of the linearized map
are $|\lambda|<1$.
**Marginal**: $|\lambda|=1$
**Unstable**:  $|\lambda|>1$

**Superstable**: fixed points with multiplier $\lambda=0$,
- perturbations decay like $\eta_n\sim\eta_0^{(2^n)}$, faster than
  normal algebraic behavior

#### Cobwebs
1. Start at point $x_0$.
2. Go up until intersecting $x_{n+1}=f(x)$
3. Go to the right until intersection $x_{n+1}=x_n$
4. Repeat 2 and 3 until convergence or divergence.

Example of $x_{n+1}=\sin(x_n)$ (with globally stable point $x=0$.
Example of $x_{n+1}=\cos(x_n)$ (with globally stable point
$x=0.739...$ (transcendental).

Contrast $\lambda < 0$and $0< \lambda > 1$:
- $\lambda<0$: convergence through damped oscillations (e.g. $\cos$
  example above).
- $0<\lambda 1$: convergence monotonically

------------------------------------------------------------

## 10.2 Logistic Map: Numerics

Robert May's plea for difference equations in elementary mathematical
courses.

Example of the **logistic map**

**x_{n+1}=rx(1-x)**

Bounds:
- $0<r<4$
- $0<x<1$

$r<1$: extinction
$r=1$: transcritical bifurcation
$1<r<3$: steady state at $1-\frac{1}{r}$
$r=3$: flip bifurcation (associated with period doubling)
$3<r<r_c=3.569946...$: period-doubling region
$r_c<r<4$: chaos! with islands of stability

------------------------------------------------------------

## 10.3 Logistic Map: Analysis

Find and analyze the stability of fixed points for $0<r<3$

Comment on transcritical bifurcation

Comment on flip bifurcation: In graphical approach we see that the
slope of $f$ at the point intersecting the diagonal becomes $-1$ at
$r=3$.

Find and analyze the stability of **second-iterate map** for
$3<r<1+\sqrt{6}$.

------------------------------------------------------------

## 10.4 Periodic Windows

How does a $3$-cycle emerge out of the chaos?

Just figure out $f^3$ like we did $f^2$ for the second-iterate map.

This is an $8$th order polynomial. Within the island of stability:
- $2$ trivial solutions at $x=0,1$.
- $3$ unstable solutions.
- $3$ stable solutions.


As we increase $r$, the stable and unstable period-3 cycles annihilate
when they are *tangent* to the diagonal, hence **tangent bifurcation**
(at $r=1+\sqrt{8}$, much harder to show this than for the 2-period!).

#### (Type-I) Intermittency

This is just a saddle-node bifurcation with another name, so right
below the period-3 window we see the **ghost** of the 3-cycle: nearly
3-period series interspersed with chaos.

This is a common feature inin systems where the transition from
periodic to chaotic behavior follows a saddle-node bifurcation of
cycles.

**Intermittency route to chaos**: time between bursts of chaos is
statistically distributed (like a random variable although this is
totally deterministic). As we move away from the period, the bursts
become more and more chaotic until they destroy all order.

#### Period-Doubling in the Window

At the end of the $3$-cycle, just like the $2$ cycle we get a period
doubling route to chaos, this time covering all orbits of period
$3\cdot 2^n$.

This kind of cascade occurs for *all* periodic windows!

------------------------------------------------------------

## 10.5 Lyapunov Exponent

We have not yet formally shown that this behavior is chaotic
(i.e. sensitive dependence on initial conditions).

Derivation of Lyapunov exponents for difference equations.

We want to get positive $\lambda: |\delta_n| = |\delta_0|e^{n\lambda}$
i.e. $\lambda = \frac{1}{n} \ln \frac{|\delta_n|}{|\delta_0|}$

Knowing that $\delta_n = f^n (x_0+\delta_0)-f^n(x_0)$
$\lambda = \frac{1}{n} \ln |\frac{f^n
(x_0+\delta_0)-f^n(x_0)}{\delta_0}|$,
and taking the limit $\delta_0 \rightarrow 0$, we get:
$$\lambda = \frac{1}{n}\ln |(f^n)'(x_0)|$$

Using the chain rule: $(f^n)'(x_0)=\prod_{i=0}^{n-1} f'(x_i)$ (recall
that $x_i = f^i(x_0)$), we get:

$$\lambda = \frac{1}{n}\sum_{i=0}^{n-1} \ln |f'(x_i)|$$

We **define** the Lyapunov exponent as:

$$\lambda \equiv
\lim_{n\rightarrow\infty}\left{\frac{1}{n}\sum_{i=0}^{n-1} \ln
|f'(x_i)|\right}$$

Note: this depends on the initial point $x_0$, though it will be the
same for all points in a given basin of attraction.

2 Examples where $\lambda$ can be determined analytically.
- Presence of stable $p-cycle$; superstable fixed point
- **Tent map**

Example of numerically determining $\lambda$ for the logistic map.

------------------------------------------------------------

## 10.6 Universality and Experiments

Consider the **sine map**. This has the exact same qualitative
behavior as the logistic equation (look at the bifurcation diagram).

Quantitatively, it is slightly different (e.g. period-doubling begins
later with thinner windows).

#### Qualitative Universality: The U-sequence

Result by Metropolis et al.

For unimodal maps, the ordering of periodic attractors is always the
same.

#### Quantitative Universality

Result by Feigenbaum

The Feigenbaum constant is universal: the ratio of the distance
between successive period-doublings.

$$\delta = \lim_{n\rightarrow\infty}\frac{r_n-r_{n-1}}{r_{n+1}-r_n} =
4.669\dots$

This is a new mathematical constant.

Different universal scaling in vertical direction on bifurcation
diagram (the $x$ direction).

Look at figure 10.6.3

Real-life experimental confirmation! (rolling convection tubes)

#### What does any of this mean physically?

Example of the **Rossler system**: 3 differential equations with only
one non-linearity that undergoes a period-doubling bifurcation of
cycles.

If we produce a Lorenz map, the system falls very nearly on a 1-d
curve, you guessed it, that is unimodal.

**Generally**: If a system's Lorenz map is nearly 1-D and unimodal,
Feigenbaum's universality theory applies.

This means we still have a long ways to go with systems whose strange
attractors are far from 2-dimensional.

------------------------------------------------------------

## 10.7 Renormalization

#### Notation
- $f(x,r)$ is a unimodal map undergoing period-doubling route to chaos
  as $r$ increases
- $x_m$ is the maximum of $f$
- $r_n$ is the value of $r$ at which $2^n$-cycle is born.
- $R_n$ is the value of $r$ at which $2^n$-cycle is superstable.

First, example of superstable cycles.

Superstable cycle of unimodal maps always contains $x_m$ as one of its
points.

Graphical procedure to location $R_n$
1. Draw horizontal line at heigh $x_m$
2. $R-n$ is where line intersects **figtree** portion of orbit diagram

Spacing between successive $R_n$ also scales with the Feigenbaum
constant.

Look at graphs $f(x, R_0)$ and $f^2(x, R_1)$. $x_m$ is a superstable
point of both! Look at a small box around $x_m$ in the second map, and
rescale to get self-similar graph.

Renormalization of $f$:
$$f(x,R_0)\approx \alpha f^2\left(\frac{x}{\alpha}, R_1\right).$$

After $n$ times:
$$f(x,R_0)\approx \alpha^n f^{(2^n)}\left(\frac{x}{\alpha^n},
R_n\right).$$

Feigenbaum showed:
$$\lim_{n\rightarrow \infty}f(x,R_0)\approx \alpha^n
f^{(2^n)}\left(\frac{x}{\alpha^n}, R_n\right) = g_0(x),$$

where $g_0$ is a **universal function** with a superstable fixed
point.

This requires $\alpha$ to be chosen appropriately (it is the vertical
scaling constant on the bifurcation diagram).

**Univeral**: $g$ is (almost) independent  of $f$, depends only on the
order of $f$'s maximum. Quadratic is generic, but you could have other
cases.

We can get other universal functions $g_i$ by starting with $R_i$
instead of $R_0$.

Using $R_\infty$, we get:
$$g(x)\equiv g_\infty(x)=\alpha g^2\left(\frac{x}{\alpha}\right),$$
since we  don't have to shift when we renormalize.

This is a **functional equation** for $g(x)$. This is self-referential
and will require boundary conditions on $g$.

Shifting the origin, we require maximum at origin:
$g'(0)=0$. Choosing, for convenience, $g(0)=1$.

We get: $\alpha = 1/g(1)$

No closed form solution for $g$ so we use power series instead.

#### Renormalization for Pedestrians

Pedagogical demonstration of RG.

$f(x,\mu)$ is unimodal map with period-doubling route to chaos
$(x,\mu)=(0,0)$: start of period-2 cycle.

We expand near the origin: $x_{n+1}=-(1+\mu)x_n+ax_n^2+\dots$, and
ignore higher order terms.

Rescale to eliminate $a$ $x\rightarrow x/a$.

$\mu>0$: period-2 points, $p$, $q$
Increasing $\mu$: at some point both points will period-double.
- Dynamics near point $p$ will be approximated by same algebraic form
  as above. We calculate the map $f^2$ and renormalize it to look like
  the above.

Step 1: find $p$ and $q$:
$$p=-(1+\mu)q+q^2$$
$$q=-(1+\mu)p+p^2$$

Combining:
$$p=\frac{\mu+\sqrt{\mu^2+4\mu}}{2}$$
$$q=\frac{\mu-\sqrt{\mu^2+4\mu}}{2}$$

Shift origin to $p$

Expand $p+\eta_{n+1}=f^2(p+\eta_n)$ for small $\eta_n$:

$$\eta_{n+1}=(1-4\mu-\mu^2)\mu_n+C\eta_n^2+\dots,$$
where
$$C= 4\mu + \mu^2-3\sqrt{\mu^2+4\mu}.$$

This has the same algebraic form as our original map.
We now rescale $\eta$ by defining a new $\mu$.

Choose $\~ x_n = C \eta_n$ and $\~\mu :-(1+\~\mu)=(1-4\mu-\mu^2)$:
$$\~x_{n+1}=-(1+\~\mu)\~x_n + \~x_n^2

Therefore: $\~\mu=\mu^2+4\mu-2$.

You get a series of renormalization transformations for $\mu_k$:
$$\mu_{k-1}=\mu_k^2+4\mu-2$$
or
$\mu_k=-2+\sqrt{6+\mu_{k-1}}$

Now we can apply our standard machinery for 1D maps to determine fixed
points.

$$\mu^2+3\mu-2=0$$
$$\mu=\frac{1}{2}(-3+\sqrt{17})$

To get the Feigenbaum constant(s), consider:
$\delta\approx \frac{\mu_{k-1}-\mu^*}{\mu_k-\mu^*}$

Taking the limit $k\rightarrow \infty$, and applying L'Hopitals rule:
$\delta = 2\mu^*+4$

Here $C$ plays the role of $\alpha$
