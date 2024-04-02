# Create your views here.
from django.http import JsonResponse
from e_commerce.models import Comic


def comic_list_api_view(request):
    if request.method == 'GET':
        print("Endpoint: comic_list_api_view")
        queryset = list(Comic.objects.all().values())
        return JsonResponse(data=queryset, safe=False)
    else:
        return JsonResponse(data={"message": "Método HTTP no permitido."}, status=405)


def comic_filter_stock_api_view(request):
    if request.method == 'GET':
        print("Endpoint: comic_filter_stock_api_view")
        queryset = list(Comic.objects.filter(stock_qty=5).values())
        return JsonResponse(data=queryset, safe=False)
    else:
        return JsonResponse(data={"message": "Método HTTP no permitido."}, status=405)


def comic_filter_price_api_view(request):
    if request.method == 'GET':
        print("Endpoint: comic_filter_price_api_view")
        queryset = list(Comic.objects.filter(price__gt=3).values())
        return JsonResponse(data=queryset, safe=False)
    else:
        return JsonResponse(data={"message": "Método HTTP no permitido."}, status=405)


def comic_list_order_api_view(request):
    if request.method == 'GET':
        print("Endpoint: comic_list_order_api_view")
        queryset = list(Comic.objects.order_by('marvel_id').values())
        return JsonResponse(data=queryset, safe=False)
    else:
        return JsonResponse(data={"message": "Método HTTP no permitido."}, status=405)
