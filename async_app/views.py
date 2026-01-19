import asyncio
from django.http import HttpResponse


async def async_counter_view(request):
    print("Iniciando contador assíncrono...")
    
    
    await asyncio.sleep(3) 
    
    print("Contador finalizado!")
    return HttpResponse("<h1>Tarefa concluída!</h1><p>A view esperou 5 segundos de forma assíncrona.</p>")