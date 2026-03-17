-- # Class: Dataset Description: A collection of samples representing a coherent data delivery or analytical campaign.
--     * Slot: id Description: A unique identifier.
--     * Slot: name Description: A human-readable name.
--     * Slot: description Description: A free-text description.
-- # Class: Sample Description: A physical sample collected for analysis, identified by site, medium, and replicate.
--     * Slot: id Description: A unique identifier.
--     * Slot: name Description: A human-readable name.
--     * Slot: site_code Description: Code identifying the sampling site (e.g. CM_003, CM_004).
--     * Slot: medium Description: The environmental medium or matrix sampled (e.g. OCN for ocean water).
--     * Slot: replicate Description: Replicate number within a site and medium.
--     * Slot: Dataset_id Description: Autocreated FK slot
-- # Abstract Class: AttributeValue Description: The value for any value of attribute for an entity. This object can hold both the un-normalized atomic value and the structured value.
--     * Slot: id
--     * Slot: attribute Description: The attribute being represented.
--     * Slot: raw_value Description: The value that was specified for an annotation in raw form, i.e. a string. E.g. "2 cm" or "2-4 cm"
-- # Class: Attribute Description: A domain, measurement, attribute, property, or any descriptor for additional properties.  Where available, please use OBO Foundry ontologies or other controlled vocabularies for attributes.
--     * Slot: id Description: A unique identifier.
--     * Slot: label Description: Text string to describe the attribute.
-- # Class: QuantityValue Description: A simple quantity, e.g. 2cm.
--     * Slot: id
--     * Slot: numeric_value Description: The numerical part of a quantity value.
--     * Slot: unit Description: Unit of measurement, ideally as a Unit Ontology CURIE.
--     * Slot: unit_cv_id Description: The unit of the quantity, expressed as a CURIE from the Unit Ontology.
--     * Slot: attribute Description: The attribute being represented.
--     * Slot: raw_value Description: The value that was specified for an annotation in raw form, i.e. a string. E.g. "2 cm" or "2-4 cm"
-- # Class: TextValue Description: A quality, described using a text string.
--     * Slot: id
--     * Slot: value Description: The value, as a text string.
--     * Slot: value_cv_id Description: For values that are in a controlled vocabulary (CV), this attribute should capture the controlled vocabulary ID for the value.
--     * Slot: attribute Description: The attribute being represented.
--     * Slot: raw_value Description: The value that was specified for an annotation in raw form, i.e. a string. E.g. "2 cm" or "2-4 cm"
-- # Class: Variable Description: Semantic definition of a measured environmental variable. Extends bertron Attribute with structured variable metadata (entity, property, expression basis).  Defined once per variable and referenced by Measurements.
--     * Slot: entity Description: The substance or thing being measured (e.g. dissolved organic carbon).
--     * Slot: property Description: The property being measured (e.g. concentration).
--     * Slot: expression_basis Description: The chemical expression basis (e.g. as dissolved carbon).
--     * Slot: default_unit Description: Default unit for this variable, ideally as a Unit Ontology CURIE.
--     * Slot: missing_value_code Description: The sentinel value used to represent missing data for this variable.
--     * Slot: id Description: Canonical identifier for this variable (e.g. carbon_dissolved_organic).
--     * Slot: label Description: Text string to describe the attribute.
--     * Slot: Dataset_id Description: Autocreated FK slot
-- # Class: Measurement Description: A single measured value for a variable on a sample, with full provenance including method, QC flags, timestamps, and aggregation metadata.  Extends bertron QuantityValue with measurement-specific context.
--     * Slot: id
--     * Slot: method_id Description: Identifier for the analytical method used to produce the measurement.
--     * Slot: flag Description: Quality assurance flag associated with the measurement.
--     * Slot: datetime_measured Description: Date and time when the measurement was taken.
--     * Slot: statistic Description: The summary statistic applied to the measurement, if any (e.g. mean, median).
--     * Slot: temporal_aggregation Description: The time interval over which the statistic was aggregated (e.g. daily, 15-min).
--     * Slot: reported_precision Description: The precision of the reported result value.
--     * Slot: notes Description: Free-text notes about the measurement.
--     * Slot: numeric_value Description: The numerical part of a quantity value.
--     * Slot: unit Description: Unit of measurement, ideally as a Unit Ontology CURIE.
--     * Slot: unit_cv_id Description: The unit of the quantity, expressed as a CURIE from the Unit Ontology.
--     * Slot: attribute Description: The variable being measured, as a reference to a Variable definition.
--     * Slot: raw_value Description: The value that was specified for an annotation in raw form, i.e. a string. E.g. "2 cm" or "2-4 cm"
--     * Slot: Sample_id Description: Autocreated FK slot

