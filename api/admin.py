from django.contrib import admin

from .models import Doctor, Rating, FeedBack, Category, Patient, Comment

admin.site.register(Rating)
admin.site.register(Category)
admin.site.register(Comment)


@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ['id', 'fullname',  'birthdate', 'blood_group', 'occupation',
                    'gender']
    list_display_links = ['id', 'fullname']
    search_fields = ['fullname', 'contact']
    ordering = ('fullname',)


@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ['id', 'title',  'contact', 'is_published', 'no_of_ratings',
                    'avg_rating']
    list_display_links = ['id', 'title']
    search_fields = ['title', 'fees']
    list_editable = ('is_published',)
    ordering = ('fees',)


@admin.register(FeedBack)
class FeedBackAdmin(admin.ModelAdmin):
    list_display = ['id', 'FullName', 'email_id', 'phone_num', 'chief_complaint', 'message']
    list_filter = ['chief_complaint']
    search_fields = ['phone_num', 'email_id']
