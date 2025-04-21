import uuid

from django.db import models


class Push(models.Model):
    id = models.AutoField(primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)
    content = models.JSONField()
    headers = models.JSONField()
    query_params = models.JSONField()
    uuid_key = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)


class ResponseStatus(models.Model):
    STATUS_OPTIONS = [
        (status_code, status_code)
        for status_code in sorted((200, 201, 401, 403, 404, 500, 502, 503))
    ]
    status_code = models.IntegerField(
        choices=STATUS_OPTIONS,
        default=STATUS_OPTIONS[0][0],
    )
