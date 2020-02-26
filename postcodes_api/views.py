import re

from django.shortcuts import HttpResponse


def validate_postcode(request, code):
    # Format postcode into uppercase
    postcode = code.upper()
    pattern = r"^(([A-Z]{1,2}[0-9][A-Z0-9]?|ASCN|STHL|TDCU|BBND|[BFS]IQQ|PCRN|TKCA) " \
              r"?[0-9][A-Z]{2}|BFPO ?[0-9]{1,4}|(KY[0-9]|MSR|VG|AI)[ -]?[0-9]{4}|[A-Z]{2} " \
              r"?[0-9]{2}|GE ?CX|GIR ?0A{2}|SAN ?TA1)$"

    if re.match(pattern, postcode):
        # Check for whitespace between outer and inner parts and add one if absent
        if postcode[-4] == " ":
            formatted_postcode = postcode
        else:
            formatted_postcode = postcode[:-4] + " " + postcode[-3:]
        return formatted_postcode
    else:
        raise ValueError("Invalid postcode.")
    formatted_postcode = None
    return HttpResponse(formatted_postcode)
