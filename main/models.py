from django.db. models import Model
from django.db import models

class Product(models.Model):
    avatar = models.ImageField(
    upload_to='avatars/',
    verbose_name='Аватарка'
    )
    name = models.CharField(verbose_name="Имя: ", max_length=200)
    price = models.DecimalField(verbose_name="Цена: ", max_digits=10, decimal_places=2)

    def __str__(self):
       return self.name
 
    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"


























































# from django.db import models

# class Category(models.Model):
#     name = models.CharField(max_length=100)

#     def __str__(self):
#         return self.name


# class Product(models.Model):
#     name = models.CharField(max_length=200)
#     price = models.DecimalField(max_digits=10, decimal_places=2)
#     image = models.ImageField(upload_to='Продукты/', blank=True)

#     def __str__(self):
#         return self.name

#     class Meta:
#         verbose_name = "Продукт"
#         verbose_name_plural = "Продукты"


# class Order(models.Model):
#     STATUS = [
#         ('new', 'Новый'),
#         ('processing', 'В обработке'),
#         ('delivered', 'Доставлен'),
#         ('cancelled', 'Отменён'),
#     ]

#     customer_name = models.CharField(max_length=100)
#     phone = models.CharField(max_length=20)
#     address = models.TextField()

#     status = models.CharField(
#         max_length=20,
#         choices=STATUS,
#         default='new'
#     )

#     def __str__(self):
#         return self.customer_name

#     class Meta:
#         verbose_name = "Заказ"
#         verbose_name_plural = "Заказы"


# class OrderItem(models.Model):
#     order = models.ForeignKey(Order, on_delete=models.CASCADE)
#     product = models.ForeignKey(Product, on_delete=models.CASCADE)
#     quantity = models.PositiveIntegerField(default=1)

#     def __str__(self):
#         return f"{self.product.name} x {self.quantity}"
# # Create your models here.








from django.db import models

# ── Kategoriya ──────────────────────────────────────
class Kategoriya(models.Model):
    nomi = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    emoji = models.CharField(max_length=10, blank=True)

    def __str__(self):
        return self.nomi

    class Meta:
        verbose_name = "Kategoriya"
        verbose_name_plural = "Kategoriyalar"


# ── Mahsulot ─────────────────────────────────────────
class Mahsulot(models.Model):
    nomi        = models.CharField(max_length=200)
    tavsif      = models.TextField(blank=True)
    narx        = models.DecimalField(max_digits=10, decimal_places=2)
    eski_narx   = models.DecimalField(max_digits=10, decimal_places=2,
                                      null=True, blank=True)
    rasm        = models.ImageField(upload_to='mahsulotlar/', blank=True)
    kategoriya  = models.ForeignKey(Kategoriya, on_delete=models.CASCADE,
                                    related_name='mahsulotlar')
    reyting     = models.PositiveSmallIntegerField(default=5)
    badge       = models.CharField(max_length=50, blank=True)  # "Aksiya", "Yangi"
    yaratilgan  = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nomi

    class Meta:
        verbose_name = "Mahsulot"
        verbose_name_plural = "Mahsulotlar"
        ordering = ['-yaratilgan']


# ── Buyurtma ─────────────────────────────────────────
class Buyurtma(models.Model):
    HOLAT = [
        ('yangi',      'Yangi'),
        ('jarayonda',  'Jarayonda'),
        ('yetkazildi', 'Yetkazildi'),
        ('bekor',      'Bekor qilindi'),
    ]
    mijoz_ismi    = models.CharField(max_length=100)
    telefon       = models.CharField(max_length=20)
    manzil        = models.TextField()
    holat         = models.CharField(max_length=20, choices=HOLAT,
                                     default='yangi')
    yaratilgan    = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.mijoz_ismi} — {self.holat}"

    class Meta:
        verbose_name = "Buyurtma"
        verbose_name_plural = "Buyurtmalar"
        ordering = ['-yaratilgan']


# ── Buyurtma qatori ───────────────────────────────────
class BuyurtmaQatori(models.Model):
    buyurtma  = models.ForeignKey(Buyurtma, on_delete=models.CASCADE,
                                  related_name='qatorlar')
    mahsulot  = models.ForeignKey(Mahsulot, on_delete=models.CASCADE)
    miqdor    = models.PositiveIntegerField(default=1)
    narx      = models.DecimalField(max_digits=10, decimal_places=2)

    def jami(self):
        return self.narx * self.miqdor

    def __str__(self):
        return f"{self.mahsulot.nomi} x {self.miqdor}"