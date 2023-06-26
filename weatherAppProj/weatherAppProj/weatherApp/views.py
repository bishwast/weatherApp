from django.shortcuts import render

# Create your views here.
def index(request):
    ## Collect the data from user input
    if request.method == 'POST':        ## Sending a form
        city = request.POST['city']     ## Colelct a form for city
    else:
        city = ''
    return render(request, 'index.html', {'city': city})