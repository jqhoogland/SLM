# Chapter 9
## Lorenz Equations

------------------------------------------------------------

## 9.0 Introduction

The **Lorenz Equations**:
$$ \dot x = \sigma(y-x), $$
$$ \dot y = r x - y - xz, \text{ and}$$
$$ \dot z = xy - bz, $$

$\{\sigma, b, r\}$ are parameters $> 0$

Look to (Ed) Lorenz's original paper (1963)

------------------------------------------------------------

## 9.1 A Chaotic Waterwheel

A physical realization with these exact equations!

------------------------------------------------------------

## 9.2 Simple Properties of the Lorenz Equations

$\sigma$ is the **Prandtl number**
$r$ is the **Rayleigh number**, ratio of driving intensity to dissipation
$b$ has no name (related to aspect ratio of rolls in convection problems)

#### Nonlinearities

Two quadratic instances: $xy$, and $xz$

#### Symmetry

$(x, y) \rightarrow $(-x, -y)$.
]

#### Volume Contraction

This system is **dissipative**: Volumes in phase space contract under the flow.

But first...
How do volumes evolve?

Consider a surface at time $t$, let it evolve an infinitessimal time
to a new surface. What is the difference in volumes enclosed by these
surfaces?

$$V(t+dt)-V(t)=\int_S (\boldsymbol f \cdot \boldsymbol n dt)dA$$

$$ \dot V = \int_S (\boldsymbol f \cdot \boldsymbol n)dA = \int_V
\nabla \cdot \boldsymbol f dV$$

Where $\nabla \cdot \boldsymbol f = -\sigma -1 -b < 0$.

So the volume in phase space shrinks exponentially fast.

What are these sets of zero volume?
- Fixed points
- Limit cycles
- Strange attractors (chaos)

No quasiperiodic solutions by contradiction (of torus volume having to
stay the same)

No *repelling* fixed points or orbits: repellers create volume.

All fixed points should be sinks or saddles.
All closed orbits (if they exist) must be stable or saddle-like.

#### Fixed points
- Origin always a fixed point
- $r>1$: There is a symmetric pair of fixed popints
  $x^*=y^*=\pm\sqrt{b(r-1)}, z^*=r-1$
  - These are left-, $C^+$, or right-, $C^-$, turning convection rolls.
  - These coalesce in pitchfork bifurcation (recall symmetry)

#### Linear Stability of Origin
- $z$ equation decoupled and shrinks to $0$ exponentially fast.
- $\mathcal J = \begin{pmatrix}
  -\sigma & \sigma \\
  r & -1
  \end{pmatrix}.$
  - $r>1$: origin is saddle-point (2-in, 1-out)
  - $r<1$: origin is a sink. In fact, this is **globally stable**, no
    other solutions exist (use a Lyapunov function with concentric
    ellipsoid energy function).

#### Stability of $C^+$ and $C^-$

These are linearly stable for:
$1<r<r_H=\frac{\sigma(\sigma + b + 3)}{\sigma-b-1}

They lose stability in a subcritical Hopf Bifurcation which has
unstable, **saddle cycles** (stable in cylinder height direction
but instable in the directions along the plane of the cycle). These
are only possible in $\geq3$ dimensions.

What happens instead then? Trajectories to infinity? Nope, they remain
in a certain large ellipsoid.

------------------------------------------------------------

## 9.3 Chaos on a Strange Attractor

Lorenz used numerical integration to look at $(\sigma=10, b=8/3,
r=28)$.

Hopf bifurcation value for these parameters is $r_H=24.74$
These solutions are aperiodic!

Comment on exponential divergence of initially close points.
=> **Lyapunov exponents**

