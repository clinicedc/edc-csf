from django.contrib import admin
from edc_model_admin import SimpleHistoryAdmin, audit_fieldset_tuple
from edc_model_admin.dashboard import ModelAdminSubjectDashboardMixin

from .admin_site import edc_csf_admin
from .fieldsets import get_csf_fieldset, get_culture_fieldset, get_lp_fieldset
from .forms import LumbarPunctureCsfForm
from .models import LumbarPunctureCsf


@admin.register(LumbarPunctureCsf, site=edc_csf_admin)
class LumbarPunctureCsfAdmin(ModelAdminSubjectDashboardMixin, SimpleHistoryAdmin):

    form = LumbarPunctureCsfForm

    autocomplete_fields = ["qc_requisition", "csf_requisition"]

    fieldsets = (
        (
            None,
            {
                "fields": (
                    "subject_identifier",
                    "report_datetime",
                )
            },
        ),
        get_lp_fieldset(),
        get_culture_fieldset(),
        get_csf_fieldset(),
        audit_fieldset_tuple,
    )

    radio_fields = {
        "reason_for_lp": admin.VERTICAL,
        "csf_culture": admin.VERTICAL,
        "india_ink": admin.VERTICAL,
        "csf_cr_ag": admin.VERTICAL,
        "csf_cr_ag_lfa": admin.VERTICAL,
        "differential_lymphocyte_unit": admin.VERTICAL,
        "differential_neutrophil_unit": admin.VERTICAL,
        "csf_glucose_units": admin.VERTICAL,
        "bios_crag": admin.VERTICAL,
        "crag_control_result": admin.VERTICAL,
        "crag_t1_result": admin.VERTICAL,
        "crag_t2_result": admin.VERTICAL,
    }

    list_display = ("lp_datetime", "reason_for_lp")

    list_filter = ("lp_datetime", "reason_for_lp")
