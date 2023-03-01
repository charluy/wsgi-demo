from django.http import HttpResponse
from django.utils.timezone import now


def time(request):
    return HttpResponse(f"La hora es {now()}")


def exception_raise(request):
    raise Exception
