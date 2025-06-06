from django.shortcuts import render
from django.http import HttpResponse
from calendar import Calendar
from datetime import datetime
from django.shortcuts import redirect
from .models import MinhaAgenda
from django.shortcuts import get_object_or_404

# Create your views here.

def agenda(request):
    today = datetime.today()
    year = today.year
    month = today.month
    
    cal = Calendar(firstweekday=6)
    weekly = cal.monthdayscalendar(year, month)
    
    
    
    if request.GET.get('mes') and request.GET.get('ano'):
        cal = Calendar(firstweekday=6)
        month = int(request.GET.get('mes'))
        year = int(request.GET.get('ano'))
        weekly = cal.monthdayscalendar(year, month)
        
    mes_anterior = month - 1
    ano_anterior = year
    if mes_anterior == 0:
        mes_anterior = 12
        ano_anterior -= 1

    # Próximo mês
    mes_proximo = month + 1
    ano_proximo = year
    if mes_proximo == 13:
        mes_proximo = 1
        ano_proximo += 1
     
        
    
    compromissos = MinhaAgenda.objects.all().order_by('data', 'horario')
    
    
    context = {
    'ano': year,
    'mes': month,
    'weekly': weekly,
    'today': today,
    'compromissos': compromissos,
    'mes_anterior': mes_anterior,
    'ano_anterior': ano_anterior,
    'mes_proximo': mes_proximo,
    'ano_proximo': ano_proximo,
    }
    
        
    return render(request,'minha_agenda.html', context)



def adiciona_compromisso(request):
    
    if request.method == 'POST':
            descricao = request.POST.get('descricao')
            data = request.POST.get('data')
            horario = request.POST.get('horario')
            
            compromisso = MinhaAgenda(descricao=descricao, data=data, horario=horario)
            
            compromisso.save()
            
            
            nova_data = data.split('-')
            mes = nova_data[1]
            ano = nova_data[0]
            return redirect(f'/agenda/minha_agenda/?mes={mes}&ano={ano}')  
        
    return redirect('agenda')


def excluir_compromisso(request, id):
    compromisso = get_object_or_404(MinhaAgenda, id=id)
    compromisso.delete()
    
    data = compromisso.data
    mes = data.month
    ano = data.year
    
    return redirect(f'/agenda/minha_agenda/?mes={mes}&ano={ano}')