from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
def index(request):
    listPerson=[    
                {'profile':'images/javad-ghasemi.jpg','firstName':'جواد','lastName':'قاسمی','age':20,'skills':['Python','Django','SQL Server' ,'HTML', 'CSS', 'JavaScript','Git']},
                {'profile':'images/mahdi-abbasi.jpg','firstName':'مهدی','lastName':'عباسی','age':46,'skills':['Python','Django','SQL Server' ,'HTML', 'CSS', 'JavaScript','C#','C++','.NET','Java']},
                {'profile':'images/john.jpg','firstName':'جان','lastName':'ویلسون','age':36,'skills':['Python','Django','SQL Server', 'JavaScript','C#','C++']},
                {'profile':'images/karim.jpg','firstName':'کریم','lastName':'عبدالله','age':26,'skills':['Git', 'JavaScript','C#','C++']},
                ]
    context={
        'media_url':settings.MEDIA_URL,
        'teacher':listPerson,
        'lenList':range(0 , len(listPerson)),
    }
    return render(request,'home/index.html',context)
