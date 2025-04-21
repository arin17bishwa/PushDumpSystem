from .models import ResponseStatus


def get_response_status_code():
    # gets a random(first without any ordering) status code and returns it. It is expected that only 1 of them exists.
    # If nothing exists, it returns a default value of 200
    status_code_obj = ResponseStatus.objects.first()
    print(status_code_obj.status_code)
    return status_code_obj.status_code if status_code_obj is not None else 200
