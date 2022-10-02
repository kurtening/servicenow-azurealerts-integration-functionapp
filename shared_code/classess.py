from dataclasses import dataclass
import requests


@dataclass
class ServiceNow:
    """Service Now API Details
    """
    # The instance of your service now "<instance>.service-now.com"
    instance: str
    # Service Account Username
    # (Must have itil, rest_service, and web services role)
    username: str
    # Service Account Password
    password: str


@dataclass
class NewIncident(ServiceNow):
    # JSON String of the SNOW Fields
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json"
    }
    table: str = "/api/now/table/incident"

    def create_incident(self, body: str) -> dict:
        url = f"https://{self.instance}{self.table}"
        response = requests.post(
            url, auth=(self.username, self.password),
            headers=self.headers,
            data=body
            )
        # Check for HTTP codes other than 200
        if response.status_code not in list(range(200, 300)):
            print('Status:',
                  response.status_code,
                  'Headers:', response.headers)
            return response.json()

        # Decode the JSON response into a dictionary and use the data
        data = response.json()
        return data
