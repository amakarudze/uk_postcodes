import re

from django.shortcuts import HttpResponse


def validate_postcode(request, code):
    # Format postcode into uppercase
    postcode = code.upper()
    print(postcode)
    if len(postcode) < 5 or len(postcode) > 8:
        raise ValueError(f"Invalid postcode - {postcode}.")

    pattern = r"^(([A-Z]{1,2}[0-9][A-Z0-9]?|ASCN|STHL|TDCU|BBND|[BFS]IQQ|PCRN|TKCA) " \
              r"?[0-9][A-Z]{2}|BFPO ?[0-9]{1,4}|(KY[0-9]|MSR|VG|AI)[ -]?[0-9]{4}|[A-Z]{2} " \
              r"?[0-9]{2}|GE ?CX|GIR ?0A{2}|SAN ?TA1)$"

    if re.match(pattern, postcode):
        # Check for whitespace between outer and inner parts and add one if absent
        if postcode[-4] == " ":
            formatted_postcode = postcode
        else:
            if len(postcode) == 5:
                formatted_postcode = postcode[:2] + " " + postcode[2:]
            elif len(postcode) == 6:
                formatted_postcode = postcode[:3] + " " + postcode[3:]
            elif len(postcode) == 7:
                formatted_postcode = postcode[:4] + " " + postcode[4:]
            else:
                raise ValueError("Invalid postcode.")

        message = f"{formatted_postcode} is a valid UK postcode."

        return HttpResponse(message)
    else:
        raise ValueError(f"Invalid postcode - {postcode}.")
