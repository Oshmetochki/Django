from django.http import HttpResponse
def index(request):
    return HttpResponse('Куда?')
def clown(request):
    return HttpResponse('Сам клоун')
