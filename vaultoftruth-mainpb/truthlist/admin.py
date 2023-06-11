from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Category)
admin.site.register(Question)
admin.site.register(UserAnswer)
admin.site.register(Reason)
admin.site.register(ReasonAnswer)
admin.site.register(Comment)
