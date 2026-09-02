from django.shortcuts import render , redirect
from django.http import HttpResponse
from django.urls import reverse,reverse_lazy

from django_app.models import Author,Article,tag
from django_app.forms import Articlesform,Authorform
from django.views.generic import ListView ,DetailView,FormView,CreateView,UpdateView



#old func
"""
# hello_world function 
def hello_world(request):
    
    
    # return HttpResponse('hello world')    
    return render(request,'hello.html',{'name':'yousef','names':[
        'yousef',
        'ahmad',
        'sara'
    ]})
    





# function to render data and get varibles from url 
def article(request,id,name,age):
    return render(request,'article/view_article.html',{'name':name,'age':age,'id':id})
    

# fetch data "read"
def articles(request):
    #lastest
    #earlist
    #first
    #last
    #order_by
    
    
    #data=Article.objects.all()[4:8]
    
    #------------------------------------------------------------------------------------------
    
    # lt=less than
    # gt=greater than
    
    # lte=less than or eq
    # gte=greater than or eq
    #range 
    #data=Article.objects.filter(pk__lt=20)
    #data=Article.objects.filter(pk__range=(20,30))
    #title__contains  %title%
    #title__icontains %TitLe%
    #startswith %title
    #endswith title%
    #prefetch_related (many to many)
    #select_related (one to one)
    #data=Article.objects.select_related('author').all()
    
    data=Article.objects.prefetch_related('tag').select_related('author').all()

    
    
    print(data)
    return render(request,'article/show_articles.html',{'data':data})
    

def articles_with_id(request,id):

    try:

        data=Article.objects.get(pk=id)
        print(data)
    except KeyError as e:
        data=f'an error plaese enter a right value {e}'
        
    finally:
        return render(request,'articles_with_id.html',{'data':data})
        
        
# update function apdate and filtering the data 
def update_article(request):
    Article.objects.filter(pk=1).update(content='its 1 prammary key the content was updated')
    article=Article.objects.get(pk=1)

    

    return render(request,'articles_with_id.html',{'data':article})
    
def delete_article(request,id):
    print(id)
    try:
        Article.objects.all().delete()
        article=Article.objects.all()
        print(article)
    except:
        print('an error')
        
    return redirect(f'/djangoapp/articles/{id}')


def create_article(request):
    
    if request.method=='POST':
        
        form=Articlesform(request.POST)
        if form.is_valid():
        
            title=form.cleaned_data['title']
            content=form.cleaned_data['content']
            author_id=form.cleaned_data['author_id']
            tags=form.cleaned_data['tags']
            
            
            
            article=Article.objects.create(author_id=author_id.id,title=title,content=content)
            article.tag.set(tags)
            return redirect('/djangoapp/articles/')
        
        

        
        
    else: 
        
        
        
        
        form=Articlesform()
        
        
        

        
        return render(request,'article/create.html',{'form':form})

def create_author(request):
    
    if request.method=='POST':
        
        form=Authorform(request.POST)
        print('isn,t_valid')
        if form.is_valid():
            print('is_valid')
            name=form.cleaned_data['name']
            email=form.cleaned_data['email']
            birthdate=form.cleaned_data['birthdate']
            bio=form.cleaned_data['bio']

            
            Author.objects.create(name=name,email=email,birth_day=birthdate,bio=bio)
            
            

            return redirect('/djangoapp/articles/create')
        
        else:
            print(form.errors)

    else: 
        
        
        
        
        form=Authorform()
        
        
        

        

    
    
    
# class Articleformview(FormView):
#     form_class=Articlesform
#     template_name='article/create.html'
#     success_url='/djangoapp'
#     def get_success_url(self):    
#         return reverse('article_list')
    
#     def form_valid(self, form):    
#             article=Article.objects.create(author_id=form.cleaned_data['author_id'].id,title=form.cleaned_data['title'],content=form.cleaned_data['content'])
            
#             article.tag.set(form.cleaned_data['tags'])
            

#             return super().form_valid(form)
    """


class Articlelistviews(ListView):
    model=Article
    queryset=Article.objects.prefetch_related('tag').select_related('author').all()
    template_name='article/show_articles.html'
    
class Articledetailview(DetailView):
    model=Article
    template_name='article/list.html'
    
class Articleformview(CreateView):
    model=Article
    form_class=Articlesform
    
    template_name='article/create.html'
    success_url=reverse_lazy('article_list')
    
    

    
class Articleupdateview(UpdateView):
    model=Article
    form_class=Articlesform
    template_name='article/update.html'
    success_url=reverse_lazy('article_list')

# about as examble
def about(request):
    return render(request,'about.html')
    

# home page examble , insert values into tuble 
def home(request):
    

    return render(request,'home.html')
    

class authorcreateview(CreateView):
    model=Author
    
    fields=['bio','email','name','birth_day']
    
    template_name='author/create.html'
    

    
    
    
    
    
    def get_success_url(self):
        return reverse('article_list')
    