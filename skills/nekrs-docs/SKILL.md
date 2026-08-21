---
name: nekrs-docs
description: Use the official nekRS documentation to install and build nekRS, create or review simulation cases, configure .par files, write .udf/OKL hooks, choose boundary and initial conditions, prepare meshes, run on workstations or HPC systems, select models and properties, postprocess results, follow tutorials, and troubleshoot failures. Trigger for nekRS CFD usage, configuration, examples, diagnostics, and documentation-grounded explanations; do not use for Nek5000 unless the request specifically concerns nekRS interoperability.
---

# Work with nekRS

Ground answers and edits in the bundled official nekRS documentation. Treat the references as
authoritative for the documented version, but account for version drift.

## Start here

1. Classify the request by topic.
2. Read `references/index.md` and only the references routed to that topic.
3. Search the relevant files for the exact option, callback, command, or error text before answering.
4. When proposing a case change, inspect the user's existing `.par`, `.udf`, mesh inputs, launch
   command, nekRS version, compute backend, and relevant log excerpt when available.
5. Preserve exact section names, parameter spelling, units, field names, and code signatures from
   the documentation or examples. Never invent a configuration key or callback.
6. Distinguish verbatim upstream examples from adaptations. Explain every adaptation that affects
   physics, boundary conditions, discretization, time stepping, solver behavior, or resource use.

Use a fast text search when the answer depends on exact syntax:

```bash
rg -n -i "search term" references/documentation references/examples
```

## Solve common tasks

### Explain or configure a case

- Read `case.rst` first, then the topic-specific reference.
- Separate host-side UDF functions from device-side `__okl__` boundary/source code.
- Relate each proposed setting to its `.par` section or UDF callback.
- Prefer a minimal patch over rewriting a complete case.

### Diagnose a failed run

- Read `debugging.rst`, `running.rst`, and the relevant setup reference.
- Establish whether failure occurs during build, JIT compilation, mesh loading, initialization,
  time stepping, output, or scheduler launch.
- Ask for or inspect the first causal error, not only the final MPI abort line.
- Avoid claiming that a fix is portable across CUDA, HIP, DPC++, SERIAL, MPI implementations, or
  schedulers unless the documentation supports it.

### Produce a new example

- Start from the closest bundled example under `references/examples/`.
- Cross-check it against the corresponding tutorial and current case-file documentation.
- Keep geometry, boundary IDs, nondimensionalization, material properties, and process counts
  explicit. Mark placeholders clearly.
- Do not present a case as validated unless it was actually built and run in a compatible nekRS
  environment.

### Answer theory or modeling questions

- Use `theory.rst` for governing equations and `models.rst`/`properties.rst` for implementation
  controls.
- State assumptions and distinguish documented behavior from general CFD guidance.

## Handle uncertainty and freshness

- The bundled quickstart documents nekRS v26.0 commands. If the installed version differs, say so
  and check its `RELEASE.md`, `nrsman`, or matching
  versioned docs before giving exact commands or parameters.
- If the bundled docs do not support a claim, state the gap. Consult the official nekRS repository
  or documentation when current external access is available.
- Do not silently generalize from Nek5000 syntax to nekRS.

## Reference navigation

Read `references/index.md` for the topic-to-file map and example inventory. Load individual large
references only when the task requires them.
