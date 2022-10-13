from django.db import models

# Create your models here.
# class PmiCalculator(models.Model):
#     house_price = models.DecimalField(max_digits=10, decimal_places=2)
#     down_payment = models.DecimalField(max_digits=10, decimal_places=2)
#     interest_rate = models.DecimalField(max_digits=5, decimal_places=2)
#     loan_term = models.IntegerField()
#     monthly_pmi_payment = models.DecimalField(max_digits=6, decimal_places=2)
#     mortgage_amount = models.DecimalField(max_digits=10, decimal_places=2)
#     monthly_interest_rate = models.DecimalField(max_digits=5, decimal_places=2)
#     total_payment_periods = models.IntegerField()
#     monthly_mortgage_payment = models.DecimalField(max_digits=6, decimal_places=2)

# class FutureValueAnnuity(models.Model):
#     future_value = models.DecimalField(max_digits=30, decimal_places=2)
#     payment = models.DecimalField(max_digits=10, decimal_places=2)
#     interest_rate = models.DecimalField(max_digits=5, decimal_places=2)
#     number_periods = models.IntegerField()

#     def __str__(self):
#         return future_value

class MailingMember(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)

    def __str__(self):
        return self.name
