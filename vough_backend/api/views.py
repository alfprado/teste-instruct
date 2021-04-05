from rest_framework.views import Response, APIView
from rest_framework import status
from api.models import Organization
from api.serializers import OrganizationSerializer
from api.integrations.github import GithubApi
from django.http import Http404


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
                'name': org['name'] if org['name'] else pk,
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

    def delete(self, request, pk, format=None):
        """
        Delete an Organization.
        """
        organization = self.get_object(pk)
        if organization:
            organization.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            raise Http404
