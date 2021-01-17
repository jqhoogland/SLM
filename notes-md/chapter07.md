# Chaptper 7
## Limit Cycles

------------------------------------------------------------

## 7.0 Introduction

**Limit Cycle**: Isolated closed trajectory
**Isolated**: neighboring trajectories are not closed.

*Stable limit cycle*: Neighboring trajectories spiral towards the limit cycle
*Unstable limit cycle*: Neighboring trajectories spiral away from the limit cycle
*Half-stable limit cycle*: One of the neighboring trajectories spirals away from the limit cycle and the other spirals to it.,

Importance in physical world as model of system with self-sustained oscillations

Only possible in *non-linear systems*!
Linear systems can have closed orbits, but not isolated closed orbits

------------------------------------------------------------

## 7.1 Examples

### 7.1.1
Example with radial coordinates: $\dot r = r(1-r^2);\quad \dot \theta=1$
which has a stable limit cycle that is the unit circle.

### 7.1.1 Van der Pol Oscillator

**Van der Pol Equation**:
$$\dot x + \mu (x^2-1)\dot x + x = 0$$

This is a simple harmonic oscillator with a nonlinear damping term:
positively damping for $|x|>1$, but negative for $|x|<1$.

With a bit of work, you can show there is a unique stable limit cycle
for each positive $\mu$.

------------------------------------------------------------

## 7.2 Ruling Out Closed Orbits

How to go about proving that a system has no periodic solutions?
1. Index theory (previous chapter)
2. Gradient Systems
3. Liapunov Functions
4. Duloc's Criterion

Options 2-4 presented in this chapter

### Gradient Systems

**Gradient system**: one which can be written as $\dot \boldsymbol x =
-\nabla V$, for continuously-differentiable, single-valued scalar
$V(\boldsymbol x)$
**Potential function**: $V$ in the above.

thm. Closed orbits are impossible in gradient systems

pf. Contradiction. Assume closed orbit.
- $\Delta V = 0$ because it is single-valued
- $\Delta V = \int_0^T \frac{dV}{dt} dt = \int (\nabla V \cdot
  \boldsymbol \dot x)dt = -\int ||\dot \boldsymbol x||^2 dt < 0$

This kind of proof works more generally even if not a gradient system.

### Liapunov Functions

**Liapunov Function**: A continuously differentiable, real-valued
function $V(\boldsymbol x)$ that satisfies:
- Positive definite:
  - $V(\boldsymbol x) > 0 \forall \boldsymbol x \neq \boldsymbol x^*$
  - $V(\boldsymbol x^*) = 0$
- All trajectories flow downhill to $\boldsymbol x^*$
  - $\dot V < 0 \forall \boldsymbol x \neq \boldsymbol x^*$

If this is satisfied, then $\boldsymbol x^*$ is globally
asymptotically stable.

Solutions can't get stuck anywhere, then $\dot V= 0$ which contradicts
the assumption.

Hard to construct these functions.

Example where sum of squares works.

### Dulac's Criterion

Based on Green's theorem

**Dulac's Criterion**: $\dot \boldsymbol x = \boldsymbol f
(\boldsymbol x)$ is continuously differentiable vector field defined
on simply connected subset $R$ of plane. If there is a continuously
differentiable, real-valued function $g(\boldsymbol x)$: $\nabla
\cdot (g\boldsymbol \dot x)$ has one sign throughout $R$, there are no
closed orbits in $R$.

pf. Suppose there is a closed orbit, $C$ in this region.
- $A$ denotes area of region inside $C$>
$$\int\int_A \nabla \cdot (g\dot \boldsymbol x)dA = \oint
g\dot\boldsymbol x \cdot \boldsymbol n dl$$
- left-hand side is non-zero because the product has one sign
  throughout $R$; right-hand side is zero because $C$ is a trajectory.

Hard to find $g(\boldsymbol x$).
Candidates:
$g=1,1/x^ay^b, e^{ax}, e^{ay}$

------------------------------------------------------------

## 7.3 Poincare-Bendixson Theorem

