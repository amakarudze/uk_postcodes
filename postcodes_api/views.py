import csv
import re

from django.shortcuts import HttpResponse


def validate_postcode(request, code):
    # Format postcode into uppercase
    postcode = code.upper()

    if len(postcode) < 5 or len(postcode) > 8:
        return HttpResponse(f"Invalid postcode - {postcode}.")

    pattern = r"[A-Z]"
    if re.match(pattern, postcode[1]):
        filename = postcode[:2].lower() + ".csv"
    else:
        filename = postcode[0].lower() + ".csv"

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
    try:
        with open(f"Data/CSV/{filename}") as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=",")
            for row in csv_reader:
                if postcode or formatted_postcode in row:
                    message = f"{formatted_postcode} is a valid UK postcode."

                    return HttpResponse(message)

                else:
                    return HttpResponse(f"Invalid postcode - {postcode}.")
    except FileNotFoundError:
        return HttpResponse(f"Invalid postcode - {postcode}.")
