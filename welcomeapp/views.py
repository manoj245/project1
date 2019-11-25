from django.http import HttpResponse
def welcome(request):
    return HttpResponse("""<html><body bgcolor=gray><h1><center> welcome </center></h1></body></html>""")


# Create your views here.
