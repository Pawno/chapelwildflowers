from django.contrib import admin

# Register your models here.

from website.models import BlogPost, EmailSubscriber

@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    pass

@admin.register(EmailSubscriber)
class CourseAdmin(admin.ModelAdmin):
    pass