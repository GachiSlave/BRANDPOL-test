from django.db import models

# Create your models here.

class Tests(models.Model):
    is_available = models.BooleanField(default=True)
    title = models.CharField('Название',max_length=50, default='Тест ')
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return  f'/tests/{self.id}'

class Questions(models.Model):
    question_text = models.CharField("Вопрос",max_length=250, default='Вопрос:')
    test = models.ForeignKey(Tests, on_delete=models.CASCADE)

    def __str__(self):
        return self.question_text

    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'