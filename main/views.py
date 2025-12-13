from django.shortcuts import render, get_object_or_404
from .models import Subject, Topic


def index(request):
    subjects = Subject.objects.all().order_by('title')

    return render(request, "main/index.html", {
        'subjects': subjects 
    })


def subject_detail(request, subject_slug):
    #получение предмета по слагу
    subject = get_object_or_404(Subject, slug=subject_slug)
    
    # Получение всех разделов (prefetch_related для оптимизации)
    sections = subject.sections.prefetch_related('topics').all()
    
    return render(request, 'main/subject_detail.html', {
        'subject': subject,
        'sections': sections
    })


def topic_detail(request, topic_id):
    # темы, вопросы и ответы к ним
    topic = get_object_or_404(Topic, pk=topic_id)
    questions = topic.questions.prefetch_related('options').all()
    
    return render(request, 'main/topic_detail.html', {
        'topic': topic,
        'questions': questions
    })