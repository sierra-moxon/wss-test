from __future__ import annotations

import re
import sys
from datetime import (
    date,
    datetime,
    time
)
from decimal import Decimal
from enum import Enum
from typing import (
    Any,
    ClassVar,
    Literal,
    Optional,
    Union
)

from pydantic import (
    BaseModel,
    ConfigDict,
    Field,
    RootModel,
    SerializationInfo,
    SerializerFunctionWrapHandler,
    field_validator,
    model_serializer
)


metamodel_version = "1.7.0"
version = "None"


class ConfiguredBaseModel(BaseModel):
    model_config = ConfigDict(
        serialize_by_alias = True,
        validate_by_name = True,
        validate_assignment = True,
        validate_default = True,
        extra = "forbid",
        arbitrary_types_allowed = True,
        use_enum_values = True,
        strict = False,
    )





class LinkMLMeta(RootModel):
    root: dict[str, Any] = {}
    model_config = ConfigDict(frozen=True)

    def __getattr__(self, key:str):
        return getattr(self.root, key)

    def __getitem__(self, key:str):
        return self.root[key]

    def __setitem__(self, key:str, value):
        self.root[key] = value

    def __contains__(self, key:str) -> bool:
        return key in self.root


linkml_meta = LinkMLMeta({'default_prefix': 'wss_test',
     'default_range': 'string',
     'description': 'Schema for water sample measurements.\n'
                    'Extends BERtron common data model types (Attribute, '
                    'QuantityValue)\n'
                    'with environmental measurement provenance and variable '
                    'semantics.',
     'id': 'https://w3id.org/sierra-moxon/wss-test',
     'imports': ['linkml:types'],
     'license': 'MIT',
     'name': 'wss-test',
     'prefixes': {'ENVO': {'prefix_prefix': 'ENVO',
                           'prefix_reference': 'http://purl.obolibrary.org/obo/ENVO_'},
                  'UO': {'prefix_prefix': 'UO',
                         'prefix_reference': 'http://purl.obolibrary.org/obo/UO_'},
                  'bertron': {'prefix_prefix': 'bertron',
                              'prefix_reference': 'https://w3id.org/ber-data/bertron-schema/'},
                  'linkml': {'prefix_prefix': 'linkml',
                             'prefix_reference': 'https://w3id.org/linkml/'},
                  'nmdc': {'prefix_prefix': 'nmdc',
                           'prefix_reference': 'https://w3id.org/nmdc/'},
                  'qud': {'prefix_prefix': 'qud',
                          'prefix_reference': 'http://qudt.org/1.1/schema/qudt#'},
                  'schema': {'prefix_prefix': 'schema',
                             'prefix_reference': 'http://schema.org/'},
                  'wss_test': {'prefix_prefix': 'wss_test',
                               'prefix_reference': 'https://w3id.org/sierra-moxon/wss-test/'}},
     'see_also': ['https://sierra-moxon.github.io/wss-test'],
     'source_file': 'src/wss_test/schema/wss_test.yaml',
     'title': 'wss-test'} )


