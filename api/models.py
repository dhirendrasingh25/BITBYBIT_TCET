from django.db import models

class Transaction(models.Model):
    transaction_id = models.IntegerField()
    item_name = models.CharField(max_length=50)
    total_items = models.IntegerField()

    def __str__(self):
        return f'Transaction {self.transaction_id}'

class UserData(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    username = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    password = models.CharField(max_length=50)
    friends = models.CharField(max_length=50)
    salary = models.IntegerField()
    transactions = models.ManyToManyField(Transaction)
    occupation = models.CharField(max_length=50)
    status_paid = models.BooleanField(default=False)
    status_unpaid = models.BooleanField(default=False)

    def __str__(self):
        return self.username

class User(models.Model):
    First_Name = models.CharField(max_length=50)
    Last_Name = models.CharField(max_length=50)
    Username = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.Username
