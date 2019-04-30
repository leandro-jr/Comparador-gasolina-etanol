from django.db import models



class FuelConsumption(models.Model):
    year = models.CharField(max_length=64)
    brand = models.CharField(max_length=64)
    model = models.CharField(max_length=64)
    engine = models.CharField(max_length=64)
    version = models.CharField(max_length=255)
    fuel = models.CharField(max_length=64)
    km_per_liter_ethanol_city = models.FloatField()
    km_per_liter_ethanol_road = models.FloatField()
    km_per_liter_gas_city = models.FloatField()
    km_per_liter_gas_road = models.FloatField()

    def __str__(self):
        # return f"{self.brand} {self.model} {self.engine} {self.version} consumption is ethanol city: {self.km_per_liter_ethanol_city}, ethanol road: {self.km_per_liter_ethanol_road}, gas city: {self.km_per_liter_gas_city}, gas road: {self.km_per_liter_gas_road}"
        return f"{self.brand} {self.model} {self.version} {self.engine}({self.year})"

class FCShort(models.Model):
    year = models.CharField(max_length=64, default=0)
    brand = models.CharField(max_length=64, default=0)
    model = models.CharField(max_length=64, default=0)
    engine = models.CharField(max_length=64, default=0)
    version = models.CharField(max_length=64, default=0)
    fuel = models.CharField(max_length=64, default=0)
    km_per_liter_ethanol_city = models.FloatField(default=0)
    km_per_liter_ethanol_road = models.FloatField(default=0)
    km_per_liter_gas_city = models.FloatField(default=0)
    km_per_liter_gas_road = models.FloatField(default=0)

    def __str__(self):
        # return f"{self.brand} {self.model} {self.engine} {self.version} consumption is ethanol city: {self.km_per_liter_ethanol_city}, ethanol road: {self.km_per_liter_ethanol_road}, gas city: {self.km_per_liter_gas_city}, gas road: {self.km_per_liter_gas_road}"
        return f"{self.brand} {self.model} {self.version} {self.engine}({self.year})"

class Price(models.Model):
    date = models.CharField(max_length=64)
    product = models.CharField(max_length=64)
    region = models.CharField(max_length=64)
    state = models.CharField(max_length=64)
    city = models.CharField(max_length=64)
    avg_price = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.city}-{self.state}, {self.product} avg price was {self.avg_price} in {self.date}"

class Cities(models.Model):
    state = models.CharField(max_length=64)
    city = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.city}-{self.state}"

class States(models.Model):
    state_full = models.CharField(max_length=64)
    state_short = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.state_full}-{self.state_short}"
