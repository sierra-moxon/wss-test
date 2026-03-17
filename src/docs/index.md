# Water Sample Schema (wss-test)

A [LinkML](https://linkml.io/) schema for structured water sample measurement data.
Built on the [BERtron](https://github.com/ber-data/bertron-schema) common data model,
wss-test adds measurement provenance, variable semantics, and QC metadata to BERtron's
base `Attribute` and `QuantityValue` types.

## What it does

The schema captures environmental water quality measurements in a validated, structured
format — replacing flat spreadsheets with a model that separates **what** was measured
from **how** and **when** it was measured.

```
 DATA FLOW                      BERTRON                          OBSERVATIONS
 ─────────                      ───────                          ────────────

 Dataset                        bertron:DataCollection           bertron:AttributeValue (abstract)
 ├── variables[]                  ├── id, title, description       ├── attribute → Attribute
 │   └── Variable                │                                ├── raw_value
 │                                └── wss:Dataset                  │
 └── samples[]                        ├── + variables[]            ├── bertron:QuantityValue
     └── Sample                       └── + samples[]              │     ├── numeric_value
         └── measurements[]                                        │     ├── unit, unit_cv_id
             └── Measurement    bertron:Entity                     │     │
                  └── attribute   ├── id, name, description        │     └── wss:Measurement
                       └── Var.   ├── properties[]                 │           ├── attribute → Variable
                                  │    └── AttributeValue          │           ├── + method_id
                                  │                                │           ├── + flag
                                  └── wss:Sample                   │           ├── + datetime_measured
                                       ├── + site_code             │           ├── + statistic
                                       ├── + medium                │           ├── + temporal_aggregation
                                       ├── + replicate             │           ├── + reported_precision
                                       └── + measurements[]        │           └── + notes
                                                                   │
                                  bertron:Attribute                └── bertron:TextValue
                                    ├── id, label                        ├── value
                                    │                                    └── value_cv_id
                                    └── wss:Variable
                                         ├── id, label (inherited)
                                         ├── + expression_basis
                                         ├── + default_unit
                                         └── + missing_value_code
```

The **Data Flow** column shows the wss-test containment hierarchy. The **BERtron**
column shows the corresponding BERtron base types and how wss-test extends each one:
`Dataset` maps to `DataCollection`, `Sample` maps to `Entity`, and `Variable` maps
to `Attribute`. The **Observations** column shows BERtron's `AttributeValue` type
tree — where `Measurement` (via `QuantityValue`) and `TextValue` live.

- **Dataset** (maps to `bertron:DataCollection`) — top-level container, adding
  `variables[]` and `samples[]`
- **Variable** (extends `bertron:Attribute`) — semantic definition of the analyte.
  Inherits `label` from Attribute to name the measured substance; adds
  expression basis, default unit, and missing value sentinel
- **Measurement** (extends `bertron:QuantityValue`) — a single observed value with
  method, QC flag, timestamp, statistic, temporal aggregation, precision, and notes
- **Sample** (maps to `bertron:Entity`) — site code, medium, replicate, and a list of measurements

## Key design choice

A variable like "dissolved oxygen" is defined **once**. Two analytical methods on the
same sample are distinguished by `method_id` on each Measurement, not by duplicating
variable definitions.

## Quick links

| Resource | Description |
|----------|-------------|
| [Schema documentation](elements/index.md) | Auto-generated class, slot, type, and enum reference |
| [Examples](examples.md) | Annotated example data showing common measurement patterns |
| [Artifacts](artifacts.md) | Downloadable JSON Schema, Excel template, SQL DDL, and Python models |
| [About](about.md) | Design rationale, tech stack, and development guide |

## Getting started

```bash
# Install dependencies
just install

# Run the test suite
just test

# Build and serve docs locally
just testdoc
```

## Technology

- [LinkML](https://linkml.io/) for schema definition
- [MkDocs](https://www.mkdocs.org/) with [Material theme](https://squidfunk.github.io/mkdocs-material/) for documentation
- [BERtron](https://github.com/ber-data/bertron-schema) common data model as the base layer
