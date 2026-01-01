from typing import Any, ClassVar, List, Optional, Self, Union, get_args, get_origin

from pydantic import AnyUrl, BaseModel, Field, computed_field
from rdflib import RDF, BNode, Graph, Literal, URIRef

from one_record_ontology.utils.graph_utils import SubjectType, get_root_subject


class OneRecordBaseModel(BaseModel):
    _type: ClassVar[URIRef]
    _types: ClassVar[List[URIRef]]
    subject: SubjectType = Field(default_factory=BNode, exclude=True)

    model_config = {
        "arbitrary_types_allowed": True,
        "json_schema_mode_override": "serialization",
    }

    @computed_field(alias="@id")
    def id(self) -> AnyUrl:
        if isinstance(self.subject, BNode):
            return AnyUrl(url=str(self.subject.skolemize()))

        return AnyUrl(url=str(self.subject))

    @computed_field(alias="@type")
    def types(self) -> List[AnyUrl]:
        return [AnyUrl(url=str(t)) for t in self.__class__._types]

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)

        if cls is OneRecordBaseModel:
            return  # base class itself is allowed

        if not hasattr(cls, "_type") or not cls._type:
            raise TypeError(
                f"{cls.__name__} must define a non-empty class attribute `_type`"
            )

        if not hasattr(cls, "_types") or not cls._types:
            raise TypeError(
                f"{cls.__name__} must define a non-empty class attribute `_types`"
            )

    @classmethod
    def from_graph(cls, g: Graph, subject: Optional[SubjectType] = None) -> Self:
        if subject is None:
            subject = get_root_subject(g, cls._type)

        kwargs: dict[str, Any] = {}

        for name, field in cls.model_fields.items():
            if field.annotation is None:
                raise TypeError(f"Field {name} has no annotation")

            if field.serialization_alias is None:
                continue

            annotation = field.annotation
            origin = get_origin(annotation)
            if origin is list or origin is Union:
                (base_type, *_) = get_args(annotation)
            else:
                base_type = annotation

            field_uri = URIRef(field.serialization_alias)

            if issubclass(base_type, OneRecordBaseModel):
                if origin is not list:
                    obj_node = g.value(subject, field_uri)
                    if obj_node is not None:
                        obj = base_type.from_graph(g, obj_node)
                        kwargs[name] = obj
                else:
                    objs = []
                    for obj_node in g.objects(subject, field_uri):
                        obj = base_type.from_graph(g, obj_node)
                        objs.append(obj)
                    kwargs[name] = objs
            else:
                if origin is not list:
                    value = g.value(subject, field_uri)
                    if isinstance(value, Literal):
                        kwargs[name] = value.toPython()
                else:
                    values: list[Any] = []
                    for obj in g.objects(subject, field_uri):
                        if isinstance(obj, Literal):
                            values.append(obj.toPython())
                    kwargs[name] = values

        result = cls(**kwargs)
        result.subject = subject

        return result

    def to_graph(self) -> Graph:
        g = Graph()

        for t in self.__class__._types:
            g.add((self.subject, RDF.type, t))

        for name, field in self.__class__.model_fields.items():
            if field.annotation is None:
                raise TypeError(f"Field {name} has no annotation")

            if field.serialization_alias is None:
                continue

            annotation = field.annotation
            origin = get_origin(annotation)
            if origin is list or origin is Union:
                (base_type, *_) = get_args(annotation)
            else:
                base_type = annotation

            value = getattr(self, name)

            if value is None:
                continue

            if issubclass(base_type, OneRecordBaseModel):
                objs: List[OneRecordBaseModel]
                if origin is not list:
                    objs = [value]
                else:
                    objs = value

                for obj in objs:
                    obj_graph = obj.to_graph()
                    g += obj_graph
                    g.add(
                        (
                            self.subject,
                            URIRef(field.serialization_alias),
                            obj.subject,
                        )
                    )
            else:
                if origin is not list:
                    objs = [value]
                else:
                    objs = value

                for value in objs:
                    g.add(
                        (
                            self.subject,
                            URIRef(field.serialization_alias),
                            Literal(value),
                        )
                    )

        return g
