from django.contrib import admin
from .models import Category, Question, QuizAttempt

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('text', 'category', 'correct_option')
    list_filter = ('category',)
    search_fields = ('text',)

@admin.register(QuizAttempt)
class QuizAttemptAdmin(admin.ModelAdmin):
    list_display = ('player_name', 'category', 'score', 'total_questions', 'taken_at')
    list_filter = ('category', 'taken_at')
    search_fields = ('player_name',)
