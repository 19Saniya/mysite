from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from features.models import Features
from userInfo.models import UserInfo


def home(request):
    featuresData = Features.objects.all()

    fdata = {
        'featuresData': featuresData
    }
    data = {
        'title': 'Home Page',
        'bdata': 'Welcome3',
        'courselist': ['PHP', 'JAVA', 'C', 'DJANGO'],
        'numbers': [10, 20, 30, 40, 50],
        'student_details': [
            {'name': 'pradeep', 'phone': 9234455343},
            {'name': 'mishra', 'phone': 3798659652}
        ]
    }
    return render(request, "home.html", fdata)


def bootstrap(request):
    return render(request, "Bootstrap.html")


def triangle(request):
    return render(request, "triangle.html")


# def userform(request):
    # finalans = 0
    # data = {}
    # try:
    #     # n1=int(request.GET['num1'])
    #     # n2=int(request.GET['num2'])
    #     n1 = request.POST.get('user_name')
    #     n2 = request.POST.get('user_email')
    #     n3 = int(request.POST.get('user_phone'))
    #     n4 = request.POST.get('user_comment')
    #     finalans = {}
    #     data = {
    #         'n1': n1,
    #         'n2': n2,
    #         'output': "Submitted Successfully"
    #     }
    #     url = '/about/?output={}'.format(finalans)
    #     return HttpResponseRedirect(url)
    # except:
    #     pass
def userform(request):
    msg=''
    if request.method == "POST":
        name = request.POST.get('userInfo_name')
        email = request.POST.get('userInfo_email')
        phone = request.POST.get('userInfo_phone')
        comment = request.POST.get('userInfo_comment')
        sv = UserInfo(userInfo_name=name, userInfo_email=email, userInfo_phone=phone, userInfo_comment=comment)
        sv.save()
        msg='Submitted Successfully'
    return render(request, "userform.html", {'msg':msg})

# def saveuser(request):
#     if request.method=="POST":
#         name = request.POST.get('user_name')
#         email = request.POST.get('user_email')
#         phone = request.POST.get('user_phone')
#         comment = request.POST.get('user_comment')
#         sv = UserInfo(userInfo_name=name, userInfo_email=email, userInfo_phone=phone, userInfo_comment=comment)
#         sv.save()
#     return render(request, "userform.html",)
def about(request):
    # if request.method=='GET':
    #     output=request.GET.get{'output'}
    return (request, "about")


def course(request):
    return HttpResponse("Welcome")


def coursedetails(request, courseid):
    return HttpResponse(courseid)
