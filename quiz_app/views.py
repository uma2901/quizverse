from django.shortcuts import render, redirect, get_object_or_404
from .models import Category, Question, QuizAttempt

def home(request):
    categories = Category.objects.all()
    return render(request, 'quiz_app/home.html', {'categories': categories})

def start_quiz(request):
    if request.method == 'POST':
        player_name = request.POST.get('player_name', '').strip() or 'Anonymous'
        category_id = request.POST.get('category')
        if not category_id:
            categories = Category.objects.all()
            return render(request, 'quiz_app/home.html', {'categories': categories, 'error': 'Please choose a category to begin.'})
        request.session['player_name'] = player_name
        request.session['category_id'] = category_id
        return redirect('quiz', category_id=category_id)
    return redirect('home')

def quiz(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    questions = list(category.questions.all())
    player_name = request.session.get('player_name', 'Anonymous')
    if not questions:
        return render(request, 'quiz_app/home.html', {'categories': Category.objects.all(), 'error': f'"{category.name}" has no questions yet. Please choose another category.'})
    return render(request, 'quiz_app/quiz.html', {'category': category, 'questions': questions, 'player_name': player_name})

def submit_quiz(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    questions = list(category.questions.all())
    player_name = request.session.get('player_name', 'Anonymous')
    if request.method != 'POST':
        return redirect('quiz', category_id=category_id)
    score = 0
    results = []
    for question in questions:
        selected = request.POST.get(f'question_{question.id}')
        is_correct = (selected == question.correct_option)
        if is_correct:
            score += 1
        results.append({'question': question, 'selected': selected, 'is_correct': is_correct})
    QuizAttempt.objects.create(player_name=player_name, category=category, score=score, total_questions=len(questions))
    return render(request, 'quiz_app/result.html', {
        'category': category, 'player_name': player_name, 'score': score,
        'total': len(questions), 'percentage': round((score/len(questions))*100) if questions else 0,
        'results': results,
    })

def leaderboard(request):
    top_attempts = QuizAttempt.objects.all().order_by('-score', 'taken_at')[:10]
    return render(request, 'quiz_app/leaderboard.html', {'top_attempts': top_attempts})
