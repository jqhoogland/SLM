# Chapter 8
## Bifurcations Revisited

------------------------------------------------------------

## 8.0 Introduction

| 1D                                                                 | 2D                                                                     |
| ---                                                                | ---                                                                    |
| Fixed points                                                       | Fixed points; Orbits; Limit cycles; Centers; etc.                      |
| Bifurcations create, destroy or exchange stability of fixed points | Bifurcations create, destroy or exchange stability of any of the above |

------------------------------------------------------------

## 8.1 Saddle-Node, Transcritical, and Pitchfork Bifurcations

Not different from the 1D case - all the action happens in a one-dimensional subspace.

#### Normal Forms
| Saddle-node             | $ \dot x = \mu - x^2,\quad \dot y = -y $ |
| Transcritical           | $ \dot x = \mu x - x^2,\quad \dot y = -y $ |
| Supercritical Pitchfork | $ \dot x = \mu x - x^3,\quad \dot y = -y $ |
| Subcritical Pitchfork   | $ \dot x = \mu x + x^3,\quad \dot y = -y $ |

$-y$ so the other dimension is attractive
Recall "ghost" effects and critical slowing-down.

Example of biochemical switch of gene regulating pathway (saddle-node).
Example of supercritical pitchfork bifurcation

These are examples of **zero-eigenvalue bifurcations**. The
bifurcation occurs when the eigenvalue (of the Jacobian) goes
through the origin.

------------------------------------------------------------

## 8.2 Hopf Bifurcations

Now, we have two eigenvalues with an imaginary component (spirals), that go
through $Re \lambda = 0$ at the same time.

| Supercritical Hopf Bifurcation | Stable spiral becomes unstable spiral surrounded by small, nearly elliptical limit cycle.<br/>The limit cycle grows continuously from zero.                                                        |
| Subcritical Hopf Bifurcation   | Stable spiral becomes unstable spiral surrounded by small, nearly elliptical limit cycle.<br/>Trajectories jump discontinously to distant attractor at bifurcation.</br>Can exhibit **Hysteresis** |
| Degenerate Hopf Bifurcation    | Not a proper Hopf bifurcation. Stable spiral to unstable spiral but **NO** limit cycles. <br/>At bifurcation, we have a center, non-isolated closed orbits.<br/>Example nonconservative system becomes conservative |

It's hard to tell which case you have. Usually, you'll have to use
some numerical techniques.

Example of system which turns out to be subcritical (by process of elimination).

------------------------------------------------------------

## 8.3 Oscillating Chemical Reactions

Example of Hopf Bifurcations in **chemical oscillators**.

Example of using Poincare-Bendixson theorem with bifurcation added.

------------------------------------------------------------

## 8.4 Global Bifurcations of Cycles

Next to Hopf Bifurcation, **3 other ways to create or destroy limit
cycles**.

How are they qualitatively different?
- Harder to detect because they involve large regions of the phase
  plane, not just the neighborhood of a fixed point.

Hence => **Global Bifurcations**

#### Saddle-node Bifurcation of Cycles (or Fold)

Direction 1: half-stable cycle born out of nowhere (not close to
origin) that splits into a stable and unstable limit cycle.
Direction 2: An unstable and stable limit cycle annihilate.

Origin stays stable throughout and does not participate.

Example)
- Treat the radial component as a 1D system in isolation, and look for
  saddle-node bifurcation of fixed points.

#### Infinite-Period Bifurcation

Fixed point appears on the limit cycle (i.e. "infinite period")

#### Homoclinic Bifurcation (or saddle-loop)
Limit cycle approaches saddle point. At bifurcation, cycle touches the
saddle point and becomes a homoclinic orbit. Another kind of
infinite-period bifurcation.

#### Scaling Laws
For **Amplitude** and **Period** of the limit cycle as the bifurcation
is approached.

|                                   | Amplitude      | Period                                 |
| Supercritical Hopf                | $O(\mu^{1/2})$ | $O(1)$                                 |
| Saddle-node bifurcation of cycles | $O(1)$         | $O(1)$                                 |
| Infinite-period                   | $O(1)$         | $O(\mu^{-1/2})$                        |
| Homoclinic Bifurcation            | $O(1)$         | $O(\ln \mu)$ this is the only new one. |

