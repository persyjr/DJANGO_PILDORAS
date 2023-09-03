from django.http import HttpResponse
import datetime

def saludo(request): # primera vista 
    print("saludo(request)")
    return HttpResponse("hola primera vista")

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