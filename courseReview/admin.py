from django.contrib import admin

from .models import college, department, major, course, professor, extendUser, review

# Register your models here.
admin.site.register(college)
admin.site.register(department)
admin.site.register(major)
admin.site.register(course)
admin.site.register(professor)
admin.site.register(extendUser)
admin.site.register(review)