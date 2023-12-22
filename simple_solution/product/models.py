from django.db import models


class Item(models.Model):
    """Модель продукта"""
    name = models.CharField(max_length=255, verbose_name='Название')
    description = models.TextField(
        max_length=1000,
        verbose_name='Описание'
    )
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name='Цена'
    )
    currency = models.CharField(max_length=24, verbose_name='Валюта')

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        ordering = ('id',)

    def __str__(self):
        return f'{self.name}'


class Order(models.Model):
    """Модель заказа"""
    items = models.ManyToManyField(
        Item,
        through='OrderItem',
        verbose_name='Продукты'
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата создания'
    )

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'
        ordering = ('-created_at',)

    def __str__(self):
        items_list = ', '.join([item.name for item in self.items.all()])
        return f'Заказ {self.id}: {items_list}'


class OrderItem(models.Model):
    """Модель для создания аттрибута quantity в заказе"""
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    item = models.ForeignKey(
        Item,
        on_delete=models.CASCADE,
        verbose_name='Продукт'
    )
    quantity = models.PositiveIntegerField(
        default=1,
        verbose_name='Количество'
    )

    class Meta:
        verbose_name = 'Элемент заказа'
        verbose_name_plural = 'Элементы заказа'


class DiscountTax(models.Model):
    """
    Базовая (абстрактная) модель, или интерфейс,
    для моделей Tax и Discount.
    """
    order = models.ForeignKey(
        Order,
        on_delete=models.CASCADE,
        verbose_name='Заказ')
    amount = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name='Сумма'
    )

    class Meta:
        abstract = True

    def __str__(self):
        return f'{self.order} - {self.amount}'


class Discount(DiscountTax):
    """Модель скидки"""

    class Meta:
        verbose_name = 'Скидка'
        verbose_name_plural = 'Скидки'
        ordering = ('-id',)
        default_related_name = 'discounts'
        constraints = [
            models.UniqueConstraint(
                fields=['order', 'amount'],
                name='unique_order_discount',
            )
        ]

    def __str__(self):
        return f'Скидка {self.id}'


class Tax(DiscountTax):
    """Модель налога"""

    class Meta:
        verbose_name = 'Налог'
        verbose_name_plural = 'Налоги'
        ordering = ('-id',)
        default_related_name = 'taxes'
        constraints = [
            models.UniqueConstraint(
                fields=['order', 'amount'],
                name='unique_order_tax',
            )
        ]

    def __str__(self):
        return f'Налог {self.id}'
