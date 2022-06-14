from django.views.generic.list import ListView
from turtle import title
from django.conf import settings
from django.shortcuts import get_object_or_404, redirect, render
from .models import *
from django.core.mail import send_mail
from django.utils.translation import gettext as _
# Create your views here.

def index(request):
    data = IndexCarousel.objects.all()
    news = News.objects.filter(category=2).order_by('createdDate')[0:10]
    resources = Resources.objects.all().order_by('createdDate')[0:10]
    contests = News.objects.filter(category=1).order_by('createdDate')[0:10]
    talenteds = TalentedStudents.objects.filter(isInHome=True)[0:10]
    context = {
        'slides':data,
        'news':news,
        'laws':resources,
        "contests":contests,
        "talenteds":talenteds,
        'title':_('Bosh sahifa')
    }
    return render(request,'index.html',context)

def contact(request):
    info = MainInfos.objects.first()
    if(request.method == 'POST'):
        send_mail(
            "Fakultet saytdan xabar keldi",
            f"Jo'natuvchi:{request.POST['name']} \nJo'natuvchi telefon raqami:{request.POST['phone']}\n\nXabar:\n{request.POST['message']}",
            settings.EMAIL_HOST_USER,
            [info.email],
            fail_silently=True
        )
        return redirect('/contact/')
    return render(request,'contact-1.html')


def question_times(request):
    people = ReceptionTimes.objects.all()
    return render(request,'membership.html',{'people':people,'title':_('Qabul kunlari')})

class NewsCompetitionsList(ListView):
    paginate_by = 8
    template_name='news_competition.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = _("Tanlov yangiliklari")
        return context

    def get_queryset(self):
        return News.objects.filter(category=1)



class NewsEducationList(ListView):
    paginate_by = 8
    template_name='news_competition.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = _("Talim yangiliklari")
        return context

    def get_queryset(self):
        return News.objects.filter(category=2)




class EmployeesList(ListView):
    model= Employees
    paginate_by = 50
    template_name='employees.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = _("Xodimlari")
        return context



def about_us(request):
    data = Texts.objects.get(id=1)
    context={
        'breadcrumbs':[_('Biz haqimizda')],
        "data":data,
        "title":"Biz haqimizda"
    } 
    return render(request, "about.html",context=context)




def news_detail(request,id):
    data = get_object_or_404(News,pk=id)
    context={
        'breadcrumbs':[_('Yangiliklar'),data.title],
        "data":data,
        "title":data.title
    }
    return render(request,'news_detail.html',context)

from django.core.paginator import Paginator
def resources_detail(request,id):
    print("id",id)
    data = Resources.objects.filter(category=id)
    paginator = Paginator(data, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context={
        'breadcrumbs':[_('Resurslar'),],
        "page_obj":page_obj,
        "title":"Resurslar"
    }
    return render(request,'laws_list.html',context)


def talenteds_detail(request,id):
    data = TalentedStudents.objects.get(id=id)
    context={
        'breadcrumbs':[_('Yulduzlar'),data.fullname],
        "data":data,
        "title":data.fullname
    }
    return render(request,'talenteds_detail.html',context)


class LawsList(ListView):
    model= ResourceCategory
    paginate_by = 6
    template_name='laws_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['breadcrumbs'] = ['Meyoriy hujjatlar']
        context['title'] = ('Meyoriy hujjatlar')
        return context



class TalentedsList(ListView):
    model= TalentedStudents
    paginate_by = 6
    template_name='talenteds_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['breadcrumbs'] = [("Fakulter talantli o'quvchilari")]
        context['title'] = ("Fakulter talantli o'quvchilari")
        return context

