from django.core.exceptions import ValidationError

import re


def mobile_number_validator(value: str):
    if not re.match(r"^\+91\-[9876]\d{2}\-\d{3}\-\d{4}$", value):
        raise ValidationError(
            "provide '+91-000-000-0000' in this format.",
            params={"value": value},
        )
