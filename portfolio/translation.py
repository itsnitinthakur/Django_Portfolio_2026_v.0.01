from modeltranslation.translator import TranslationOptions, register

from .models import Certificate, Experience, Hackathon, Project, Skill


@register(Skill)
class SkillTranslationOptions(TranslationOptions):
    fields = ('name',)


@register(Project)
class ProjectTranslationOptions(TranslationOptions):
    fields = ('title', 'description')


@register(Experience)
class ExperienceTranslationOptions(TranslationOptions):
    fields = ('title', 'location', 'description')


@register(Certificate)
class CertificateTranslationOptions(TranslationOptions):
    fields = ('title', 'description')


@register(Hackathon)
class HackathonTranslationOptions(TranslationOptions):
    fields = ('title', 'location', 'result', 'description', 'highlight')
