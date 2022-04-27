from rest_framework.generics import CreateAPIView
from mpesa.api.serializers import LNMOnlineSerializer
from mpesa.models import LNMOnline


class LNMCallbackAPIView(CreateAPIView):
    queryset = LNMOnline
    serializer_class = LNMOnlineSerializer

    def create(self, request):
        print(request.data)
