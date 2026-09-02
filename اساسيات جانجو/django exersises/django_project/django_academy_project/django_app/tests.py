from django.test import TestCase
from django_academy_project.django_app.models import Article




article = Article()  
article.title = 'django_name5'
article.content = 'django_name5'
article.save()
