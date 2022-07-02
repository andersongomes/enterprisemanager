from rest_framework import status, viewsets
from rest_framework.response import Response


class AboutViewSet(viewsets.ViewSet):
    def about(self, request):
        return Response("This is a system to manage a little enterprise", status.HTTP_200_OK)
