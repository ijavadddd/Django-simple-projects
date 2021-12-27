from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
def index(request):
    listPerson=[    
                {'profile':'images/javad-ghasemi.jpg','firstName':'جواد','lastName':'قاسمی','age':'20','skills':['Python','Django','SQL Server' ,'HTML', 'CSS', 'JavaScript']},
                {'profile':'images/mahdi-abbasi.jpg','firstName':'مهدی','lastName':'عباسی','age':'46','skills':['Python','Django','SQL Server' ,'HTML', 'CSS', 'JavaScript','C#','C++','.NET','Java']}
                ]
    context={
        'media_url':settings.MEDIA_URL,
        'teacher':listPerson,
        'lenList':range(0 , len(listPerson)),
    }
    return render(request,'home/index.html',context)
