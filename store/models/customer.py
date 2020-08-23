from django.db import models


class Customer(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    email = models.EmailField(max_length=20)
    password = models.CharField(max_length=50)
    mobile = models.CharField(max_length=15)

    def register(self):
        self.save()

    def is_exist(self):
        if Customer.objects.filter(email=self.email):
            return True
        else:
            return False
    @staticmethod
    def get_data_by_email(email):
        try:
            return Customer.objects.get(email=email)
        except:
            return False

