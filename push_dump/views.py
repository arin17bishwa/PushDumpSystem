from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Push
from .utils import get_response_status_code


@api_view(['POST'])
def store_push(request):
    try:
        body = request.data
        headers = dict(request.headers)
        query_params = request.query_params.dict()

        obj = Push.objects.create(
            content=body,
            headers=headers,
            query_params=query_params
        )

        return Response({
            'message': 'Saved successfully',
            'id': obj.id,
            'uuid': obj.uuid_key
        }, status=get_response_status_code())

    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
