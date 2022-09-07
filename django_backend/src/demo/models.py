from django.db import models


ROLE_CHOICES = [
    ("M", "Member"),
    ("O", "Owner"),
    ("A", "Admin"),
]


class Person(models.Model):
    firstname = models.CharField(max_length=64, blank=True, null=True)
    lastname = models.CharField(max_length=64, blank=True, null=True)
    title = models.CharField(max_length=64, blank=True, null=True)
    email = models.EmailField(max_length=254)
    role = models.CharField(max_length=64, blank=True, null=True, choices=ROLE_CHOICES)
    likes_dogs = models.BooleanField()
    likes_cats = models.BooleanField()
    dob = models.DateField(auto_now=False, auto_now_add=False)
    bio = models.TextField()
    phone = models.CharField(max_length=16, blank=True, null=True)

    class Meta:
        verbose_name_plural = "People"
        ordering = ["id"]

    def __str__(self):
        return f"{self.firstname} {self.lastname}"