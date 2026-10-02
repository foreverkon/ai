# Fluid-mechanics manuscript writing

Use when drafting or revising fluid-mechanics prose. The choices below are supported by the named JFM and PoF articles; they are adaptable practices, not journal-wide frequency claims or a fixed section template. Use [English realization](../english.md) for generic language consistency and [flow stability](flow-stability.md) for numerical verification.

## Journal requirements

- JFM requires a single-paragraph abstract of at most 250 words summarizing aims and results. AIP's general guidance applicable to PoF calls for a single paragraph without displayed equations, footnotes, references, graphics or tables; PoF Letters have separate abstract and section restrictions. [JFM instructions](https://www.cambridge.org/core/journals/journal-of-fluid-mechanics/information/author-instructions/preparing-your-materials); [AIP instructions](https://publishing.aip.org/resources/researchers/author-instructions/).
- JFM requires each figure to have a single caption, be cited in the text and follow the order of first mention. [JFM instructions](https://www.cambridge.org/core/journals/journal-of-fluid-mechanics/information/author-instructions/preparing-your-materials).
- Follow the journal's language and notation conventions: JFM specifies British spelling; AIP specifies scientific American English, punctuated displayed equations and consistent mathematical fonts/notation. Keep the chosen spelling consistent and treat each equation as part of its sentence. [JFM instructions](https://www.cambridge.org/core/journals/journal-of-fluid-mechanics/information/author-instructions/preparing-your-materials); [AIP instructions](https://publishing.aip.org/resources/researchers/author-instructions/).

## Build the argument paragraph by paragraph

- Turn the introduction's literature into a specific question: state the established result and tested regime, identify the unresolved observable or extrapolation, then explain which comparison answers it. Cite the supported proposition rather than attaching a reference to a broad topic. [H08 §1; CC23 §1; M19 §I; L23 §I]
- In methods, connect the physical setup and assumptions to the analyzed quantity: scales and boundary conditions → calculation or measurement → processing → observable and relevant check. Explain a method choice through the quantity it enables. [H08 §2; M19 §II; L23 §§II–III; C24 §I]
- Give a result paragraph one deciding task. Orient the reader to the quantity, cases and fixed parameters; report the readout; interpret the comparison. Change that order when a definition or derivation must come first. [H08 §2.2; CC96 §3; ODA24 §3; M19 §IIIB]
- Explain a derivation through its operations and purpose: substitute the expansion, collect terms, impose the compatibility condition, identify the coefficient or relation obtained. Introduce the small parameter before using *at leading order*. [H08 §3; SL07 §2; CC96 §2]
- Conclude with the physical answer and its scope. Retain a disagreement, limiting condition or counterexample when it changes that answer; do not compress a necessary condition into a sufficient one. [H08 §5; SL07 §4; L23 §§IVB–C; K20 §IIIB]

## Choose tense, subject and claim strength

- Use the present for definitions, governing relations, figure readouts and claims that the paper establishes; use the past for completed operations and a particular earlier study. Present perfect can connect completed work to its current implication. Choose by sentence function, not by section name. [H08 §§2,5; SL07 §§1,4; L23 §§II–III; C24 §II; K20 §IV]
- Use *we* for a deliberate modelling, measurement or comparison choice; use the field, equation, apparatus or boundary as subject when its treatment is the focus. Active and passive constructions both occur in the source methods. [H08 §2.2; ODA24 §2; L23 §III; M19 §II]
- Separate readout from explanation: *increases/decreases* reports a trend; *agrees within …* quantifies a comparison; *supports/is consistent with* relates a diagnostic to an interpretation; *may* marks an unresolved explanation. Give the assumptions next to the inference they restrict and say what evidence would resolve a proposed mechanism or threshold. [H08 §§3,5; SL07 §§3,4; C24 §IIIB; K20 §IIIB]
- Use *whereas* for parallel contrast, *because* for an established reason and *therefore* for an implication with nearby premises. An attractive flow field alone does not supply the missing causal premise. [H08 §§2,5; SL07 §§3,4; CC96 §3]
- Make a cited study the sentence subject when comparing its finding or assumption; place a citation at the imported definition or method. Use the target journal's citation form; author–year and numerical styles can both perform these functions. Give a figure/table/section locator when the comparison depends on that item. [H08 §§1,2; M19 §I; C24 §IIIC]

## Quantify the comparison

- Name the reference case, normalization, parameter range and quantity before writing *higher*, *lower*, *agreement* or *independent of*. A percentage change needs a denominator; a threshold comparison needs compatible dimensionless definitions, including velocity, length and viscosity/rheology conventions. Keep a maximum effect tied to its case. [H08 §2; CC96 §2.3; ODA24 §3; K20 §IIIB1; C24 §II]
- Define the criterion behind *critical*, *optimal*, *broad-band* or *negligible*. A linear neutral point, first asymmetric structure and first turbulent puff are different thresholds; a large fit coefficient of determination describes that fit, not every model prediction. [M19 §IIIA; L23 §IVB; C24 §§IIIA–C]
- Report agreement and departure at the precision the evidence supports. Qualitative evidence supports a bounded qualitative comparison; numerical accuracy or percentage-error claims need a defined metric and data. When quantification is needed, specify the additional measurement, calculation or documented figure reading. [SL07 appendices A,C; M08 §IIIB; L23 §IVA]
- Match values to cases, check quantity names against definitions and dimensions, and choose reported precision from relevant sensitivity. [SL07 appendices A,C; M19 §§II–III; C24 §§IIIA–B]
- Distinguish a measured trend, a fitted scaling and an asymptotic relation. State the fitted/tested interval or limiting parameter; check where agreement ends instead of extending a relation from visual resemblance. [H08 §§3,4; SL07 §§2,3; ODA24 §3]
- State what the calculation determines. Linear modal growth, finite-amplitude saturation and an energy-source interpretation are different claims; attach the regime and diagnostic to each. [SL07 §§2.4–2.6; CC96 §§2.4,3]

Original sentence templates; replace brackets with verified quantities and conditions:

> We discretize the disturbance equations using [basis and grid] and solve the resulting generalized eigenvalue problem for [eigenvalue].
> Using the same [Reynolds-number definition and scales], the critical Reynolds number increases from [A] to [B] as [parameter] changes from [p1] to [p2].
> For [unstable mode and conditions], [term] is the dominant positive energy source and [term] is a negative sink. The full signed disturbance-energy budget gives [positive net growth rate], supporting [interpretation] of the linear instability.
> The model reproduces the frequency dependence of the droplet–plate phase shift but underpredicts its high-frequency maximum. [Original paraphrase of L23 §IVA]

## Use terms for their physical meaning

Select terms appropriate to the flow studied. The short combinations are writing examples; the cited passages supply the definitions and distinctions.

| Term and useful combination | Meaning and writing decision | Source |
|---|---|---|
| **base flow**; linearize about the base flow | Reference state for linearization; say whether it is steady. | SL07 §2.3.1 |
| **mean flow**; time-averaged mean flow | Averaged state; define the averaging operation. It can differ from the base flow. | SL07 §2.5 |
| **critical Reynolds number**; determine the critical Reynolds number | Specify the nondimensional definition, including scales and viscosity/rheology convention, and the mode or threshold criterion. | H08 §2; CC96 §2.3; C24 §II |
| **neutral curve**; trace the neutral curve | Zero-growth locus in a stated parameter plane, with other parameters fixed. | H08 §2.2 |
| **least damped eigenmode**; track the least damped eigenmode | Largest growth rate under the declared sign convention; it may still decay. | H08 §2.2 |
| **marginally stable**; marginally stable mode | Zero or nearly zero linear growth, as specified; do not infer nonlinear stability. | SL07 §2.6 |
| **solvability condition**; impose the solvability condition | Compatibility condition for a singular linear problem; state what it determines. | H08 §3 |
| **saturated limit cycle**; approach a saturated limit cycle | Periodic finite-amplitude state; state the validity of the amplitude model. | SL07 §2.4.2 |
| **disturbance energy budget**; evaluate the energy budget | Signed production/dissipation contributions; name the terms supporting the explanation. | CC96 §2.4 |
| **buoyancy-assisted / buoyancy-opposed flow** | Specify the buoyancy force relative to the mean-flow direction; heating/cooling alone does not define it. | CC96 §2 |
| **roughness sublayer**; within the roughness sublayer | Roughness-affected near-wall region; state how its extent is identified in the flow studied. | CC23 §3.2 |
| **dispersive stress**; compute the dispersive stress | Stress from spatial deviations of the time-mean velocity; define the averaging and decomposition. | CC23 §2.3 |
| **self-similar form**; collapse onto a self-similar form | Specify rescaled variables and the range over which collapse is tested. | ODA24 §3 |
| **cubic Landau equation**; equilibrium / threshold amplitude | A weakly nonlinear amplitude model. Define coefficient signs and distinguish a stable saturated amplitude from an unstable-branch threshold. | K20 §II |
| **phase speed**; determine the phase speed | For a temporal mode, c = ω_r/k: ω_r is the real part of angular frequency and k ≠ 0 is real angular wavenumber. | M19 §§II,IIIB |
| **phase shift**; droplet–plate phase shift | Relative phase between specified motions; state the droplet–plate or droplet–droplet reference. | L23 §§IIB,IVB |
| **amplification ratio**; measure the amplification ratio | Define numerator and denominator amplitudes; a displacement-amplitude ratio is not a growth rate. | L23 §IIB |
| **yield stress**; fit a yield-stress model | State the threshold stress, units and constitutive model; specify how it is estimated. | C24 §II |
| **shear-thinning**; shear-thinning fluid | Apparent viscosity decreases with increasing shear rate; distinguish this property from elasticity. | C24 §§I–II |
| **intermittency indicator**; quantify intermittency | Define the turbulent-time fraction, detection criterion and observation window. | C24 §IIIC |

## Connect figures to prose

- Use the caption to identify quantity, panels, conditions, normalization and line/symbol encodings. Use the body to read the decisive comparison and explain its implication. [H08 figs 1–3; SL07 figs 3,8; ODA24 figs 12–13; M19 fig.7]
- Give fixed and varied parameters, displayed components and scales. Normalized eigenfunctions compare structure; physical amplitudes require an explicit amplitude prescription and compatible scales. Distinguish measured/simulated curves from hypothetical continuations. [H08 §2.2; SL07 §§2.3.2,2.4.2; M19 fig.7; L23 §IVC, fig.8]
- Choose the diagnostic that answers the paragraph's question: a neutral map for regimes, a budget for energy sources, a time series for evolution or a rescaled plot for similarity. Introduce the figure and then state the relevant trend rather than leaving the reader to infer it. [H08 §2; CC96 §3; ODA24 §3]

## Revision pass

1. State each paragraph's answer in one line; repair sentences that do not advance it.
2. Check every comparison for its quantity, reference, scales and range.
3. Choose tense and grammatical subject by sentence function; place citations at the supported claim.
4. Replace vague labels with defined terms; preserve qualifiers that distinguish different physics.
5. Check each figure/caption/body sequence for conditions, readout and inference.
6. Ensure the abstract and conclusion give the same bounded physical answer as the results.

## Primary articles

- **H08** — [Heaton (2008), annular Poiseuille stability](https://doi.org/10.1017/S0022112008002577).
- **SL07** — [Sipp & Lebedev (2007), cylinder and cavity global stability](https://doi.org/10.1017/S0022112007008907).
- **CC96** — [Chen & Chung (1996), mixed convection in a vertical channel](https://doi.org/10.1017/S0022112096008026).
- **CC23** — [Chan & Chin (2023), rough-wall turbulent boundary layers](https://doi.org/10.1017/jfm.2023.818).
- **ODA24** — [Osama, Deegan & Agbaglah (2024), drop impact on a thin film](https://doi.org/10.1017/jfm.2024.766).
- **M19** — [Moradi & Tavoularis (2019), weakly eccentric annular-flow instability](https://doi.org/10.1063/1.5088992).
- **M08** — [Merzari et al. (2008), eccentric-annular-channel stability](https://doi.org/10.1063/1.3005864).
- **K20** — [Khan & Bera (2020), non-isothermal annular-flow bifurcation](https://doi.org/10.1063/5.0021104).
- **L23** — [Lei et al. (2023), droplet coalescence on a vibrating vertical surface](https://doi.org/10.1063/5.0157591).
- **C24** — [Charles et al. (2024), asymmetry and intermittency in pipe-flow transition](https://doi.org/10.1063/5.0211807).