CREATE TABLE "Dataset" (
	id TEXT NOT NULL,
	name TEXT,
	description TEXT,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_Dataset_id" ON "Dataset" (id);

CREATE TABLE "Attribute" (
	id TEXT NOT NULL,
	label TEXT NOT NULL,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_Attribute_id" ON "Attribute" (id);

CREATE TABLE "Sample" (
	id TEXT NOT NULL,
	name TEXT,
	site_code TEXT,
	medium TEXT,
	replicate INTEGER,
	"Dataset_id" TEXT,
	PRIMARY KEY (id),
	FOREIGN KEY("Dataset_id") REFERENCES "Dataset" (id)
);
CREATE INDEX "ix_Sample_id" ON "Sample" (id);

CREATE TABLE "AttributeValue" (
	id INTEGER NOT NULL,
	attribute TEXT NOT NULL,
	raw_value TEXT,
	PRIMARY KEY (id),
	FOREIGN KEY(attribute) REFERENCES "Attribute" (id)
);
CREATE INDEX "ix_AttributeValue_id" ON "AttributeValue" (id);

CREATE TABLE "QuantityValue" (
	id INTEGER NOT NULL,
	numeric_value FLOAT,
	unit TEXT,
	unit_cv_id TEXT,
	attribute TEXT NOT NULL,
	raw_value TEXT,
	PRIMARY KEY (id),
	FOREIGN KEY(attribute) REFERENCES "Attribute" (id)
);
CREATE INDEX "ix_QuantityValue_id" ON "QuantityValue" (id);

CREATE TABLE "TextValue" (
	id INTEGER NOT NULL,
	value TEXT,
	value_cv_id TEXT,
	attribute TEXT NOT NULL,
	raw_value TEXT,
	PRIMARY KEY (id),
	FOREIGN KEY(attribute) REFERENCES "Attribute" (id)
);
CREATE INDEX "ix_TextValue_id" ON "TextValue" (id);

CREATE TABLE "Variable" (
	entity TEXT,
	property TEXT,
	expression_basis TEXT,
	default_unit TEXT,
	missing_value_code INTEGER,
	id TEXT NOT NULL,
	label TEXT NOT NULL,
	"Dataset_id" TEXT,
	PRIMARY KEY (id),
	FOREIGN KEY("Dataset_id") REFERENCES "Dataset" (id)
);
CREATE INDEX "ix_Variable_id" ON "Variable" (id);

CREATE TABLE "Measurement" (
	id INTEGER NOT NULL,
	method_id TEXT,
	flag TEXT,
	datetime_measured DATETIME,
	statistic TEXT,
	temporal_aggregation TEXT,
	reported_precision FLOAT,
	notes TEXT,
	numeric_value FLOAT NOT NULL,
	unit TEXT NOT NULL,
	unit_cv_id TEXT,
	attribute TEXT NOT NULL,
	raw_value TEXT,
	"Sample_id" TEXT,
	PRIMARY KEY (id),
	FOREIGN KEY(attribute) REFERENCES "Variable" (id),
	FOREIGN KEY("Sample_id") REFERENCES "Sample" (id)
);
CREATE INDEX "ix_Measurement_id" ON "Measurement" (id);
