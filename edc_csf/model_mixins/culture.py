from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.db.models import PROTECT
from edc_lab.utils import get_requisition_model_name
from edc_model.models import datetime_not_future


class CultureModelMixin(models.Model):

    """add a requisition fields if needed, for example:

    qc_requisition = models.ForeignKey(
        get_requisition_model_name(),
        on_delete=PROTECT,
        related_name="qcrequisition",
        verbose_name="QC Requisition",
        null=True,
        blank=True,
        help_text="Start typing the requisition identifier or select one from this visit")
    """

    qc_assay_datetime = models.DateTimeField(
        verbose_name="QC Result Report Date and Time",
        validators=[datetime_not_future],
        blank=True,
        null=True,
    )

    quantitative_culture = models.IntegerField(
        blank=True,
        null=True,
        validators=[MinValueValidator(0), MaxValueValidator(100_000_000)],
        help_text="Units CFU/ml",
    )

    class Meta:
        abstract = True
