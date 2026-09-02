from django.db import models






class Author(models.Model):
    bio=models.CharField(null=True)
    name=models.CharField(max_length=100,null=True)
    email=models.EmailField(unique=True,null=True)
    birth_day=models.DateTimeField(null=True)
    
    def __str__(self):
        return self.name +' , email='+self.email
    



class tag(models.Model):
    name=models.CharField(max_length=255,null=True)
    description=models.TextField(null=True)
    
    def __str__(self):
        return self.name 
    

    


# OneToOneField
class Article(models.Model):
    title=models.CharField(max_length=255,null=True)
    content=models.TextField(null=True)
    created_at=models.DateTimeField(auto_now_add=True,null=True)
    updated_at=models.DateTimeField(auto_now=True,null=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE,null=True)
    tag=models.ManyToManyField(tag)
    
    



# ForeignKey
# class article(models.Model):
#     title=models.CharField(max_length=255),
#     content=models.TextField(),
#     created_at=models.DateTimeField(auto_now_add=True),
#     updated_at=models.DateTimeField(auto_now=True),
#     author=models.ForeignKey(Author,on_delete=models.PROTECT)



# # ManyToManyField
# class Article(models.Model):
#     title=models.CharField(max_length=255,null=True)
#     content=models.TextField(null=True)
#     created_at=models.DateTimeField(auto_now_add=True,null=True)
#     updated_at=models.DateTimeField(auto_now=True,null=True)
#     author=models.ManyToManyField(tag)