class Dataset(ConfiguredBaseModel):
    """
    A collection of samples representing a coherent data delivery or analytical campaign.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/sierra-moxon/wss-test', 'tree_root': True})

    id: str = Field(default=..., description="""A unique identifier.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Dataset', 'Sample', 'Attribute']} })
    name: Optional[str] = Field(default=None, description="""A human-readable name.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Dataset', 'Sample']} })
    description: Optional[str] = Field(default=None, description="""A free-text description.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Dataset']} })
    variables: Optional[list[Variable]] = Field(default=None, description="""Variable definitions used by measurements in this dataset.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Dataset']} })
    samples: Optional[list[Sample]] = Field(default=None, description="""The samples included in this dataset.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Dataset']} })


class Sample(ConfiguredBaseModel):
    """
    A physical sample collected for analysis, identified by site, medium, and replicate.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/sierra-moxon/wss-test'})

    id: str = Field(default=..., description="""A unique identifier.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Dataset', 'Sample', 'Attribute']} })
    name: Optional[str] = Field(default=None, description="""A human-readable name.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Dataset', 'Sample']} })
    site_code: Optional[str] = Field(default=None, description="""Code identifying the sampling site (e.g. CM_003, CM_004).""", json_schema_extra = { "linkml_meta": {'domain_of': ['Sample']} })
    medium: Optional[str] = Field(default=None, description="""The environmental medium or matrix sampled (e.g. OCN for ocean water).""", json_schema_extra = { "linkml_meta": {'domain_of': ['Sample']} })
    replicate: Optional[int] = Field(default=None, description="""Replicate number within a site and medium.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Sample']} })
    measurements: Optional[list[Measurement]] = Field(default=None, description="""The measurements performed on this sample.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Sample']} })


class AttributeValue(ConfiguredBaseModel):
    """
    The value for any value of attribute for an entity. This object can hold both the un-normalized atomic value and the structured value.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'abstract': True,
         'class_uri': 'nmdc:AttributeValue',
         'from_schema': 'https://w3id.org/sierra-moxon/wss-test',
         'mappings': ['bertron:AttributeValue']})

    attribute: str = Field(default=..., description="""The attribute being represented.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AttributeValue'], 'mappings': ['bertron:attribute']} })
    raw_value: Optional[str] = Field(default=None, description="""The value that was specified for an annotation in raw form, i.e. a string. E.g. \"2 cm\" or \"2-4 cm\"""", json_schema_extra = { "linkml_meta": {'domain_of': ['AttributeValue'],
         'mappings': ['nmdc:raw_value', 'bertron:raw_value']} })


class Attribute(ConfiguredBaseModel):
    """
    A domain, measurement, attribute, property, or any descriptor for additional properties.  Where available, please use OBO Foundry ontologies or other controlled vocabularies for attributes.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/sierra-moxon/wss-test',
         'mappings': ['bertron:Attribute']})

    id: str = Field(default=..., description="""A unique identifier.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Dataset', 'Sample', 'Attribute']} })
    label: str = Field(default=..., description="""Text string to describe the attribute.""", json_schema_extra = { "linkml_meta": {'aliases': ['title'], 'domain_of': ['Attribute']} })


class QuantityValue(AttributeValue):
    """
    A simple quantity, e.g. 2cm.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'nmdc:QuantityValue',
         'from_schema': 'https://w3id.org/sierra-moxon/wss-test',
         'mappings': ['schema:QuantityValue', 'bertron:QuantityValue']})

    numeric_value: Optional[float] = Field(default=None, description="""The numerical part of a quantity value.""", json_schema_extra = { "linkml_meta": {'aliases': ['result_value'],
         'domain_of': ['QuantityValue'],
         'mappings': ['nmdc:numeric_value',
                      'qud:quantityValue',
                      'schema:value',
                      'bertron:numeric_value']} })
    unit: Optional[str] = Field(default=None, description="""Unit of measurement, ideally as a Unit Ontology CURIE.""", json_schema_extra = { "linkml_meta": {'domain_of': ['QuantityValue'],
         'mappings': ['nmdc:unit',
                      'qud:unit',
                      'schema:unitCode',
                      'UO:0000000',
                      'bertron:unit']} })
    unit_cv_id: Optional[str] = Field(default=None, description="""The unit of the quantity, expressed as a CURIE from the Unit Ontology.""", json_schema_extra = { "linkml_meta": {'domain_of': ['QuantityValue'], 'mappings': ['bertron:unit_cv_id']} })
    attribute: str = Field(default=..., description="""The attribute being represented.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AttributeValue'], 'mappings': ['bertron:attribute']} })
    raw_value: Optional[str] = Field(default=None, description="""The value that was specified for an annotation in raw form, i.e. a string. E.g. \"2 cm\" or \"2-4 cm\"""", json_schema_extra = { "linkml_meta": {'domain_of': ['AttributeValue'],
         'mappings': ['nmdc:raw_value', 'bertron:raw_value']} })


class TextValue(AttributeValue):
    """
    A quality, described using a text string.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'nmdc:TextValue',
         'from_schema': 'https://w3id.org/sierra-moxon/wss-test',
         'mappings': ['bertron:TextValue']})

    value: Optional[str] = Field(default=None, description="""The value, as a text string.""", json_schema_extra = { "linkml_meta": {'domain_of': ['TextValue'], 'mappings': ['bertron:value']} })
    value_cv_id: Optional[str] = Field(default=None, description="""For values that are in a controlled vocabulary (CV), this attribute should capture the controlled vocabulary ID for the value.""", json_schema_extra = { "linkml_meta": {'domain_of': ['TextValue'], 'mappings': ['bertron:value_cv_id']} })
    attribute: str = Field(default=..., description="""The attribute being represented.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AttributeValue'], 'mappings': ['bertron:attribute']} })
    raw_value: Optional[str] = Field(default=None, description="""The value that was specified for an annotation in raw form, i.e. a string. E.g. \"2 cm\" or \"2-4 cm\"""", json_schema_extra = { "linkml_meta": {'domain_of': ['AttributeValue'],
         'mappings': ['nmdc:raw_value', 'bertron:raw_value']} })


class Variable(Attribute):
    """
    Semantic definition of a measured environmental variable. Extends bertron Attribute with structured variable metadata (entity, property, expression basis).  Defined once per variable and referenced by Measurements.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/sierra-moxon/wss-test',
         'slot_usage': {'id': {'description': 'Canonical identifier for this variable '
                                              '(e.g. carbon_dissolved_organic).',
                               'identifier': True,
                               'name': 'id',
                               'required': True}}})

    entity: Optional[str] = Field(default=None, description="""The substance or thing being measured (e.g. dissolved organic carbon).""", json_schema_extra = { "linkml_meta": {'domain_of': ['Variable']} })
    property: Optional[str] = Field(default=None, description="""The property being measured (e.g. concentration).""", json_schema_extra = { "linkml_meta": {'domain_of': ['Variable']} })
    expression_basis: Optional[str] = Field(default=None, description="""The chemical expression basis (e.g. as dissolved carbon).""", json_schema_extra = { "linkml_meta": {'domain_of': ['Variable']} })
    default_unit: Optional[str] = Field(default=None, description="""Default unit for this variable, ideally as a Unit Ontology CURIE.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Variable']} })
    missing_value_code: Optional[int] = Field(default=None, description="""The sentinel value used to represent missing data for this variable.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Variable']} })
    id: str = Field(default=..., description="""Canonical identifier for this variable (e.g. carbon_dissolved_organic).""", json_schema_extra = { "linkml_meta": {'domain_of': ['Dataset', 'Sample', 'Attribute']} })
    label: str = Field(default=..., description="""Text string to describe the attribute.""", json_schema_extra = { "linkml_meta": {'aliases': ['title'], 'domain_of': ['Attribute']} })


class Measurement(QuantityValue):
    """
    A single measured value for a variable on a sample, with full provenance including method, QC flags, timestamps, and aggregation metadata.  Extends bertron QuantityValue with measurement-specific context.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/sierra-moxon/wss-test',
         'slot_usage': {'attribute': {'description': 'The variable being measured, as '
                                                     'a reference to a Variable '
                                                     'definition.',
                                      'name': 'attribute',
                                      'range': 'Variable'},
                        'numeric_value': {'aliases': ['result_value'],
                                          'name': 'numeric_value',
                                          'required': True},
                        'unit': {'name': 'unit', 'required': True}}})

    method_id: Optional[str] = Field(default=None, description="""Identifier for the analytical method used to produce the measurement.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Measurement']} })
    flag: Optional[str] = Field(default=None, description="""Quality assurance flag associated with the measurement.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Measurement']} })
    datetime_measured: Optional[datetime ] = Field(default=None, description="""Date and time when the measurement was taken.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Measurement']} })
    statistic: Optional[str] = Field(default=None, description="""The summary statistic applied to the measurement, if any (e.g. mean, median).""", json_schema_extra = { "linkml_meta": {'domain_of': ['Measurement']} })
    temporal_aggregation: Optional[str] = Field(default=None, description="""The time interval over which the statistic was aggregated (e.g. daily, 15-min).""", json_schema_extra = { "linkml_meta": {'domain_of': ['Measurement']} })
    reported_precision: Optional[float] = Field(default=None, description="""The precision of the reported result value.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Measurement']} })
    notes: Optional[str] = Field(default=None, description="""Free-text notes about the measurement.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Measurement']} })
    numeric_value: float = Field(default=..., description="""The numerical part of a quantity value.""", json_schema_extra = { "linkml_meta": {'aliases': ['result_value'],
         'domain_of': ['QuantityValue'],
         'mappings': ['nmdc:numeric_value',
                      'qud:quantityValue',
                      'schema:value',
                      'bertron:numeric_value']} })
    unit: str = Field(default=..., description="""Unit of measurement, ideally as a Unit Ontology CURIE.""", json_schema_extra = { "linkml_meta": {'domain_of': ['QuantityValue'],
         'mappings': ['nmdc:unit',
                      'qud:unit',
                      'schema:unitCode',
                      'UO:0000000',
                      'bertron:unit']} })
    unit_cv_id: Optional[str] = Field(default=None, description="""The unit of the quantity, expressed as a CURIE from the Unit Ontology.""", json_schema_extra = { "linkml_meta": {'domain_of': ['QuantityValue'], 'mappings': ['bertron:unit_cv_id']} })
    attribute: str = Field(default=..., description="""The variable being measured, as a reference to a Variable definition.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AttributeValue'], 'mappings': ['bertron:attribute']} })
    raw_value: Optional[str] = Field(default=None, description="""The value that was specified for an annotation in raw form, i.e. a string. E.g. \"2 cm\" or \"2-4 cm\"""", json_schema_extra = { "linkml_meta": {'domain_of': ['AttributeValue'],
         'mappings': ['nmdc:raw_value', 'bertron:raw_value']} })


# Model rebuild
# see https://pydantic-docs.helpmanual.io/usage/models/#rebuilding-a-model
Dataset.model_rebuild()
Sample.model_rebuild()
AttributeValue.model_rebuild()
Attribute.model_rebuild()
QuantityValue.model_rebuild()
TextValue.model_rebuild()
Variable.model_rebuild()
Measurement.model_rebuild()
