from django.http import HttpResponse
from django.views import View
from .tasks import hello2
from django.shortcuts import render


class IndexView(View):
    def get(self, request):
        print(request.user.is_authenticated, 'true -request.session')
        hello2.delay()
        return HttpResponse('Hello!')
