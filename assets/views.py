from django.shortcuts import render
from .models import Asset

# Create your views here.
def fetch_assets_list(request):
    assets = Asset.objects.all()
    return render(request, "assets/assets_list.html", {'assets': assets})
