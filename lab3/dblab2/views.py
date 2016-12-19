from django.http import HttpResponseRedirect


def main(request):
    return HttpResponseRedirect('/objects/')