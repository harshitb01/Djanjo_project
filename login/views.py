from django.shortcuts import render
# Create your views here.


def home_page(request):
    return render(request, 'home.html')


def details(request):
    UserName = request.GET['UName']
    Password = request.GET['Pwd']
    return render(request, 'result.html', {'name': 'Harshit',
                                           'no': '9247847383',
                                           'mail': 'hbj3974203@gmail.com',
                                           'dob': '2002/07/11',
                                           'UName': UserName,
                                           'Pwd': Password})
