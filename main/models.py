from django.db. models import Model
from django.db import models

# Create your models here.



class Product(Model):
    name = models.CharField(max_length=300, verbose_name="Имя")
    price = models.DecimalField(verbose_name="Цена", max_digits=10, decimal_places=2)
    description =models.TextField(max_length=300, verbose_name="Описание")
    color = models.CharField(max_length=100, null=True, blank=True)
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, 
                                 verbose_name="Категория" , null=True, blank=True)

    


    # def clean(self):
    #     if self.marks.count() > 5:
    #         raise ValidationError("У студента не может быть больше 5 оценок.")

    # def save(self):
    #     self.full_clean()
    #     super().save()

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"

    def __str__(self):
        return f"{self.name}"



class Category(Model):
    name = models.CharField(max_length=300, verbose_name="Имя")
    category_count = models.IntegerField(verbose_name="Каличество категорий")



    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категорий"

    def __str__(self):
        return f"{self.name}"
    