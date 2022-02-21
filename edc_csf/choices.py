from edc_constants.constants import NO, NOT_DONE, YES
from edc_reportable import (
    MILLIGRAMS_PER_DECILITER,
    MILLIMOLES_PER_LITER,
    MILLIMOLES_PER_LITER_DISPLAY,
    MM3,
    MM3_DISPLAY,
)

from .constants import AWAITING_RESULTS, THERAPEUTIC_PL

YES_NO_NOT_DONE_WAIT_RESULTS = (
    (YES, YES),
    (NO, NO),
    (AWAITING_RESULTS, "Awaiting results"),
    (NOT_DONE, "Not done"),
)

LP_REASON = (
    ("scheduled_per_protocol", "Scheduled per protocol"),
    (THERAPEUTIC_PL, "Therapeutic LP"),
    ("clincal_deterioration", "Clinical deterioration"),
)

MG_MMOL_UNITS = (
    (MILLIGRAMS_PER_DECILITER, MILLIGRAMS_PER_DECILITER),
    (MILLIMOLES_PER_LITER, MILLIMOLES_PER_LITER_DISPLAY),
)


MM3_PERC_UNITS = ((MM3, MM3_DISPLAY), ("%", "%"))
