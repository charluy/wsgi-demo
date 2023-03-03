from django.http import HttpResponse
from django.utils.timezone import now
from pprint import pprint


def time(request):

    # Preparo body de la response HTTP:
    str_time = now().strftime("%m/%d/%Y %H:%M:%S")
    str_response = f"{str_time} - Respuesta desde Django!\n"

    # Contenido de la request HTTP:
    print("\nRequest HTTP Content:\n")
    pprint(request)
    print("\n\n")

    return HttpResponse(str_response)


def exception_raise(request):
    raise Exception
