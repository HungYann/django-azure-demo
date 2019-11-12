from rest_framework.views import APIView
from rest_framework.response import Response
from . models import myfood
from . serializers import foodSerializer


class foodList(APIView):

    def get(self,request):
        food1 = myfood.objects.all()
        serializer = foodSerializer(food1,many=True)
        return Response(serializer.data)