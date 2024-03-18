from django.shortcuts import redirect
from django.urls import reverse


class ConfirmUserMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        user = request.user

        if (
                user.is_authenticated and
                user.is_confirmed and
                request.path == reverse('authentication:confirmation_page')
        ):
            return redirect('exam_preparation:prepared-question-list')
        if (
                request.path == reverse('authentication:login') or
                request.path == reverse('authentication:confirmation_page') or
                request.path == reverse('index')
        ):
            return self.get_response(request)

        if user.is_authenticated and not user.is_confirmed and not user.is_superuser:
            return redirect('authentication:confirmation_page')

        response = self.get_response(request)
        return response
