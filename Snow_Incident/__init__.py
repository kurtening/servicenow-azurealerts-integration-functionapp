import logging

import azure.functions as func


def main(req: func.HttpRequest) -> func.HttpResponse:
    """Receives an HttpRequest from Alert Action Group
    with Unified Alerts Template

    Args:
        req (func.HttpRequest): HttpRequest from action group
        with this schema
        https://learn.microsoft.com/en-us/azure/azure-monitor/essentials/activity-log-schema#alert-category

    Returns:
        func.HttpResponse: HttpResponse from the function app
    """
    pass