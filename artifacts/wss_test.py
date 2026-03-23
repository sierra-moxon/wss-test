# Auto generated from wss_test.yaml by pythongen.py version: 0.0.1
# Generation date: 2026-03-23T22:18:33
# Schema: wss-test
#
# id: https://w3id.org/sierra-moxon/wss-test
# description: Schema for water sample measurements.
#   Extends BERtron common data model types (Attribute, QuantityValue)
#   with environmental measurement provenance and variable semantics.
# license: MIT

import dataclasses
import re
from dataclasses import dataclass
from datetime import (
    date,
    datetime,
    time
)
from typing import (
    Any,
    ClassVar,
    Dict,
    List,
    Optional,
    Union
)

from jsonasobj2 import (
    JsonObj,
    as_dict
)
from linkml_runtime.linkml_model.meta import (
    EnumDefinition,
    PermissibleValue,
    PvFormulaOptions
)
from linkml_runtime.utils.curienamespace import CurieNamespace
from linkml_runtime.utils.enumerations import EnumDefinitionImpl
from linkml_runtime.utils.formatutils import (
    camelcase,
    sfx,
    underscore
)
from linkml_runtime.utils.metamodelcore import (
    bnode,
    empty_dict,
    empty_list
)
from linkml_runtime.utils.slot import Slot
from linkml_runtime.utils.yamlutils import (
    YAMLRoot,
    extended_float,
    extended_int,
    extended_str
)
from rdflib import (
    Namespace,
    URIRef
)

from linkml_runtime.linkml_model.types import Datetime, Float, Integer, String, Uriorcurie
from linkml_runtime.utils.metamodelcore import URIorCURIE, XSDDateTime

metamodel_version = "1.7.0"
version = None

# Namespaces
ENVO = CurieNamespace('ENVO', 'http://purl.obolibrary.org/obo/ENVO_')
UO = CurieNamespace('UO', 'http://purl.obolibrary.org/obo/UO_')
BERTRON = CurieNamespace('bertron', 'https://w3id.org/ber-data/bertron-schema/')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
NMDC = CurieNamespace('nmdc', 'https://w3id.org/nmdc/')
QUD = CurieNamespace('qud', 'http://qudt.org/1.1/schema/qudt#')
SCHEMA = CurieNamespace('schema', 'http://schema.org/')
WSS_TEST = CurieNamespace('wss_test', 'https://w3id.org/sierra-moxon/wss-test/')
DEFAULT_ = WSS_TEST


# Types

# Class references
class DatasetId(extended_str):
    pass


class SampleId(extended_str):
    pass


class AttributeId(extended_str):
    pass


class VariableId(AttributeId):
    pass


