from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['POST'])
def receive_phone(request):
    text = request.data.get("text")
    if text:
        return Response({"message": f"Вы ввели: {text}"})
    return Response({"error": "Текст не получен"}, status=400)
