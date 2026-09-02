from django.shortcuts import render
from django.views.generic import ListView,CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy ,reverse

from . import models
from . import forms
from .forms import Projectcreateform,Projectupdateform
from .models import Project,Task
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin




class projectlistview(LoginRequiredMixin,ListView):
    model=Project
    template_name='project/list.html'
    success_url=reverse_lazy('project_list')
    paginate_by=3
    
    def get_queryset(self):
        queryset=super().get_queryset()
        where={'user_id':self.request.user}
        q=self.request.GET.get('q',None)
        if q :
            where['title__icontains']=q  
        return queryset.filter(**where)
        
        


class projectcreateview(LoginRequiredMixin,CreateView):
    model=Project
    form_class=Projectcreateform
    template_name='project/create.html'
    
    
    success_url=reverse_lazy('project_list')
    def form_valid(self, form):
        form.instance.user=self.request.user
        return super().form_valid(form)
    
class taskcreateview(LoginRequiredMixin,CreateView):
    model=Task
    fields=['description','is_completed','project']
    
    http_method_names=['post']
    
    def test_func(slef):
        project_id_old=slef.request.POST.get('project','')
        return models.Project.objects.get(PK=project_id_old)==self.request.user.id
    

    def get_success_url(self):
        return reverse('project_update',args=[self.object.project.id])
    
class taskupdateview(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model=Task
    fields=['is_completed']
    
    http_method_names=['post']
    def test_func(self):
        return self.get_object().project.user_id == self.request.user.id
    
    

    def get_success_url(self):
        return reverse('project_update',args=[self.object.project.id])
    
    
class taskdeleteview(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model=Task
    http_method_names=['post']
    
    def test_func(self):
        return self.get_object().project.user_id == self.request.user.id
    

    def get_success_url(self):
        return reverse('project_update',args=[self.object.project.id])
    

class projectupdateview(LoginRequiredMixin,UserPassesTestMixin,UpdateView): 
    model=Project
    form_class=Projectupdateform
    template_name='project/update.html'
    
    def test_func(self):
        return self.get_object().user_id==self.request.user.id
    
    def get_success_url(self):
        return reverse ('project_update',args=[self.object.id])
    
    
class projectdeleteview(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model=Project
    template_name='project/delete.html'
    success_url=reverse_lazy('project_list')
    def test_func(self):
        return self.get_object().user_id == self.request.user.id
    

        