Opposite goal to previous section: *Establish existence of closed
orbits*

This theorem is one of the few results in this direction, also
establishes absence of chaos in phase plane.

thm. **Poincare-Bendixson Theorem**:
- Suppose:
  1. $R$ is closed, bounded subset of plane
  2. $\dot\boldsymbol x = \boldsymbol f(\boldsymbol x)$
  3. $R$ contains no fixed point
  4. There exists a trajectory $C$ confined in $R$. (This is the tough condition)
- Then, options:
  1. $C$ is a closed orbit
  2. $C$ spirals towards a closed orbit
- Always: $R$ contains some closed orbit

How to meet condition 4:
- Construct **trapping region** $R$ which has vector field on boundary
  pointing inward for all points.

Difficult to apply in practice, convenient case with polar coords.

Good example 7.3.2 of glycolysis

### No Chaos in the Phase Plane

Requires 2-dimensionality of phase plane.

In 3D- trajectories can wander around forever in a bounded region
without settling down to a fixed point or closed orbit. Sometimes
attracted to a strange attractor- fractal set with aperiodic motion
sensitive to tiny changes in initial conditions. Leads to
unpredictable long-term behavior (i.e. chaos!)

------------------------------------------------------------

## 7.4 Lienard Systems

Context: 1920s-50s lots of research into nonlinear oscillators (think radios and vaccuum tube tech)

def. **Lienard's equation**:
$$ \ddot x + f(x) \dot x + g(x) = 0 $$

Equivalently:
$$\dot x = y$$
$$\dot y = -g(x)-f(x)y$$

Generalization of the van der Pol oscillator
(reminder: $\ddot x + \mu(x^2-1)\dot x + x = 0$)

Mechanically: equation of motion for unit mass subject to nonlinear damping force $-f(x)\dot x$ and nonlinear restoring force $-g(x)$

thm. **Lienard's Theorem**:
- Suppose $f$ and $g$ satisfy:
  1. Continuously differentiable for all $x$
  2. $g$ is odd
  3. $g$ is positive for positive $x$
  4. $f$ is even
  5. defining $F(x)\equiv \int_0^xf(u)du$
    - $F$ has $1$ positive zero at $x=a$,
    - $F$ is negative for $x\in (0,a)$
    - $F$ is positive and nondecreasing $x>a$
    - $F\rightarrow \infty$ as $x\rightarrow \infty$

- Implies: system has unique, stable limit cycle surrounding origin in phase plane.

Intuition:
- Requirements on $g$ make it act like an ordinary spring
- Requirements on $f$ make the damping negative at small $|x|$ and positive at large $|x|$, you'd expect the system to settle down somehwere in between.

Example: Show the van der Pol eqn has a unique, stable limit cycle.
How: show $g$ and $f$ satisfy the above constraints

------------------------------------------------------------

## 7.5 Relaxation Oscillations

Chapter 7 until now: qualitative questions

Now: quantitative question: *Given that a closed orbit exists, what can we say about its shape and period?*

Exact solutions rare, but we can get useful approximations.

Start: van der Pol equation, where $\mu >> 1$, *strongly nonlinear* limit.
- Example of **relaxation oscillations**, limit cycle as slow build up followed by sudden discharge.

#### Example: give the analysis for this equation.

Need for some change of variables
Focus on the nullclines

Limit cycle has 2 widely separated time scales, $O(\mu)$ and $O(\mu^{-1})$.

Estimating total period is dominated by 2 **slow branches**.

Here the two time scales are sequential
Next section: two time scales operating concurrently.

------------------------------------------------------------

## 4.6 Weakly Nonlinear Oscillators

$$\ddot x + x + \epsilon h(x,\dot x) = 0$$
where $|\epsilon|<<1$ and $h$ is arbitrary smooth function.

This is a small perturbation from the linear oscillator.

Example:
1. van der Pol equation in opposite limit to previous section
2. **Duffing Equation**: $\ddot + x + \epsion x^3$

### Regular Perturbation Theory and Its Failure

