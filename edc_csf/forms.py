from ambition_form_validators import LumbarPunctureCsfFormValidator

from .models import LumbarPunctureCsf


class LumbarPunctureCsfForm(SubjectModelFormMixin):

    form_validator_cls = LumbarPunctureCsfFormValidator

    class Meta:
        model = LumbarPunctureCsf
        fields = "__all__"
