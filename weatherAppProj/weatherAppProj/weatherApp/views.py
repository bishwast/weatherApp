from django.shortcuts import render
import json
import urllib.request

# Create your views here.
def index(request):
    ## Collect the data from user input
    if request.method == 'POST':        ## Sending a form
        
        city = request.POST['city']     ## Colelct a form for city
        
        # Access openweather API: request url and open
        req = urllib.request.urlopen('https://api.openweathermap.org/data/2.5/weather?q='+city+'&appid=5f260826a74a9f764f807ceffa9b90cc').read()
        json_data = json.loads(req)
        # covert tp dict
        data = {
            "country_code" : str(json_data['sys']['country']),
            "coordinate" : str(json_data['coord']['lon']) + ' ' + str(json_data['coord']['lat']),
            "temperature" : str(json_data['main']['temp']) + 'k',
            "pressure" : str(json_data['main']['pressure']),
            "humidity" : str(json_data['main']['humidity']),
        }
        
    else:
        city = ''
        data = {}
    return render(request, 'index.html', {'city': city, 'data' : data})


