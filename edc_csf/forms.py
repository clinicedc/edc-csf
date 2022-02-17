from django import forms
from edc_form_validators import FormValidatorMixin
from edc_sites.forms import SiteModelFormMixin

from .form_validators import LumbarPunctureCsfFormValidator
from .models import LumbarPunctureCsf


class LumbarPunctureCsfForm(SiteModelFormMixin, FormValidatorMixin, forms.ModelForm):

    form_validator_cls = LumbarPunctureCsfFormValidator

    class Meta:
        model = LumbarPunctureCsf
        fields = "__all__"
