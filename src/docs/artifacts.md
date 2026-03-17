# Generated Artifacts

Download the generated model serializations. These are produced automatically from the
LinkML schema and reflect the current state of the wss-test data model.

## Model Serializations

| Format | Description | Download |
|--------|-------------|----------|
| JSON Schema | Validate JSON/YAML data against the schema | [wss_test.schema.json](artifacts/wss_test.schema.json) |
| Excel Spreadsheet | Workbook with a sheet per class — use as a data entry template | [wss_test.xlsx](artifacts/wss_test.xlsx) |
| SQL DDL | Relational database schema for loading into SQL databases | [wss_test.sql](artifacts/wss_test.sql) |
| Python Dataclasses | Python classes generated from the schema | [wss_test.py](artifacts/wss_test.py) |
| Pydantic Model | Pydantic v2 model for validation and serialization | [wss_test_pydantic.py](artifacts/wss_test_pydantic.py) |

## About the Excel Workbook

The Excel workbook contains one sheet for each class in the schema:

- **Dataset** — top-level dataset metadata (`id`, `name`, `description`)
- **Sample** — sample provenance (`id`, `site_code`, `medium`, `replicate`)
- **Variable** — variable definitions (`id`, `label`, `entity`, `property`, `expression_basis`, `default_unit`, `missing_value_code`)
- **Measurement** — individual measurements (`attribute`, `numeric_value`, `unit`, `method_id`, `flag`, `datetime_measured`, `statistic`, `temporal_aggregation`, `reported_precision`, `notes`)
- **Attribute** — base attribute definitions
- **QuantityValue** — base quantity values
- **AttributeValue** — abstract base (for reference)
- **TextValue** — text-typed values

Use this workbook as a template for data submission. Fill in the Variable sheet first
to define your measured variables, then populate Sample and Measurement sheets with
your data.

## About the JSON Schema

The JSON Schema can be used to validate data files programmatically:

```bash
# Validate a YAML dataset
pip install check-jsonschema
check-jsonschema --schemafile docs/artifacts/wss_test.schema.json tests/data/valid/Dataset-001.yaml
```

## About the SQL DDL

The SQL DDL creates tables matching the schema classes. This is useful for loading
validated data into a relational database for querying:

```sql
-- Tables created: Dataset, Sample, Variable, Measurement,
--                 Attribute, QuantityValue, AttributeValue, TextValue
```
