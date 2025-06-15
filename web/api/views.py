from django.http import JsonResponse


def test_api(request):
    return JsonResponse(
        {
            "success": True
         },
        status=200,
    )