Watch out:
- Terminology, when we talk of *the* Lyapunov exponent, we actually mean
the largest of the $n$ exponents (since we're in $n$ dimensions)
- The exponent actually depends on the trajectory you're looking
  at. In practice, you should average over many points on the same
  trajectory.

Positive Lyapunov exponent => Existence of time horizon at which
prediction breaks down.

$\delta_0$ is original discrepancy
$a$ is allowed tolerance

$t_{\text{horizon}} \sim O\left( \frac{1}{\lambda} \ln
\frac{a}{||\delta_0||}\right)$

#### Chaos
No universally accepted definition of **chaos** at time of writing

> **CHAOS** is (1) *aperiodic long-term behavior* in a (2)
> *deterministic* system that exhibits (3) *sensitive dependence on
> initial conditions*.

3 key elements:
1. **Aperiodic long-term behavior**: there are trajectories which do
   not settle to fixed points, periodic points, or quasiperiodic
   orbits as $t\rightarrow \infty$.
   - For practicality, these should not be rare (e.g. there is some
     open set of points that lead to these aperiodic trajectories, or
     non-zero probability for random IC)
2. **Deterministic system**: No random or noisy inputs or parameters
   - Irregularity arises from nonlinearity alone.
3. **Sensitive dependence on initial conditions**: nearby trajectories
   separate exponentially fast (postive Lyapunov exponents)


Instability is not chaos => Think of infinity as an attractive fixed
point.

#### (Strange) Attractor
Similarly difficult to define rigorously

>**Attractor** is a set to which all neighboring trajectories
>converge. This includes stable fixed points and limit cycles. It is a
>closed set, $A$ with the following properties:
1. $A$ is an *invariant set*: all trajectories starting in the set
   stay in the set for all time.
2. $A$ *attracts an open set, $U$ of initial conditions*: $U$ contains
   $A$, then for infinite time all points in $U$ tend to zero distance
   from $A$. Largest $U$ possible is the **Basin of attraction**
3. $A$ is *minimal*: no proper subset of $A$ that satisfies (1) and
   (2).

Noone knows (at time of writing) whether the Lorenz set strange
attractor is actually an attractor in sense (3).

def. **Strange attractor**: attractor with sensitive dependence on
initial conditions. This is currently regarded as less important than
the geometric property of being a fractal set (use *chaotic* or *fractal*
attractor to emphasize these notions)

------------------------------------------------------------

## 9.4 Lorenz Mapping

Plotting the curve on the $yz$-plane, trajectories only leave one
spiral upon reaching a certain maximum value.

Let $z_k$ be the $k$-th local maximum $z$ value attained.

$z_{k+1}$ should be a function of $z_k$.

Indeed, performing the numerical integration, these points fall *almost*
perfectly on a curve.

def. **Lorenz Map**: function $f: z_{k+1}=f(z_k)$.

The curve has thickness => This is not a well defined function, but we
can treat it approximately as such.

How is this reminiscent of the Poincare map?
- Poincare map takes points on a surface, i.e. two coordinates
- Lorenz map uses only one number: requires a very flat attractor
  (i.e. close to 2D) such as this one.

#### Ruling out Stable Limit Cycles

Key observation: $|f'(z)|>1$ everywhere.
So if a limit cycle exists: it's unstable.

The fixed point of the Lorenz map is unstable.

Extension for all stable limit cycles by contradiction.

Assume there is a closed loop, then look at how a perturbation over
the loop, this is with the product of the $f'(z_k)$'s which are all
$>1$.

------------------------------------------------------------

## 9.5 Exploring Parmeter Space

Narrowing to $r$ for the same fixed $\sigma$ and $b$ as before.

There is a region of **transient** or **metastable chaos** or
**preturbulence**.

These have initially unpredictable behavior but do ultimately settle
to some (again it's unpredictable which one) equilibrium points.

Example of rolling dice (deterministic system with simple final states which depends
sensitively on initial conditions).

Limit cycle emerges for $r>313$

Infinite limit yields analytical results.

Between $r=28$ and $313$ it's more difficult: there are regions of
periodic behavior like the logistic map!

------------------------------------------------------------

## 9.6 Using Chaos to Send Secret Messages

Ability to create a receiver which approaches chaotic system behavior
from partial information.
- Construct a Lyapunov function to cancel out the chaos
