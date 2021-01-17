# Chapter 6
## Phase Plane

------------------------------------------------------------

## 6.0 Introduction

Aim: 2-D *nonlinear* systems.
- General properties
- Examples (from biology & physics)
- Index theory
- Focus on fixed points

------------------------------------------------------------

## 6.1 Phase Portraits

General form of vector field on phase plane:

$$ \dot x_1 = f_1(x_1, x_2) $$
$$ \dot x_2 = f_2(x_1, x_2) $$

or in vector notation:

$$ \dot \boldsymbol x = \boldsymbol f(\boldsymbol x) $$

Entire phase plane filled with trajectories: each point is a suitable initial condition.

Nonlinear systems: typically no hope of analytically determining trajectories.
Instead, what is *qualitative* behavior?

Salient features:
1. **Fixed points** $\boldsymbol x^*: \boldsymbol f(\boldsymbol x^*) = \boldsymbol 0$
2. **Closed orbits**: 1. $\exists T > 0: \boldsymbol x(t+T) = \boldsymbol x(t) \forall t$
3. Arrangment of trajectories near fixed points and closed orbits
4. (in)stability of fixed points and closed orbits

### Numerical Computation of Phase Portraits
Numerical techniques generalize easily to vectors, e.g. the Runge-Kutta method.

**Direction field** as favored over representative field of vectors as different lengths tend to get cluttered.

**Nullclines**: curves where either $\dot x$ or $\dot y$ is $0$. This is where flow is strictly horizontal or verticle.

Example with:
- $\dot x = x + e^{-y}$
- $\dot y = -y$

Space is characterized by one unstable fixed point.

------------------------------------------------------------

# 6.2 Existence, Uniqueness, and Topological Consequences.

But wait, we don't even have guarantees that our nonlinear system has
solutions.


thm. **Existence & Uniqueness theorem** (in general, for
$n$-dimensional systems).

The logical generalization.


corollary: different trajectories never intersect. Otherwise there
would be two solutions for the same initial condition, violating
uniqueness.


thm. **Poincare-Bendixson theorem** if a trajectory is confined to a
closed, bounded region, and there are no fixed points, it must
eventually approach a closed orbit.

------------------------------------------------------------

# 6.3 Fixed Points and Linearization

Somewhat similar to 1-D linearization.

We have a fixed point $(x^*, y^*)$

Consider a small disturbance $\boldsymbol u = (u,v) = (x-x^*, y-y^*)$.

$\dot u = \dot x = f(x^*+u, y^*+v) \approx u \frac{\partial
f}{\partial x} + v \frac{\partial f}{partial y}$

Similarly for $v$, which we can combine:
$$\dot \boldsymbol u = \boldsymbol A \boldsymbol u,$$
where $A$ is the **Jacobian**:
$$A =
\begin{pmatrix}
\frac{\partial f}{\partial x} & \frac{\partial f}{\partial y} \\
\frac{\partial g}{\partial x} & \frac{\partial g}{\partial y}
\end{pmatrix}_{(x^*, y^*)},
$$
evaluated at the fixed point.

**When can you neglect the quadratic terms?**
- As long as we don't have one of the borderline cases
- Recall, these are centers, stars, degenerate nodes, non-isolated
  fixed points.

Example of nonlinear, *uncoupled* system:
$$\dot x = -x + x^3$$
$$\dot y = -2y $$

Example of system where linearization predicts center when reality
gives spiral for non-zero $a$:
$$\dot x = -y + ax(x^2+y^2)$$
$$\dot y = x + ay(x^2+y^2)$$

The slightest, non-zero perturbation to a center turns it into a
spiral.

Nonlinearity can change stable center to unstable spiral!
Nonlinearity can only change stars and degenerate nodes to spirals
with *same* stability.

If stability is our interest, what are the possible trajectories:
- **Robust cases**
  - *Repellers* (aka *sources*): Both e-vals have a positive real
    part.
  - *Attractors* (aka *sinks*): Both e-vals have a negative real part.
  - *Saddles*: One e-val has positive real part, the other has a
    negative, real part.

- **Marginal cases**: At least one e-val has $\text{Re}(\lambda)=0$
  - *Centers*: Both e-vals are pure imaginary
  - **Higher-order** & **non-isolated fixed points**: At least one
    e-val is 0.

**Hyperbolic fixed point**: $\text{Re}(\lambda)\neq0$ for both e-vals.
  - Poor name choice: This is not the same as saddle point.
  - Stability is not affected by small nonlinearities.
  - For higher order systems: same terminology if all e-vals lie off
  imaginary axis.

