from django.shortcuts import render

# Create your views here.
def home(request):
    d={'author': 'Rahim','age':5,'lst':[1,2,3,4],'courses':[
        {
            'id' : 1,
            'name' : 'Python',
            'fee' : 2000
        },
        {
            'id' : 2,
            'name' : 'Django',
            'fee' : 10000
        },
        {
            'id' : 3,
            'name' : 'C',
            'fee' : 1000
        }
    ]}
    return render(request, "home.html",context=d)
