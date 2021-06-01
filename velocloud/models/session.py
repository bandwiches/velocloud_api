

class VCO(object):
    """Velocloud Orchestrator"""

    def __init__(self, TOKEN: str, API_URL: str = "https://vco47-usvi1.velocloud.net"):
        self.token = f'TOKEN {TOKEN}'
        self.API_URL = API_URL
        self.headers = {'Content-Type': 'application/json', 'Authorization': f'{self.token}'}

    def get_headers(self):
        return self.headers
