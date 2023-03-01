from pprint import pprint


def app(environ, start_response):
    data = b"Hellooo, World!\n"
    pprint(environ)
    start_response("200 OK", [
        ("Content-Type", "text/plain"),
        ("Content-Length", str(len(data)))
    ])

    # raise Exception

    return iter([data])
