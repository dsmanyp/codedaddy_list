from django.shortcuts import render
from bs4 import BeautifulSoup
import requests

BASE_CRAIGLIST_URL = 'https://berlin.craigslist.org/search/sss?query={}'

# Create your views here.
def home(request):
    return render(request, 'base.html')


def new_search(request):
    search = request.POST.get('search')
    response = requests.get('https://berlin.craigslist.org/search/ggg?query=cafe&sort=rel&is_paid=all')
    date = response.text

    data = {
        'search': search,
    }
    return render(request, 'my_app/search.html', data)
