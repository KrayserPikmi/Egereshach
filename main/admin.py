from django.contrib import admin
from .models import Subject, Section, Topic, Question, AnswerOption 
from ckeditor.fields import RichTextField


class AnswerOptionInline(admin.TabularInline):
    model = AnswerOption
    extra = 1  


class QuestionInline(admin.StackedInline):
    model = Question
    inlines = [AnswerOptionInline]
    extra = 1


@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    list_display = ('code', 'title', 'section')
    list_filter = ('section__subject',)
    search_fields = ('title', 'code', 'content')
    inlines = [QuestionInline] 


class SectionInline(admin.TabularInline):
    model = Section
    extra = 1 
    fields = ('title', 'order') 


@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug')
    prepopulated_fields = {'slug': ('title',)} 
    inlines = [SectionInline] 


admin.site.register(Section) 
admin.site.register(Question)
