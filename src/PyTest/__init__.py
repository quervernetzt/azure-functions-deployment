import logging

import azure.functions as func
import requests


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    r = requests.get('https://api.github.com/events')

    return func.HttpResponse(
             r.content,
             status_code=200
        )
