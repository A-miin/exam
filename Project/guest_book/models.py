from django.db import models

status_choices = [('active', 'Активно'), ('blocked', 'Заблокировано')]
# Create your models here.
class Record(models.Model):
    name = models.CharField(null=False, blank=False, verbose_name="Имя автора")
    email = models.EmailField(null=False, blank=False, verbose_name="Почта автора записи")
    text = models.TextField(null=False, blank=False, verbose_name="Текст записи")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(null=False, blank=False,choices=status_choices, default='active' )

    class Meta:
        db_table='records'
        verbose_name="Запись"
        verbose_name_plural = "Записи"

    def __str__(self):
        return f'{self.id}. {self.name}({self.email})'