Example of van der Pol oscillator having a degeneracy. By scaling $x$
you can show this to be a Hopf bifurcation.

What happens in higher dimensions?
- Many more kinds of bifurcations of limit cycles become
  possible. This table is no longer exhaustive.
  Homoclinic bifurcations become harder to analyze and often leave
  chatoic dynamics in its aftermath.

Why care about these scaling laws?
- These are experimentally measurable properties which allow you to
  judge the validity of different models.

------------------------------------------------------------

## 8.5 Hysteresis in the Driven Pendulum and Josephson Junction

Example of problem with both homoclinic and infinite-period
bifurcations. This is the weakly-damped harmonic oscillator with a
limit cycle with bistability: looping over the top or rest state.

Phrased in terms of Josephson junction.

Takeaways: proof of existence and uniqueness of limit cycle in certain region
using tricks from Poincare.

Topological argumentation: librations and rotations are the homotopy
classes on the cylinder

------------------------------------------------------------

## 8.6 Coupled Oscillators and Quasiperiodicity

#### New phase space: Torus!
We've looked at the plane and the cylinder.
Consider also the **torus**.

This is the phase space for systems with two variables that are both
periodic.

#### Coupled Systems
Uncoupled oscillators ($\dot \theta_1 = \omega_1; \dot \theta_2 = \omega_2$)
- Rational slope (ratio of the two frequencies): All trajectories are
  closed orbits on the torus
  - Example $3/2$ ratio gives the **trefoil knot**
  - For $p/q$ ratio: the result forms a **p:q torus knot**.
- Irrational slope: **quasiperiodic flow**
  - trajectories wind around endlessly
  - **This is a new type of long-term behavior that can only appear on
    the torus**

#### Coupled System
Look at the phase difference.

Example where the trajectories approach a stable fixed point,
**phase-locked** solution where oscillators are separated by constant
phase at a constant, **compromise frequency** (not necessarily halfway
between the frequencies but related to the coupling strengths).

Bifurcations:
- We have a stable and unstable locked solution that can annihilate in
  a saddle-node bifurcation
- When these annihilate, we have the periodic or quasiperodic
  solutions of the uncoupled case, but not the lines are not
  necessarily straight.

------------------------------------------------------------

## 8.7 Poincare Maps

Section 8.5 used a Poincare map to prove existence of a periodic
orbit. Let's discuss them more generally.

When are poincare maps useful?
- For studying swirling flows (e.g. near periodic orbit or in some
  chaotic system)

Consider:
- n$-dimensional system $\dot \boldsymbol x = \boldsymbol
  f(\boldsymbol x)$

Let $S = n-1$ dimensional surface of section (transverse to flow)

def. **Poincare map** $P$:
- A mapping from $S$ to itself. Follow the trajectories from one
  intersection with $S$ to the next.

Let $\boldsymbol x_k$ denote the $k$-th intersection.
Then, $\boldsymbol x_{k+1}=P(\boldsymbol x_k)$

If there is a  fixed point $\boldsymbol x^*: P(\boldsymbol x^*)=\boldsymbol
x^*$, then trajectories going through $\boldsymbol x^*$ are closed
orbits

Poincare map converts questions of closed orbits to questions of fixed
points, easier in principle, though it's often impossible to determine
a formula for $P$.

Example of system where $P$ *is* exactly determinable.

Use of **cobweb construction** to find fixed points of iterated
(discrete) map.

Example of time-dependent system (i.e. introduce other variable to
make it time-independent).

#### Linear Stability of Periodic Orbits
No surprises: questions about stability of closed orbits become
questions about stability of fixed points of the Poincare map

We look at the linearized Poincare map.

Recall that this is a discrete map, so the stability/instability thing
is a little different. We care about the absolute value of the
eigenvalues being larger or smaller than $1$.

Eigenvalues may equal $1$,l at for example a bifurcation of periodic
orbits which will require non-linear stability analysis.

**Characteristic** or **Floquet multipliers**  of periodic orbit: the
eigenvalues of the linearized Poincare map.

We don't generally care about the trivial multiplier along the
direction of periodic orbit.
