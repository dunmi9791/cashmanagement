from django.db import models

# Create your models here.


class Inflow(models.Model):
    class ITypes(models.IntegerChoices):
        SAL = 1, "SALES"
        DIV = 2, "DIVIDEND"
        INT = 3, "INTEREST"
        RET = 4, "RETURN"
        OTH = 5, "OTHER"

    class RInterval(models.IntegerChoices):
        NA = 1, "N/A"
        DAY = 2, "DAYS"
        WEK = 3, "WEEKS"
        MON = 4, "MONTHS"
        YEA = 5, "YEARS"

    amount = models.FloatField()
    date = models.DateField()
    type = models.PositiveSmallIntegerField(choices=ITypes.choices)
    repetitive = models.BooleanField(default=False)
    repetition_interval = models.PositiveSmallIntegerField(choices=RInterval.choices, default=1)
    repetition_time = models.PositiveSmallIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Inflow {self.id} - {self.type} - {self.date.strftime("%Y/%m/%d")}'

    class Meta:
        verbose_name_plural = 'inflows'


class Outflow(models.Model):
    class OTypes(models.IntegerChoices):
        EXP = 1, "EXPENSES"
        COR = 2, "COST OF REVENUE"
        SAL = 3, "SALARIES"
        REN = 4, "RENT"
        OTH = 5, "OTHER"

    class RInterval(models.IntegerChoices):
        NA = 1, "N/A"
        DAY = 2, "DAYS"
        WEK = 3, "WEEKS"
        MON = 4, "MONTHS"
        YEA = 5, "YEARS"

    amount = models.FloatField()
    date = models.DateField()
    type = models.PositiveSmallIntegerField(choices=OTypes.choices)
    repetitive = models.BooleanField(default=False)
    repetition_interval = models.PositiveSmallIntegerField(choices=RInterval.choices, default=1)
    repetition_time = models.PositiveSmallIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Outflow {self.id} - {self.type} - {self.date.strftime("%Y/%m/%d")}'

    class Meta:
        verbose_name_plural = 'outflows'


class Balance(models.Model):
    amount = models.FloatField()
    date = models.DateField()
    type = models.CharField(max_length=64)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Balance {self.id} - {self.type} - {self.date.strftime("%Y/%m/%d")}'

    class Meta:
        verbose_name_plural = 'balance'