thm. **Hartman-Grobman theorem**: local phase portrait near a
hyperbolic fixed point is topologically equivalent to the phase
portrait of the linearization.

**Structurally stable**: said of a phase portrait if its topology
cannot be changed by arbitrarily small perturbation to vector field.

------------------------------------------------------------

## 6.4 Rabbits and Sheep

**Lotka-Volterra model of competition**: captures competition between
two species for a shared resource

2 effects:
1. In absence of other species, each grows logistically towards
   carrying capacity. Rabbits have faster growth rate.
2. Sheep win in grazing conflicts which occur at rate proportional to
   population sizes.

Model:

$$ \dot x = x(3-x-2y), $$
$$ \dot y = y(2-x-y), $$

where $x$ is the population of sheep, and $y$ of rabbits.

What biological conclusion results from the following analysis?
- **Principle of competitive exclusion**: one species drives the other
  to extinction when two species compete for the same limited
  resource. This is confirmed in other models.

**Basin of Attraction**: for a given attracting fixed points, this is
the set of initial conditions that are attracted to that fixed point
as $t\rightarrow\infty$.

**Separatrix** or **basin boundary**: The trajectory comprising the
stable manifold which separates basins of attraction.

------------------------------------------------------------

## 6.5 Conservative Systems

**Conserved quantity**: real-valued continuous function that is
constant on trajectories. For this to be nontrivial, the function
should be nonconstant on every open set.

e.g. energy for trajectories of moving particles through phase space.

Newton's law: $m\ddot x = F(x) = -\frac{dV}{dt}$
Moving terms to the same side and inverting the chain rule, we get
$$E=\frac{1}{2}m\dot x^2 + V(x): \frac{dE}{dt}=0$$

Conservative systems cannot have attracting fixed points. The value of
a conserved quantity will be the same for every trajectory in its
basin of attraction, but then, by definition, it is not a conserved
quantity because it is the same on an open set.

Example of double-well potential $V(x) =
-\frac{1}{2}x^2+\frac{1}{4}x^4$

**Homoclinic orbits**: trajectories starting and ending at the same
fixed point. These are not periodic since they take infinite time to
reach the fixed point.

**Nonlinear centers**:
Conservation means that nonlinearities cannot create stable spirals
from centers. They become more robust.

thm. Theorem 6.5.1: Second-order conservative systems will have closed
trajectories in small neighborhoods surrounding isolated fixed
points. This also holds near local maxima

------------------------------------------------------------

## 6.6 Reversible Systems.

Any mechanical system that takes a second-order form has time-reversal
symmetry (second derivatives don't change).

The velocity will change: we reflect over the x-axis in phase space.

**Reversible system**: A second-order system invariant under
$t\rightarrow-t$, $y\rightarrow -y$.

thm. Theorem 6.6.1 (similar to conservative system theorem):
sufficiently close to an origin fixed point, all trajectories are
closed loops for a reversible system.

**Heteroclinic trajectories**: another name for **saddle connections**

Example of determining existence of homoclinic orbit.

More general notion of reversibility using any parity operator.

Example of more general reversibility and showing something is not
conservative by identifying stable fixed points.

------------------------------------------------------------

## 6.7 Pendulum

**Librations**: small-energy fluctuations around lowest-energy state (origin)

------------------------------------------------------------

## 6.8 Index Theory

Linearization as an example of *local analysis*

Index theory as a method of *global analysis*

**Index** of closed curve $C$: integer measuring winding of vector
field on C.
- Choose a reference axis to measure against.
- For each point on $C$, measure the angle with respect to that angle.
- This will change continuously around $C$ (as the vector field is
  smooth)
- So the angle will change by an integer multiple of $2\pi$ over one
  loop.
- This integer is the index.

Properties
 1. If $C$ can be continuously deformed into $C'$ without passing a
   fixed point, $I_C = I_{C'}$. Continuous functions of integers must
   be constant.
 2. If $C$ doesn't enclose fixed points, its winding number is $0$.
 3. Index is invariant under a reversal of the vector field
 4. If the closed curve is a trajectory of the system, then $I_C=1$.

**Index** of a fixed point:
- the index of any closed curve that encloses that point and no other
  fixed point.
- Not related to stability. It is $+1$ for both stable and unstable
  nodes. It is $-1$ for a saddle nodes

The index of a curve around multiple fixed points is simply their sum.

Any closed orbit in the phase plane must enclose fixed points with
indices summing to $1$
