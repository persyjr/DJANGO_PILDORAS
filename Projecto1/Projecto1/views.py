from django.http import HttpResponse
import datetime
from django.template import Template, Context

def saludo(request): # primera vista 
    print("saludo(request)")
    docExterno=open('../Projecto1/Projecto1/plantillas/template.html')#abro documento
    plt =Template(docExterno.read())#leo documento y lo convierto en un objeto template
    docExterno.close() #cierro comunicacion para ahorrar recursos
    ctx=Context() #creo objeto contecto
    documento=plt.render(ctx)

    return HttpResponse(documento)

def despedida(request): # segunda vista 
    print("despedida(request)")
    return HttpResponse("Hasta la vista Baby")

def dameFecha(request): # tercera vista 
    print("dameFecha(request)")
    fecha_actual=datetime.datetime.now()
    documento="""
        <html>
        <head><title></title></head>
        <body style='background-color:yellow;'>
        <h1>la fecha y hora es </h1>
        <p id=fecha>%s</p>
        </html>
        """ % fecha_actual
    return HttpResponse(documento)

def calculaEdad(request,edad,agno): # cuarta vista 
    print("calculaEdad(request)")
    
    periodo=agno-2023
    edadFutura=edad+periodo
    documento="""
        <html>
        <head><title></title></head>
        <body style='background-color:blue;'>
        <h2>En el año %s </h2>
        <p id=edad>tendras %s años</p>
        <p id=edad>Actualmente tienes  %s años</p>
        </html>
        """ %(agno,edadFutura,edad)
    return HttpResponse(documento)