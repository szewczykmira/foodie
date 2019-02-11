from django.http import JsonResponse


def message(request):
    if request.method == 'POST':
        print(request.POST)
    return JsonResponse(request, {"all": "is ok"})