@dataclass(repr=False)
class Dataset(YAMLRoot):
    """
    A collection of samples representing a coherent data delivery or analytical campaign.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = WSS_TEST["Dataset"]
    class_class_curie: ClassVar[str] = "wss_test:Dataset"
    class_name: ClassVar[str] = "Dataset"
    class_model_uri: ClassVar[URIRef] = WSS_TEST.Dataset

    id: Union[str, DatasetId] = None
    name: Optional[str] = None
    description: Optional[str] = None
    variables: Optional[Union[dict[Union[str, VariableId], Union[dict, "Variable"]], list[Union[dict, "Variable"]]]] = empty_dict()
    samples: Optional[Union[dict[Union[str, SampleId], Union[dict, "Sample"]], list[Union[dict, "Sample"]]]] = empty_dict()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DatasetId):
            self.id = DatasetId(self.id)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        self._normalize_inlined_as_list(slot_name="variables", slot_type=Variable, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="samples", slot_type=Sample, key_name="id", keyed=True)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Sample(YAMLRoot):
    """
    A physical sample collected for analysis, identified by site, medium, and replicate.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = WSS_TEST["Sample"]
    class_class_curie: ClassVar[str] = "wss_test:Sample"
    class_name: ClassVar[str] = "Sample"
    class_model_uri: ClassVar[URIRef] = WSS_TEST.Sample

    id: Union[str, SampleId] = None
    name: Optional[str] = None
    site_code: Optional[str] = None
    medium: Optional[str] = None
    replicate: Optional[int] = None
    measurements: Optional[Union[Union[dict, "Measurement"], list[Union[dict, "Measurement"]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, SampleId):
            self.id = SampleId(self.id)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if self.site_code is not None and not isinstance(self.site_code, str):
            self.site_code = str(self.site_code)

        if self.medium is not None and not isinstance(self.medium, str):
            self.medium = str(self.medium)

        if self.replicate is not None and not isinstance(self.replicate, int):
            self.replicate = int(self.replicate)

        self._normalize_inlined_as_list(slot_name="measurements", slot_type=Measurement, key_name="numeric_value", keyed=False)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AttributeValue(YAMLRoot):
    """
    The value for any value of attribute for an entity. This object can hold both the un-normalized atomic value and
    the structured value.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NMDC["AttributeValue"]
    class_class_curie: ClassVar[str] = "nmdc:AttributeValue"
    class_name: ClassVar[str] = "AttributeValue"
    class_model_uri: ClassVar[URIRef] = WSS_TEST.AttributeValue

    attribute: Union[str, AttributeId] = None
    raw_value: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.attribute):
            self.MissingRequiredField("attribute")
        if not isinstance(self.attribute, AttributeId):
            self.attribute = AttributeId(self.attribute)

        if self.raw_value is not None and not isinstance(self.raw_value, str):
            self.raw_value = str(self.raw_value)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Attribute(YAMLRoot):
    """
    A domain, measurement, attribute, property, or any descriptor for additional properties. Where available, please
    use OBO Foundry ontologies or other controlled vocabularies for attributes.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = WSS_TEST["Attribute"]
    class_class_curie: ClassVar[str] = "wss_test:Attribute"
    class_name: ClassVar[str] = "Attribute"
    class_model_uri: ClassVar[URIRef] = WSS_TEST.Attribute

    id: Union[str, AttributeId] = None
    label: str = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, AttributeId):
            self.id = AttributeId(self.id)

        if self._is_empty(self.label):
            self.MissingRequiredField("label")
        if not isinstance(self.label, str):
            self.label = str(self.label)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class QuantityValue(AttributeValue):
    """
    A simple quantity, e.g. 2cm.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NMDC["QuantityValue"]
    class_class_curie: ClassVar[str] = "nmdc:QuantityValue"
    class_name: ClassVar[str] = "QuantityValue"
    class_model_uri: ClassVar[URIRef] = WSS_TEST.QuantityValue

    attribute: Union[str, AttributeId] = None
    numeric_value: Optional[float] = None
    unit: Optional[str] = None
    unit_cv_id: Optional[Union[str, URIorCURIE]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.numeric_value is not None and not isinstance(self.numeric_value, float):
            self.numeric_value = float(self.numeric_value)

        if self.unit is not None and not isinstance(self.unit, str):
            self.unit = str(self.unit)

        if self.unit_cv_id is not None and not isinstance(self.unit_cv_id, URIorCURIE):
            self.unit_cv_id = URIorCURIE(self.unit_cv_id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class TextValue(AttributeValue):
    """
    A quality, described using a text string.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NMDC["TextValue"]
    class_class_curie: ClassVar[str] = "nmdc:TextValue"
    class_name: ClassVar[str] = "TextValue"
    class_model_uri: ClassVar[URIRef] = WSS_TEST.TextValue

    attribute: Union[str, AttributeId] = None
    value: Optional[str] = None
    value_cv_id: Optional[Union[str, URIorCURIE]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.value is not None and not isinstance(self.value, str):
            self.value = str(self.value)

        if self.value_cv_id is not None and not isinstance(self.value_cv_id, URIorCURIE):
            self.value_cv_id = URIorCURIE(self.value_cv_id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Variable(Attribute):
    """
    Semantic definition of a measured environmental variable. Extends bertron Attribute with structured variable
    metadata (expression basis). Defined once per variable and referenced by Measurements.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = WSS_TEST["Variable"]
    class_class_curie: ClassVar[str] = "wss_test:Variable"
    class_name: ClassVar[str] = "Variable"
    class_model_uri: ClassVar[URIRef] = WSS_TEST.Variable

    id: Union[str, VariableId] = None
    label: str = None
    expression_basis: Optional[str] = None
    default_unit: Optional[str] = None
    missing_value_code: Optional[int] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, VariableId):
            self.id = VariableId(self.id)

        if self.expression_basis is not None and not isinstance(self.expression_basis, str):
            self.expression_basis = str(self.expression_basis)

        if self.default_unit is not None and not isinstance(self.default_unit, str):
            self.default_unit = str(self.default_unit)

        if self.missing_value_code is not None and not isinstance(self.missing_value_code, int):
            self.missing_value_code = int(self.missing_value_code)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Measurement(QuantityValue):
    """
    A single measured value for a variable on a sample, with full provenance including method, QC flags, timestamps,
    and aggregation metadata. Extends bertron QuantityValue with measurement-specific context.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = WSS_TEST["Measurement"]
    class_class_curie: ClassVar[str] = "wss_test:Measurement"
    class_name: ClassVar[str] = "Measurement"
    class_model_uri: ClassVar[URIRef] = WSS_TEST.Measurement

    attribute: Union[str, VariableId] = None
    numeric_value: float = None
    unit: str = None
    method_id: Optional[str] = None
    flag: Optional[str] = None
    datetime_measured: Optional[Union[str, XSDDateTime]] = None
    statistic: Optional[str] = None
    temporal_aggregation: Optional[str] = None
    reported_precision: Optional[float] = None
    notes: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.attribute):
            self.MissingRequiredField("attribute")
        if not isinstance(self.attribute, VariableId):
            self.attribute = VariableId(self.attribute)

        if self._is_empty(self.numeric_value):
            self.MissingRequiredField("numeric_value")
        if not isinstance(self.numeric_value, float):
            self.numeric_value = float(self.numeric_value)

        if self._is_empty(self.unit):
            self.MissingRequiredField("unit")
        if not isinstance(self.unit, str):
            self.unit = str(self.unit)

        if self.method_id is not None and not isinstance(self.method_id, str):
            self.method_id = str(self.method_id)

        if self.flag is not None and not isinstance(self.flag, str):
            self.flag = str(self.flag)

        if self.datetime_measured is not None and not isinstance(self.datetime_measured, XSDDateTime):
            self.datetime_measured = XSDDateTime(self.datetime_measured)

        if self.statistic is not None and not isinstance(self.statistic, str):
            self.statistic = str(self.statistic)

        if self.temporal_aggregation is not None and not isinstance(self.temporal_aggregation, str):
            self.temporal_aggregation = str(self.temporal_aggregation)

        if self.reported_precision is not None and not isinstance(self.reported_precision, float):
            self.reported_precision = float(self.reported_precision)

        if self.notes is not None and not isinstance(self.notes, str):
            self.notes = str(self.notes)

        super().__post_init__(**kwargs)


# Enumerations


# Slots
class slots:
    pass

slots.id = Slot(uri=WSS_TEST.id, name="id", curie=WSS_TEST.curie('id'),
                   model_uri=WSS_TEST.id, domain=None, range=URIRef)

slots.name = Slot(uri=WSS_TEST.name, name="name", curie=WSS_TEST.curie('name'),
                   model_uri=WSS_TEST.name, domain=None, range=Optional[str])

slots.description = Slot(uri=WSS_TEST.description, name="description", curie=WSS_TEST.curie('description'),
                   model_uri=WSS_TEST.description, domain=None, range=Optional[str])

slots.label = Slot(uri=WSS_TEST.label, name="label", curie=WSS_TEST.curie('label'),
                   model_uri=WSS_TEST.label, domain=None, range=str)

slots.site_code = Slot(uri=WSS_TEST.site_code, name="site_code", curie=WSS_TEST.curie('site_code'),
                   model_uri=WSS_TEST.site_code, domain=None, range=Optional[str])

slots.medium = Slot(uri=WSS_TEST.medium, name="medium", curie=WSS_TEST.curie('medium'),
                   model_uri=WSS_TEST.medium, domain=None, range=Optional[str])

slots.replicate = Slot(uri=WSS_TEST.replicate, name="replicate", curie=WSS_TEST.curie('replicate'),
                   model_uri=WSS_TEST.replicate, domain=None, range=Optional[int])

slots.variables = Slot(uri=WSS_TEST.variables, name="variables", curie=WSS_TEST.curie('variables'),
                   model_uri=WSS_TEST.variables, domain=None, range=Optional[Union[dict[Union[str, VariableId], Union[dict, Variable]], list[Union[dict, Variable]]]])

slots.samples = Slot(uri=WSS_TEST.samples, name="samples", curie=WSS_TEST.curie('samples'),
                   model_uri=WSS_TEST.samples, domain=None, range=Optional[Union[dict[Union[str, SampleId], Union[dict, Sample]], list[Union[dict, Sample]]]])

slots.measurements = Slot(uri=WSS_TEST.measurements, name="measurements", curie=WSS_TEST.curie('measurements'),
                   model_uri=WSS_TEST.measurements, domain=None, range=Optional[Union[Union[dict, Measurement], list[Union[dict, Measurement]]]])

slots.attribute = Slot(uri=WSS_TEST.attribute, name="attribute", curie=WSS_TEST.curie('attribute'),
                   model_uri=WSS_TEST.attribute, domain=None, range=Union[str, AttributeId], mappings = [BERTRON["attribute"]])

slots.raw_value = Slot(uri=WSS_TEST.raw_value, name="raw_value", curie=WSS_TEST.curie('raw_value'),
                   model_uri=WSS_TEST.raw_value, domain=None, range=Optional[str], mappings = [NMDC["raw_value"], BERTRON["raw_value"]])

slots.numeric_value = Slot(uri=WSS_TEST.numeric_value, name="numeric_value", curie=WSS_TEST.curie('numeric_value'),
                   model_uri=WSS_TEST.numeric_value, domain=None, range=Optional[float], mappings = [NMDC["numeric_value"], QUD["quantityValue"], SCHEMA["value"], BERTRON["numeric_value"]])

slots.unit = Slot(uri=WSS_TEST.unit, name="unit", curie=WSS_TEST.curie('unit'),
                   model_uri=WSS_TEST.unit, domain=None, range=Optional[str], mappings = [NMDC["unit"], QUD["unit"], SCHEMA["unitCode"], UO["0000000"], BERTRON["unit"]])

slots.unit_cv_id = Slot(uri=WSS_TEST.unit_cv_id, name="unit_cv_id", curie=WSS_TEST.curie('unit_cv_id'),
                   model_uri=WSS_TEST.unit_cv_id, domain=None, range=Optional[Union[str, URIorCURIE]], mappings = [BERTRON["unit_cv_id"]])

slots.value = Slot(uri=WSS_TEST.value, name="value", curie=WSS_TEST.curie('value'),
                   model_uri=WSS_TEST.value, domain=None, range=Optional[str], mappings = [BERTRON["value"]])

slots.value_cv_id = Slot(uri=WSS_TEST.value_cv_id, name="value_cv_id", curie=WSS_TEST.curie('value_cv_id'),
                   model_uri=WSS_TEST.value_cv_id, domain=None, range=Optional[Union[str, URIorCURIE]], mappings = [BERTRON["value_cv_id"]])

slots.expression_basis = Slot(uri=WSS_TEST.expression_basis, name="expression_basis", curie=WSS_TEST.curie('expression_basis'),
                   model_uri=WSS_TEST.expression_basis, domain=None, range=Optional[str])

slots.default_unit = Slot(uri=WSS_TEST.default_unit, name="default_unit", curie=WSS_TEST.curie('default_unit'),
                   model_uri=WSS_TEST.default_unit, domain=None, range=Optional[str])

slots.missing_value_code = Slot(uri=WSS_TEST.missing_value_code, name="missing_value_code", curie=WSS_TEST.curie('missing_value_code'),
                   model_uri=WSS_TEST.missing_value_code, domain=None, range=Optional[int])

slots.method_id = Slot(uri=WSS_TEST.method_id, name="method_id", curie=WSS_TEST.curie('method_id'),
                   model_uri=WSS_TEST.method_id, domain=None, range=Optional[str])

slots.flag = Slot(uri=WSS_TEST.flag, name="flag", curie=WSS_TEST.curie('flag'),
                   model_uri=WSS_TEST.flag, domain=None, range=Optional[str])

slots.datetime_measured = Slot(uri=WSS_TEST.datetime_measured, name="datetime_measured", curie=WSS_TEST.curie('datetime_measured'),
                   model_uri=WSS_TEST.datetime_measured, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.statistic = Slot(uri=WSS_TEST.statistic, name="statistic", curie=WSS_TEST.curie('statistic'),
                   model_uri=WSS_TEST.statistic, domain=None, range=Optional[str])

slots.temporal_aggregation = Slot(uri=WSS_TEST.temporal_aggregation, name="temporal_aggregation", curie=WSS_TEST.curie('temporal_aggregation'),
                   model_uri=WSS_TEST.temporal_aggregation, domain=None, range=Optional[str])

slots.reported_precision = Slot(uri=WSS_TEST.reported_precision, name="reported_precision", curie=WSS_TEST.curie('reported_precision'),
                   model_uri=WSS_TEST.reported_precision, domain=None, range=Optional[float])

slots.notes = Slot(uri=WSS_TEST.notes, name="notes", curie=WSS_TEST.curie('notes'),
                   model_uri=WSS_TEST.notes, domain=None, range=Optional[str])

slots.Variable_id = Slot(uri=WSS_TEST.id, name="Variable_id", curie=WSS_TEST.curie('id'),
                   model_uri=WSS_TEST.Variable_id, domain=Variable, range=Union[str, VariableId])

slots.Measurement_attribute = Slot(uri=WSS_TEST.attribute, name="Measurement_attribute", curie=WSS_TEST.curie('attribute'),
                   model_uri=WSS_TEST.Measurement_attribute, domain=Measurement, range=Union[str, VariableId], mappings = [BERTRON["attribute"]])

slots.Measurement_numeric_value = Slot(uri=WSS_TEST.numeric_value, name="Measurement_numeric_value", curie=WSS_TEST.curie('numeric_value'),
                   model_uri=WSS_TEST.Measurement_numeric_value, domain=Measurement, range=float, mappings = [NMDC["numeric_value"], QUD["quantityValue"], SCHEMA["value"], BERTRON["numeric_value"]])

slots.Measurement_unit = Slot(uri=WSS_TEST.unit, name="Measurement_unit", curie=WSS_TEST.curie('unit'),
                   model_uri=WSS_TEST.Measurement_unit, domain=Measurement, range=str, mappings = [NMDC["unit"], QUD["unit"], SCHEMA["unitCode"], UO["0000000"], BERTRON["unit"]])
