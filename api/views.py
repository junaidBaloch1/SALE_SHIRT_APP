from django.http import JsonResponse

# Create your views here.

def Home(request):
    return JsonResponse({"info":"FA18-BCS-000","name":"junaid"})