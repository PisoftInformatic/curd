from django.shortcuts import render, HttpResponse

# Create your views here.
from django.http import HttpResponseBadRequest, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
import git

@csrf_exempt
@require_POST
def update_server(request):
    if request.method == 'POST':
        try:
            repo = git.Repo('https://github.com/PisoftInformatic/curd.git')
            origin = repo.remotes.origin
            origin.pull()
            return HttpResponse('Updated Django server successfully', status=200)
        except Exception as e:
            return HttpResponse(str(e), status=500)
    else:
        return HttpResponseBadRequest('Wrong event type')

def index(requests):
    return HttpResponse("Hello This is Home Page")

