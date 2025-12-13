from django.db import models
from django.urls import reverse
from ckeditor.fields import RichTextField


#модель предмета (Обществознание, Математика и т.д.)
class Subject(models.Model):
    title = models.CharField("Название предмета", max_length=100)
    slug = models.SlugField("URL", unique=True)
    icon = models.ImageField("Иконка", upload_to='subjects/', blank=True)


    def __str__(self):
        return self.title
    

#модель раздела (Блок 1, Блок 2...)
class Section(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='sections')
    title = models.CharField("Название раздела", max_length=200)
    order = models.PositiveIntegerField("Порядок вывода", default=0)


    class Meta:
        ordering = ['order']


    def __str__(self):
        return f"{self.subject.title} - {self.title}"


#модель темы
class Topic(models.Model):
    section = models.ForeignKey(Section, on_delete=models.CASCADE, related_name='topics')
    title = models.CharField("Название темы", max_length=255)
    code = models.CharField("Код темы", max_length=20, help_text="Например, 1.1.1")
    
    content = RichTextField("Теория (Конспект)") 


    def __str__(self):
        return f"{self.code} {self.title}"


    def get_absolute_url(self):
        return reverse('topic_detail', kwargs={'topic_id': self.pk})
    

#модель вопроса для тестов
class Question(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, related_name='questions')
    text = models.TextField("Текст вопроса")
    explanation = models.TextField("Пояснение к ответу", blank=True)


    def __str__(self):
        return self.text[:50]
    

#модель варианта ответа
class AnswerOption(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='options')
    text = models.CharField("Вариант ответа", max_length=255)
    is_correct = models.BooleanField("Правильный ли это ответ?", default=False)


    def __str__(self):
        return self.text