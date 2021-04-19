import os
import requests


class GithubApi:
    def __init__(self):
        self.API_URL = os.environ.get("GITHUB_API_URL", "https://api.github.com")
        self.GITHUB_TOKEN = os.environ.get("GITHUB_TOKEN")

    def get_organization(self, login: str):
        """Busca uma organização no Github

        :login: login da organização no Github
        """
        try:

            response = requests.get(
                f'{self.API_URL}/orgs/{login}',
                headers={'Authorization': f'Bearer {self.GITHUB_TOKEN}'},
                params={
                    'accept': 'application/vnd.github.v3+json'
                }
            )

            if response.status_code == 200 and response.json():
                return response.json()
        except Exception:
            return {}

    def get_organization_public_members(self, login: str) -> int:
        """Retorna todos os membros públicos de uma organização

        :login: login da organização no Github
        """
        try:
            response = requests.get(
                f'{self.API_URL}/orgs/{login}/members',
                headers={'Authorization': f'Bearer {self.GITHUB_TOKEN}'},
                params={
                    'accept': 'application/vnd.github.v3+json'
                }
            )

            if response.status_code == 200:
                return len(response.json())
        except Exception:
            return 0
