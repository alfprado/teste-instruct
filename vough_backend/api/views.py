from rest_framework.views import Response, APIView
from api.models import Organization
from api.serializers import OrganizationSerializer
from api.integrations.github import GithubApi
from django.http import Http404

# TODOS:
# 1 - Buscar organização pelo login através da API do Github
# 2 - Armazenar os dados atualizados da organização no banco
# 3 - Retornar corretamente os dados da organização
# 4 - Retornar os dados de organizações ordenados pelo score na listagem da API


class OrganizationList(APIView):
    """
    List all Organizations ordered by score.
    """
    def get(self, request, format=None):
        organizations = Organization.objects.all().order_by('-score')
        serializer = OrganizationSerializer(organizations, many=True)
        return Response(serializer.data)


class OrganizationDetail(APIView):

    def get_object(self, pk):
        try:
            return Organization.objects.get(pk=pk)
        except Exception:
            return {}

    def get(self, request, pk, format=None):
        """
        Update or add organization to the list.
        """

        git = GithubApi()
        org = git.get_organization(pk)

        if org:
            members = git.get_organization_public_members(pk)
            data = {
                'login': pk,
                'name': org['name'],
                'score': org['public_repos'] + members
            }

            try:
                organization = Organization.objects.get(pk=pk)

                serializer = OrganizationSerializer(organization, data)

                if serializer.is_valid():
                    serializer.save()

                return Response(serializer.data)

            except Organization.DoesNotExist:

                serializer = OrganizationSerializer(data=data)
                if serializer.is_valid():
                    serializer.save()

                return Response(serializer.data)
        raise Http404
