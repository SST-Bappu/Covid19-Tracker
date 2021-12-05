from django.shortcuts import render,HttpResponse
import requests
from rest_framework.utils import serializer_helpers
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.renderers import TemplateHTMLRenderer
from .serializer import*
from .serializer import countrySerializer
# Create your views here.

def index(request):
    summary = requests.get('https://api.covid19api.com/summary').json()
    Global = summary['Global']
    date = Global['Date'].split('T')
    date = date[0]
    countries = summary['Countries']
    selected = None
    if request.method=='POST':
        data = request.POST.get('country')
        for country in countries:
            if country['Country']==data:
                selected = country
                break
    return render(request,'index.html',{'summary':Global,'countries':countries,'selected':selected,'date':date})

class CountryAPIView(APIView):
    # renderer_classes = [TemplateHTMLRenderer]
    serializer_class = countrySerializer
    def get_queryset(self):
        summary = requests.get('https://api.covid19api.com/summary').json()
        Global = summary['Global']
        serializer = countrySerializer(summary['Countries'])
        # return Response({'countries':serializer.data},template_name='index.html')
        return Response(serializer.data)
    