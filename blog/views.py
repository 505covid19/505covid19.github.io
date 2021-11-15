from django.shortcuts import render


# Create your views here.

#主界面
def index(request):
    sum_deaths='5534'
    sum_infections='654132'
    context={
        "sum_deaths":sum_deaths,
        "sum_infections":sum_infections,
    }
    return render(request, 'index.html', context=context)
#########################################################################################################################################################

#新闻界面
def new1(request):
    return render(request, 'new1.html', locals())


def new2(request):
    return render(request, 'new2.html', locals())


def new3(request):
    return render(request, 'new3.html', locals())


def new4(request):
    return render(request, 'new4.html', locals())


def new5(request):
    return render(request, 'new5.html', locals())


def new6(request):
    return render(request, 'new6.html', locals())


def new7(request):
    return render(request, 'new7.html', locals())


def new8(request):
    return render(request, 'new8.html', locals())


def new9(request):
    return render(request, 'new9.html', locals())


#########################################################################################################################################################

#可视化单独大图界面
def index1(request):

    return render(request, 'index1.html',locals())


def index2(request):
    return render(request, 'index2.html', locals())


def index3(request):
    return render(request, 'index3.html', locals())


def index4(request):
    return render(request, 'index4.html', locals())


def index5(request):
    return render(request, 'index5.html', locals())


def index6(request):
    return render(request, 'index6.html', locals())


def index7(request):
    return render(request, 'index7.html', locals())


#########################################################################################################################################################

#数据库操作草稿








