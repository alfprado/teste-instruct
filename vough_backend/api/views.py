
from rest_framework.views import Response, APIView
from api.models import Organization
from api.serializers import OrganizationSerializer
from api.integrations.github import GithubApi

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
