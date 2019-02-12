from django.shortcuts import render
from django.conf import settings
import requests

# Create your views here.


def home(request):
    geodata = requests.get("http://ip-api.com/json/").json()
    return render(request, 'usingapis/home.html', {
        'ip': geodata['query'],
        'country': geodata['country'],
    })


def omdb(request):
    token = settings.OMDB_APP_KEY
    search_result = {}
    if 'title' in request.GET:
        title = request.GET['title']
        url = 'http://www.omdbapi.com/?s=%s&apikey=%s' % (title, token)
        response = requests.get(url)
        search_result = response.json()
        if search_result['Response'] == 'True':
            search_was_successful = (response.status_code == 200)  # 200 = SUCCESS
            search_result['success'] = search_was_successful
    return render(request, 'usingapis/omdb.html', {'search_result': search_result})
