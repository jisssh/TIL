from django.contrib import admin
from .models import Article
# Register your models here.
# Article 모델을  admin site 에서 확인하고싶다.
admin.site.register(Article)