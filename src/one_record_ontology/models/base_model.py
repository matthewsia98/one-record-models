from typing import ClassVar, List, get_args, get_origin

from pydantic import AnyUrl, BaseModel, Field, computed_field
from rdflib import RDF, BNode, Graph, Literal, URIRef

from one_record_ontology.utils.graph_utils import SubjectType


class OneRecordBaseModel(BaseModel):
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

        if not hasattr(cls, "_types") or not cls._types:
            raise TypeError(
                f"{cls.__name__} must define a non-empty class attribute `_types`"
            )

    def to_graph(self) -> Graph:
        g = Graph()

        for t in self.__class__._types:
            g.add((self.subject, RDF.type, t))

        for name, field in self.__class__.model_fields.items():
            if field.annotation is None:
                raise TypeError(f"Field {name} has no annotation")

            if field.serialization_alias is None:
                continue

            origin = get_origin(field.annotation)
            args = get_args(field.annotation)

            if len(args) == 0:
                base_type = field.annotation
            elif len(args) == 1:
                base_type = args[0]
            else:
                base_type, *meta = args

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
