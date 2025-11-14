from django.db import models

class Usuario(models.Model):
    ROL_CHOICES = [
        ('trabajador', 'Trabajador'),
        ('empleador', 'Empleador'),
    ]

    nombre = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    contraseña = models.CharField(max_length=255)
    rol = models.CharField(max_length=20, choices=ROL_CHOICES)
    cc = models.CharField(max_length=20, unique=True)
    contacto = models.CharField(max_length=50)
    ubicacion = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.nombre} ({self.rol})"
