def get_lp_fieldset():
    return (
        "LP",
        {
            "fields": (
                "lp_datetime",
                "reason_for_lp",
                "opening_pressure",
                "closing_pressure",
                "csf_amount_removed",
            )
        },
    )


def get_culture_fieldset():
    return (
        "Quantitative Culture",
        {"fields": ("qc_requisition", "qc_assay_datetime", "quantitative_culture")},
    )


def get_csf_fieldset():
    return (
        "CSF",
        {
            "fields": (
                "csf_requisition",
                "csf_assay_datetime",
                "csf_culture",
                "other_csf_culture",
                "csf_wbc_cell_count",
                "differential_lymphocyte_count",
                "differential_lymphocyte_unit",
                "differential_neutrophil_count",
                "differential_neutrophil_unit",
                "india_ink",
                "csf_glucose",
                "csf_glucose_units",
                "csf_protein",
                "csf_cr_ag",
                "csf_cr_ag_lfa",
                "bios_crag",
                "crag_control_result",
                "crag_t1_result",
                "crag_t2_result",
            )
        },
    )
