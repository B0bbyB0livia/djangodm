import datetime

from django.http import HttpResponse, JsonResponse, Http404
from django.views.generic import View
from django.shortcuts import render

# Create your views here.

class CheckoutTestView(View):
    def post(self, request, *args, **kwargs):
        print request.POST.get("testData")
        if request.is_ajax():
            raise Http404
            data = {
                "works": True,
                "time": datetime.datetime.now(),
            }
            return JsonResponse(data)
        return HttpResponse("Hello there")

    def get(self, request, *args, **kwargs):
		template = "checkout/test.html"
		context = {}
		return render(request, template, context)
