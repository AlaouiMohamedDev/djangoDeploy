import json

from django.shortcuts import render
from django.http import HttpResponse

liste={"nom":"mohamed","prenom":"alaoui"}
def product_list(request):
    return HttpResponse(json.dumps(liste), content_type="application/json")
# Create your views here.
