from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import UserI

@api_view(['POST'])
def receive_phone(request):
    phone = request.data.get("phone")
    if phone:
        UserI.objects.create(phone=phone)
        return Response({"message":f"{phone}"})
    return Response({"error": "Текст не получен"}, status=400)
