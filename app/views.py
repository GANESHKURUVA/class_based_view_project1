from typing import Any, Dict
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View,TemplateView
from app.forms import *


# Create your views here.

def fbv_string(request):
    return HttpResponse('this is fbv string data')


class cbv_string(View):
    def get(self,request):
        return HttpResponse('this is cbv string data')
    

def fbv_html(request):
    return render(request,'fbv_html.html')

class cbv_html(View):
    def get(self,request):
        return render(request,'cbv_html.html')
    

def fbv_forms(request):
    fbo=TopicForm()
    d={'fbo':fbo}
    if request.method=='POST':
        fbd=TopicForm(request.POST)
        if fbd.is_valid():
            fbd.save()
            return HttpResponse('data inserted succssefully .. ')
    return render(request,'fbv_forms.html',d)


class cbv_forms(View):
    def get(self,request):
        cbo=TopicForm
        d={'cbo':cbo}
        return render(request,'cbv_forms.html',d)
    def post(self,request):
        cbo=TopicForm(request.POST)
        if cbo.is_valid():
            cbo.save()
            return HttpResponse('data is inserted.... ..')
        
class cbv_context(TemplateView):
    template_name='cbv_contextforms.html'
    def get_context_data(self, **kwargs):
        ecdo=super().get_context_data(**kwargs)
        fo=TopicForm
        ecdo['fo']=fo
        return ecdo
    
    def post(self,request):
        fo=TopicForm(request.POST)
        if fo.is_valid():
            fo.save()
            return HttpResponse('topic inserted successfully...!!!')




