from typing import Union, Tuple

from django.http import JsonResponse, HttpRequest
from rest_framework.views import APIView

from api.models import User


class UserCreate(APIView):

    @staticmethod
    def _get_body(body: dict) -> Union[JsonResponse, Tuple[None, None]]:
        name = body.get('name', None)
        email = body.get('email', None)
        return name, email

    def post(self, request: HttpRequest, *args, **kwargs,) -> JsonResponse:
        body: dict  = request.data
        name, email = self._get_body(body=body)
        if not name or not email:
            return JsonResponse(
                {
                    "error": "name and email is required",
                },
                status=400,
            )

        user: User = User.objects.create(
            name=name,
            email=email,
        )

        return JsonResponse(
            {
                'id': user.id,
                "name": user.name,
                "email": user.email,
            },
            status=200,
        )

