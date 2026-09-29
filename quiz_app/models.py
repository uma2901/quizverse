from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    class Meta:
        verbose_name_plural = 'Categories'
        ordering = ['name']
    def __str__(self):
        return self.name

class Question(models.Model):
    OPTION_CHOICES = [('A','Option A'),('B','Option B'),('C','Option C'),('D','Option D')]
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='questions')
    text = models.CharField(max_length=300)
    option_a = models.CharField(max_length=200)
    option_b = models.CharField(max_length=200)
    option_c = models.CharField(max_length=200)
    option_d = models.CharField(max_length=200)
    correct_option = models.CharField(max_length=1, choices=OPTION_CHOICES)
    def __str__(self):
        return self.text
    def options(self):
        return [('A', self.option_a), ('B', self.option_b), ('C', self.option_c), ('D', self.option_d)]
    def correct_answer_text(self):
        return dict(self.options())[self.correct_option]

class QuizAttempt(models.Model):
    player_name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='attempts')
    score = models.IntegerField()
    total_questions = models.IntegerField()
    taken_at = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering = ['-score', 'taken_at']
    def __str__(self):
        return f"{self.player_name} - {self.score}/{self.total_questions} ({self.category})"
    def percentage(self):
        if self.total_questions == 0:
            return 0
        return round((self.score / self.total_questions) * 100)
