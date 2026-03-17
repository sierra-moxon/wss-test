# About

## wss-test: Water Sample Schema

The wss-test schema defines a structured data model for water sample measurements.
It extends the [BERtron](https://github.com/ber-data/bertron-schema) common data model
types (Attribute, QuantityValue) with environmental measurement provenance and
variable semantics.

## Core Idea

**BERtron defines the value containers; wss-test adds measurement provenance.**

The schema inherits base types from BERtron and extends them:

- **Variable** (extends `bertron:Attribute`) — semantic definition of what is being measured,
  adding `entity`, `property`, `expression_basis`, and `default_unit`
- **Measurement** (extends `bertron:QuantityValue`) — a single measured value with full
  provenance, adding `method_id`, `flag`, `datetime_measured`, `statistic`,
  `temporal_aggregation`, `reported_precision`, and `notes`

## What Goes Where

| Concept | BERtron provides | wss-test adds |
|---------|-----------------|---------------|
| What was measured | `Attribute.label` | `Variable.entity`, `.property`, `.expression_basis` |
| How much | `QuantityValue.numeric_value`, `.unit` | — |
| How it was measured | — | `Measurement.method_id` |
| Quality | — | `Measurement.flag`, `.notes` |
| When | — | `Measurement.datetime_measured` |
| Aggregation | — | `Measurement.statistic`, `.temporal_aggregation` |
| Precision | — | `Measurement.reported_precision` |
| Sample context | Entity (`id`, `name`) | `Sample.site_code`, `.medium`, `.replicate` |

## Key Design Decision

The previous `MeasurementSpecification` class has been eliminated. It conflated two concerns:

- **What is being measured** — now captured by `Variable`, defined once per variable
- **How it was measured** — now travels with each `Measurement` via `method_id`

This means you define "dissolved oxygen" once as a Variable, not once per analytical method.
Two DO methods on the same sample are distinguishable by `method_id`, not by duplicating
variable definitions.

## Technology Stack

- [LinkML](https://linkml.io/) — Linked Data Modeling Language for schema definition
- [MkDocs](https://www.mkdocs.org/) with [Material theme](https://squidfunk.github.io/mkdocs-material/) for documentation
- Python for data validation and transformation

## Development

### Prerequisites

- Python 3.10+
- [uv](https://docs.astral.sh/uv/) for package management
- [just](https://github.com/casey/just/) for running commands

### Quick Start

```bash
# Install dependencies
just install

# Generate documentation
just gen-doc

# Run local documentation server
just testdoc

# Run all tests
just test
```

### Project Structure

```
wss-demo/
├── src/
│   ├── docs/                    # Documentation source files
│   └── wss_test/
│       ├── schema/              # LinkML schema definition
│       └── datamodel/           # Generated Python models
├── docs/                        # Generated documentation (do not edit)
├── project/                     # Generated artifacts
├── tests/
│   └── data/                    # Test data files
└── examples/                    # Usage examples
```

## License

This project is released under the [MIT License](https://opensource.org/licenses/MIT).

## Acknowledgments

This project uses the [linkml-project-copier](https://github.com/dalito/linkml-project-copier)
template for project structure and build tooling.

## Contact

For questions or feedback, please open an issue on the
[GitHub repository](https://github.com/sierra-moxon/wss-test/issues).
