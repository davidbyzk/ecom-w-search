from elasticsearch_dsl import DocType
from elasticsearch_dsl import Long
from elasticsearch_dsl import Text


class ESProduct(DocType):
    name = Text(required=True)
    description = Text()
    price = Long(required=True)

    category = Text(required=True, index="not_analyzed")
    tags = Text(multi=True)

    class Meta:
        doc_type = 'products'