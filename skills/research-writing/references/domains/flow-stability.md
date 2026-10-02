# Profile: numerical fluid-flow stability

This is a conditional profile, not the core architecture. Do not assume the user's flow geometry, governing equations, or stability formulation. Select only applicable checks; mark inapplicable items with a reason and never award free points for them.

## Intake and argument choices

Identify the base state, parameter/control variables, the stability notion actually studied, and the quantity that will decide the question. Clarify modal asymptotic behavior versus finite-time amplification, linear versus finite-amplitude conclusions, and temporal/spatial/global/local formulations only when relevant. Agreement about the question belongs in the intent tree; detailed numerical evidence is inspected while filling.

## Numerical claim review

| Intended scientific assertion | Evidence/conditions to inspect while filling |
|---|---|
| A modal growth rate changes or crosses neutrality | Growth-rate definition and sign convention; parameter range; boundary conditions; convergence and mode identification near crossings |
| Finite-time amplification changes | Chosen norm, optimization horizon, initial-condition class, normalization, numerical optimization/convergence |
| A simulation corroborates a linear prediction | Perturbation amplitude/regime, measured quantity, time window, consistency of protocol and normalization |
| An observed structure explains instability | Diagnostic versus definition; actual identifying/discriminating evidence; competing explanations and scope |
| A stability boundary is robust | Numerical sensitivity relevant to that boundary, interpolation/sampling uncertainty, and physical model assumptions |

Do not infer absence of finite-time amplification solely from modal decay. Do not infer nonlinear stability from a linear calculation. Do not call a trend a mechanism merely because two fields correlate. Domain review is semantic; a populated “convergence” field or a small residual does not automatically establish the scientific claim.

Record the actual solver, base-state procedure, discretization, boundary conditions, nondimensionalization, convergence criterion, eigenvalue convention, and relevant time-step/domain-size checks. Prefer a small diagnostic calculation that can change the claim over an unrestricted parameter sweep. Specify which mode or observable the comparison follows and how ambiguity will be handled.

## Figure contracts

Link a planned figure to the sentence IDs it helps realize in the project's separate figure notes. Record the question answered, actual data source, axes/units/normalization, fixed and varied parameters, comparisons, uncertainty or numerical sensitivity where meaningful, and the readout. Preserve native plot code and vector outputs when possible. Use actual numerical results and uncertainty appropriate to deterministic calculations.

## Terminology and source basis

Maintain manuscript-specific terms and notation, e.g. the chosen names for base flow, perturbation energy, growth rate, neutral boundary, and the relevant modes. Use [fluid writing](fluid-writing.md) for definitions, prose and figure language; choose terminology appropriate to the flow problem.

Primary references supporting the profile's general distinctions:

- Schmid, *Nonmodal Stability Theory* (2007), [publisher abstract and bibliographic record](https://www.annualreviews.org/content/journals/10.1146/annurev.fluid.38.050304.092139): modal analysis and finite-time disturbance behavior address different questions.
- NASA NPARC, [CFD verification and validation tutorial](https://www.grc.nasa.gov/www/wind/valid/tutorial/tutorial.html) and [verification assessment](https://www.grc.nasa.gov/www/wind/valid/tutorial/verassess.html): numerical error and convergence require assessment.

These references justify general checks, not the user's research claim, a universal convergence tolerance, or current journal submission requirements.