Approach 1: **Regular Perturbation Theory**

Find solutions in terms of power series in $\epsilon$
$$x(t,\epsilon) = x_0(t) + \epsilon x_1(t) + \epsilon^2 x_2(t) + \dots$$

Hope: most of the relevant information is captured in first few terms.

Expose difficulties:
##### Example: $\ddot x + 2\epsilon \dot x + x=0$
IC: $x(0)=0,\quad \dot x(0)=1$

Exact solution:
$$x(t, \epsilon) = (1-\epsilon^2)^{-1/2}e^{-\epsilon t} \sin\left[ (1-\epsilon^2)^{1/2} t\right].$$

With perturbation theory:
Plug in expansion, group terms to get:

$$[\ddot x_0 + x_0] + \epsilon[\ddot x_1 + 2\dot x_0 + x_1] + O(\epsilon^2)=0$$

Power-by-power the coefficients should vanish (because our solution is supposed to hold for all (arbitrarily small) $\epsilon$

$$O(1): \ddot x_0 + x_0 = 0$$
$$O(\epsilon): \ddot x_1 + 2\dot x_0 + x_1 = 0$$

Apply initial conditions to get
$$x_0(t) =\sin t$$

which leads to
$$\ddot x_1 + x_1 = -2\cos t$$
with solution
$$x_1(t)=-t\sin t$$

**Problem**: RHS is **resonant** forcing which blows up at infinite $t$

This provides the a good solution in that it is the series expansion of the true answer, valid as long as the next terms are small enough $\epsilon t << 1$.

We are interested however in behavior for fixed $\epsilon$ not fixed $t$.

##### Major Problems
1. True solution has **2 time scales**, fast one for sinusoidal oscillations and slow one for amplitude decay. To get correct slow time scale in perturbation theory we'd need infinite order expansion. Shit.
2. Frequency of oscillations is shifted slightly from true frequency which will lead to increasing error with long times (third time scale)

### Two-Timing
More generally, there are two time scales in weakly nonlinear oscillators.

Technique to address this: **two-timing** (you can include more than 2 times)

$\tau=t$: Fast $O(1)$ time.
$T=\epsilon t$: Slow time.

We treat these as *independent variables*, regarding the latter as constant on fast time scale.

We still use a series expansion, then transform the time derivatives with a chain rule: $\frac{d}{dt} = \frac{\partial}{\partial \tau} + \epsilon \frac{\partial}{\partial T}$

Same example but now with two-timing

Example of van der Pol Oscillator solved through two-timing: determination of limit cycle approximate form.

### Averaged Equations

General: $\ddot x + x + \epsilon h(x, \dot x) = 0

Two-timing: $h(x, \dot x) \rightarrow h(x, \partial_\tau x)$
$$O(1): \partial_{\tau\tau} x_0 + x_0 = 0$$
$$O(\epsilon): \partial_{\tau\tau} x_1 + x_1 = -2 \partial_{\tau T} x_0 - h$$

Solution for first equation is:
$$x_0=r(T)\cos(\tau + \phi(T))$$

Demand no terms on RHS of second equation proportional to sinusoidal functions.

Substituting, :
$$-2 \partial_{\tau T} x_0 - h =
2[r'\sin(\tau+\phi)+r\phi'\cos(\tau+\phi)]-h(r\cos(\tau+\phi),
-r\sin(\tau+\phi))$$

We expand $h$ as Fourier series (it is $2\pi$ periodic), $a_k$
coefficients on cosines, $b_k$ on sines.

The resonant terms will be $[2r'-b_1]\sin\theta$ and
$[2r\phi'-a_1$]\cos \theta$.

To avoid secular terms we require $r'=b_1/2= \langle h \sin
\theta\rangle$ and $r\phi'=a_1/2 = \langle h \cos \theta \rangle$.

These are the **averaged** or **slow-time** equations.

#### Example with van der Pol oscillator
#### Example with Duffing Equation
- Here the frequency depends on the amplitude (fundamentally a
  nonlinear effect)
