from django.core.exceptions import ValidationError

import re

# your validators here


def mobile_number_validator(value):
    if re.match(r"^\d{3} \d{3} \d{4}$", value):
        return

    raise ValidationError(
        "Enter in this format.`000 000 0000`.",
        code="invalid",
        params={"entered value": value},
    )


def postal_code_validator(value):
    if re.match(r"\d{3} \d{3}", value):
        return

    raise ValidationError(
        "Invalid Format. `000 000`",
        code="invalid",
        params={"entered value": value},
    )
