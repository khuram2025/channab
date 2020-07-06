from rest_framework import status
from rest_framework.response import Response


def parse_response(data, status_code=status.HTTP_200_OK, response="Ok", message="None"):
    output = {
        "Response": response,
        "Message": message,
        "Status": status_code,
        "Data": data,
    }
    return Response(data=output, status=status_code)