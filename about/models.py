from django.db import models


#форма обратной связи
class EmailAddress(models.Model):
    email = models.EmailField('Email', max_length=120, blank=True, null=True)

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'Форма обратной связи'
        verbose_name_plural = 'Формы обратной связи'
