from django.db import models


class UserI(models.Model):
    phone = models.CharField(
        "Phone number",
        max_length=12,
    )
    name = models.CharField(
        "Name",
        max_length=145,
    )

    class Meta:
        verbose_name = "Пользовател"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return f"{self.name}"
