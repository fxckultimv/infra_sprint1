from django.contrib.auth import get_user_model
from django.db import models


User = get_user_model()


class Achievement(models.Model):
    name = models.CharField(max_length=64)

    class Meta:
        verbose_name = 'Достижение'
        verbose_name_plural = 'Достижения'

    def __str__(self):
        return self.name

class Cat(models.Model):
    name = models.CharField(max_length=16)
    color = models.CharField(max_length=16)
    birth_year = models.IntegerField()
    owner = models.ForeignKey(
        User, related_name='cats', 
        on_delete=models.CASCADE
        )
    achievements = models.ManyToManyField(Achievement, through='AchievementCat')
    image = models.ImageField(
        upload_to='cats/images/', 
        null=True,  
        default=None
        )


    class Meta:
        verbose_name = 'Кот'
        verbose_name_plural = 'Коты'

    def __str__(self):
        return self.name


class AchievementCat(models.Model):
    achievement = models.ForeignKey(Achievement, on_delete=models.CASCADE)
    cat = models.ForeignKey(Cat, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Достижение кота'
        verbose_name_plural = 'Достижения котов'

    def __str__(self):
        return f'{self.achievement} {self.cat}'

