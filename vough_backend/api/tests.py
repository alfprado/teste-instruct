from api.integrations.github import GithubApi
from django.test import TestCase


class IntegrationsTests(TestCase):

    def setUp(self):
        self.git = GithubApi()

    def test_organization_public_members(self):
        self.assertEqual(self.git.get_organization_public_members('instruct-br'), 9)

    def test_organization(self):
        org = self.git.get_organization('instruct-br')

        self.assertEqual(org['name'], 'Instruct')
        self.assertEqual(org['public_repos'], 41)
