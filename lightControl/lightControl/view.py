from django.http import HttpResponse
from django.template import Template, Context

def readPage(link):
    page = open(link, "r")
    template = Template(page.read())
    page.close
    contexto = Context()
    return template.render(contexto)

def LightControl(request): # <- index
    page = readPage("lightControl/lightControl/templates/core/index.html")
    return HttpResponse(page)

def about(request): # <- about
    page = readPage("lightControl/templates/about.html")

    return render