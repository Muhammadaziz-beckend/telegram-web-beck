from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['POST'])
def receive_phone(request):
    phone_number = request.data.get("phone",None)
    if phone_number:
        return Response({"message": f"Ваш номер: {phone_number}"})
    return Response({"error": "Номер не получен"}, status=400)
