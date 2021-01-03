import re
import xlrd
import datetime
from django.core.exceptions import ValidationError


def parse_website_list_xlsx(file_path):
    """
    Parse website url list from excel
    """
    rb = xlrd.open_workbook(filename=file_path)
    sheet = rb.sheet_by_index(0)

    sheet.cell_value(0, 0)
    result = list()
    validation_errors = []
    for row in range(1, sheet.nrows):
        try:
            url = sheet.row_values(row)[0]
            result.append(url)
            print(str(len(result)) + ": " + str(url))

        except (IndexError, ValueError, TypeError) as exc:
            validation_errors.append({"detail": str(exc)})

    return result, validation_errors
