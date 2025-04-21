import uuid

from django.db import models


class Push(models.Model):
    id = models.AutoField(primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)
    content = models.JSONField()
    headers = models.JSONField()
    query_params = models.JSONField()
    response_status_code = models.IntegerField()
    uuid_key = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)

    class Meta:
        verbose_name = "Push"
        verbose_name_plural = "Pushes"
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.id}"


class ResponseStatus(models.Model):
    STATUS_OPTIONS = [
        (status_code, status_code)
        for status_code in sorted((200, 201, 401, 403, 404, 500, 502, 503))
    ]

    status_code = models.IntegerField(
        choices=STATUS_OPTIONS,
        default=STATUS_OPTIONS[0][0],
    )

    def __str__(self):
        return f"{self.status_code}"

    class Meta:
        verbose_name = "Status code"
        verbose_name_plural = "Status codes"
        ordering = ["status_code"]
