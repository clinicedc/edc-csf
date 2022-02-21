from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.utils.html import format_html
from edc_model.models import datetime_not_future

from edc_csf.choices import LP_REASON


class LpModelMixin(models.Model):

    lp_datetime = models.DateTimeField(
        verbose_name="LP Date and Time", validators=[datetime_not_future]
    )

    reason_for_lp = models.CharField(
        verbose_name="Reason for LP", max_length=50, choices=LP_REASON
    )

    opening_pressure = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(99)],
        help_text=format_html("Units cm of H<sub>2</sub>O"),
    )

    closing_pressure = models.IntegerField(
        blank=True,
        null=True,
        validators=[MinValueValidator(0), MaxValueValidator(99)],
        help_text=format_html("Units cm of H<sub>2</sub>O"),
    )

    csf_amount_removed = models.IntegerField(
        blank=True,
        null=True,
        verbose_name="CSF amount removed ",
        validators=[MinValueValidator(1)],
        help_text="Units ml",
    )

    class Meta:
        abstract = True
