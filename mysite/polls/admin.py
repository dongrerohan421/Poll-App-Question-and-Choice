from django.contrib import admin

# Register your models here.
# Dev: Rohan
# Date: 09/03/2015

'''
from .models import Question

admin.site.register(Question)
'''
from django.contrib import admin

from .models import Choice, Question

# class ChoiceInline(admin.StackedInline):
class ChoiceInline(admin.TabularInline):    # Tabular way of displaying inline related objects
    model = Choice
    extra = 3

    
class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
        ]
    inlines = [ChoiceInline]
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['question_text']   # That adds a search box at the top of the change list. When somebody enters search terms, Django will search the question_text field.
        
admin.site.register(Question, QuestionAdmin)
# admin.site.register(Choice)
111
