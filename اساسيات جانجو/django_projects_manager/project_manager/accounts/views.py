from django.shortcuts import redirect, render
from django.urls import reverse,reverse_lazy
from django.views.generic import CreateView
from accounts.forms import UserFormCreation, UserProfileView
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required


class register_view (CreateView):
    form_class=UserFormCreation
    # success_url=reverse_lazy("Login")
    template_name='registration/register.html'
    def get_success_url(self):
        login(self.request,self.object)
        return reverse_lazy('project_list')
        
    
@login_required
def EditProfile(request):
    
    if request.method == 'POST':
        
        form=UserProfileView(request.POST,instance=request.user)
        
        if form.is_valid():
            form.save()
            return redirect('profile')
            
            
        
    else:
        form=UserProfileView(instance=request.user)
                        
        return render(request,'registration/profile.html',{
            'form':form
        })
        
