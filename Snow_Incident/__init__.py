import logging
import azure.functions as func
from shared_code.classess import NewIncident


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
    incident = NewIncident().create_incident(body=req.get_body())
    logging.info(incident)
    return func.HttpResponse(
        str(incident)
    )
