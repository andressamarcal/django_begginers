# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from polls.models import Question, Choice


class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['question_text']
    

class ChoiceInline(admin.TabularInline):
    inlines = [ChoiceInline]


admin.site.register(Question, QuestionAdmin)
