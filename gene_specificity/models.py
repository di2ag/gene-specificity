from django.db.models import Model, CharField, DateTimeField, JSONField, FloatField, ForeignKey


class SpecificityMeanGene(Model):
    gene_curie = CharField(max_length=255)  # type: ignore
    tissue_curie = CharField(max_length=255)  # type: ignore
    specificity_mean = FloatField()  # type: ignore

    def get_result(self) -> list:
        return self.tissue_curie, "biolink:GrossAnatomicalStructure", self.specificity_mean  # type: ignore


class SpecificityMedianGene(Model):
    gene_curie = CharField(max_length=255)  # type: ignore
    tissue_curie = CharField(max_length=255)  # type: ignore
    specificity_median = FloatField()  # type: ignore

    def get_result(self) -> list:
        return self.tissue_curie, "biolink:GrossAnatomicalStructure", self.specificity_median,  # type: ignore


class SpecificityMeanTissue(Model):
    tissue_curie = CharField(max_length=255)  # type: ignore
    gene_curie = CharField(max_length=255)  # type: ignore
    specificity_mean = FloatField()  # type: ignore

    def get_result(self) -> list:
        return self.gene_curie, "biolink:Gene", self.specificity_mean  # type: ignore


class SpecificityMedianTissue(Model):
    tissue_curie = CharField(max_length=255)  # type: ignore
    gene_curie = CharField(max_length=255)  # type: ignore
    specificity_median = FloatField()  # type: ignore

    def get_result(self) -> list:
        return self.gene_curie, "biolink:Gene" , self.specificity_median  # type: ignore

class CurieTemplate(Model):
    curie = CharField(max_length=128)

class CurieTemplateMatch(Model):
    curie_template = ForeignKey(CurieTemplate, on_delete=models.CASCADE)
    curie = CharField(max_length=128)


class Transaction(Model):
    id = CharField(max_length=100, primary_key=True)  # type: ignore #noqa
    date_time = DateTimeField(auto_now=True)  # type: ignore
    query = JSONField(default=dict)
    status = CharField(max_length=100, default="", null=True)  # type: ignore
    versions = JSONField(default=dict)
    chp_app = CharField(max_length=128, null=True)  # type: ignore
