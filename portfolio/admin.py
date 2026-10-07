from django.contrib import admin
from modeltranslation.admin import TabbedDjangoJqueryTranslationAdmin as TranslationAdmin
from .models import Project, Experience, ContactMessage, Skill, Certificate, Hackathon, HackathonImage


@admin.register(Skill)
class SkillAdmin(TranslationAdmin):
    list_display = ['name', 'category', 'icon', 'order']
    list_editable = ['category', 'icon', 'order']
    list_filter = ['category']
    search_fields = ['name_en', 'name_ru', 'name_uz']
    ordering = ['category', 'order']


@admin.register(Project)
class ProjectAdmin(TranslationAdmin):
    list_display = ['title', 'is_featured', 'order', 'created_at']
    list_editable = ['is_featured', 'order']
    list_filter = ['is_featured']
    search_fields = ['title_en', 'title_ru', 'title_uz', 'description_en', 'description_ru', 'description_uz']


@admin.register(Experience)
class ExperienceAdmin(TranslationAdmin):
    list_display = ['title', 'company', 'start_date', 'end_date', 'is_current', 'order']
    list_editable = ['order', 'is_current']
    list_filter = ['is_current']


@admin.register(Certificate)
class CertificateAdmin(TranslationAdmin):
    list_display = ['title', 'issuer', 'year', 'is_verified', 'order']
    list_editable = ['is_verified', 'order']
    list_filter = ['is_verified', 'year']
    search_fields = ['title_en', 'title_ru', 'title_uz', 'issuer']


class HackathonImageInline(admin.TabularInline):
    model = HackathonImage
    extra = 1


@admin.register(Hackathon)
class HackathonAdmin(TranslationAdmin):
    list_display = ['title', 'organizer', 'date', 'result', 'order']
    list_editable = ['order']
    list_filter = ['date']
    search_fields = ['title_en', 'title_ru', 'title_uz', 'organizer']
    inlines = [HackathonImageInline]


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'subject', 'created_at', 'is_read']
    list_editable = ['is_read']
    list_filter = ['is_read']
    readonly_fields = ['name', 'email', 'subject', 'message', 'created_at']
