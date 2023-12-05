from django.db.models import Model, CharField, DateTimeField, JSONField, FloatField, ForeignKey, CASCADE

class GeneToTissue(Model):
    gene_id = CharField(max_length=255, db_index=True)
    tissue_id = CharField(max_length=255)
    spec = FloatField()
    norm_spec = FloatField()
    p_val = FloatField()

    def get_result(self) -> list:
        return self.tissue_id, "biolink:GrossAnatomicalStructure", self.spec, self.norm_spec, self.p_val

class TissueToGene(Model):
    gene_id = CharField(max_length=255)
    tissue_id = CharField(max_length=255, db_index=True)
    spec = FloatField()
    norm_spec = FloatField()
    p_val = FloatField()

    def get_result(self) -> list:
        return self.gene_id, "biolink:Gene", self.spec, self.norm_spec, self.p_val


class CurieTemplate(Model):
    curie = CharField(max_length=128)

class CurieTemplateMatch(Model):
    curie_template = ForeignKey(CurieTemplate, on_delete=CASCADE)
    curie = CharField(max_length=128)


class Transaction(Model):
    id = CharField(max_length=100, primary_key=True)  # type: ignore #noqa
    date_time = DateTimeField(auto_now=True)  # type: ignore
    query = JSONField(default=dict)
    status = CharField(max_length=100, default="", null=True)  # type: ignore
    versions = JSONField(default=dict)
    chp_app = CharField(max_length=128, null=True)  # type: ignore

