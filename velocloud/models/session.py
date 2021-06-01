

class VCO(object):
    """Velocloud Orchestrator"""

    def __init__(self, TOKEN: str, API_URL: str):
        self.token = f'TOKEN {TOKEN}'
        self.API_URL = API_URL
        self.headers = {'Content-Type': 'application/json', 'Authorization': f'{self.token}'}

    def get_headers(self):
        return self.headers
