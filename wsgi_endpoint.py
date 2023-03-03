from pprint import pprint
from datetime import datetime


def application(environ, start_response):

    # Preparo body de la response HTTP:
    str_time = datetime.now().strftime("%m/%d/%Y %H:%M:%S")
    str_response = f"{str_time} - Respuesta desde un script de Python!\n"
    data = bytes(str_response, 'utf-8')

    # Contenido de la request HTTP:
    print("\nRequest HTTP Content:\n")
    pprint(environ)
    print("\n\n")

    # Respuesta:
    start_response("200 OK", [
        ("Content-Type", "text/plain"),
        ("Content-Length", str(len(data)))
    ])

    return iter([data])
