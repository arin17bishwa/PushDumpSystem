import json
import random
import time

from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Push, ResponseStatus
from .utils import get_response_status_code


@api_view(["POST"])
def store_push(request):
    try:
        body = request.data
        headers = dict(request.headers)
        query_params = request.query_params.dict()
        response_status_code = get_response_status_code()

        obj = Push.objects.create(
            content=body,
            headers=headers,
            query_params=query_params,
            response_status_code=response_status_code,
        )

        sleep_time:int=random.randint(5,15)
        time.sleep(sleep_time)

        return Response(
            {"message": "Saved successfully", "id": obj.id, "uuid": obj.uuid_key, "sleep_time": sleep_time},
            status=response_status_code,
        )

    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)


def json_pushes_view(request):

    objects_data = [
        {
            "id": obj.id,
            "created_at": obj.created_at,
            "uuid_key": obj.uuid_key,
            "response_status_code": obj.response_status_code,
            "content_json": json.dumps(obj.content, indent=2),
            "headers_json": json.dumps(obj.headers, indent=2),
            "query_json": json.dumps(obj.query_params, indent=2),
        }
        for obj in Push.objects.all()
    ]

    return render(request, "json_push_viewer_000.html", {"objects": objects_data, "status_codes": [i[0] for i in ResponseStatus.STATUS_OPTIONS]})
