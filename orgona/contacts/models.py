import uuid

from django.db import models

# Create your models here.
class Religion(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )

    libelle = models.CharField(
        max_length=100,
        unique=True
    )

    def __str__(self):
        return self.libelle


class Category(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )

    libelle = models.CharField(
        max_length=100,
        unique=True
    )

    color = models.CharField(
        max_length=20,
        default="#0083fe"
    )

    def __str__(self):
        return self.libelle
    
class Contact(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )

    username = models.CharField(
        max_length=100,
        unique=True
    )

    firstname = models.CharField(
        max_length=100,
        blank=True,
        null=True
    )

    lastname = models.CharField(
        max_length=100,
        blank=True,
        null=True
    )

    email = models.EmailField(
        blank=True,
        null=True
    )

    religion = models.ForeignKey(
        Religion,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="contacts"
    )

    categories = models.ManyToManyField(
        Category,
        blank=True,
        related_name="contacts"
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    def __str__(self):
        return f"{self.firstname} {self.lastname}"


class Phone(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )

    contact = models.ForeignKey(
        Contact,
        on_delete=models.CASCADE,
        related_name="phones"
    )

    numero = models.CharField(
        max_length=30
    )

    prefixe = models.CharField(
        max_length=10,
        blank=True,
        null=True
    )

    is_whatsapp = models.BooleanField(
        default=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.numero
