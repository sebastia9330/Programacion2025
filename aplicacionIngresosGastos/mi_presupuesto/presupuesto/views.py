from django.shortcuts import render
from .models import Ingresos, Gastos

# Create your views here.
def index(request):
    ingresos = Ingresos.objects.all()
    gastos = Gastos.objects.all()
    return render(request, "presupuesto/index.html", {"ingresos": ingresos, "gastos": gastos})