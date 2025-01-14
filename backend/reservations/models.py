from django.db import models
from django.utils import timezone


class Employee(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Pracownik"
        verbose_name_plural = "Pracownicy"
        ordering = ['name']

class Customer(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    phone = models.CharField(max_length=15, blank=True, null=True)
    dog_name = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Klient"
        verbose_name_plural = "Klienci"
        ordering = ['name']

class Dog(models.Model):
    name = models.CharField(max_length=100)
    breed = models.CharField(max_length=50)
    owner = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='dogs')
    note = models.TextField(blank=True, null=True)
    last_visit = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.name} ({self.breed})"

    class Meta:
        verbose_name = "Pies"
        verbose_name_plural = "Psy"
        ordering = ['name']

class Visit(models.Model):
    date = models.DateField()
    time = models.TimeField()
    employees = models.ManyToManyField(Employee, related_name='visits')
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='visits')
    dogs = models.ManyToManyField(Dog, related_name='visits')
    purpose = models.TextField()
    table = models.CharField(max_length=100)
    # status = models
    # payment_method = models.Choices()

    def __str__(self):
        return f"Visit on {self.date} at {self.time} with {', '.join([dog.name for dog in self.dogs.all()])}"

    class Meta:
        verbose_name = "Wizyta"
        verbose_name_plural = "Wizyty"
        ordering = ['date', 'time']

class ActivityLog(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='logs')
    description = models.TextField()

    def __str__(self):
        return f"Log for {self.customer.name} at {self.timestamp}"

    class Meta:
        verbose_name = "Log"
        verbose_name_plural = "Logi"
        ordering = ['timestamp']