from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
#
# class Product(models.Model):
#   product_name=models.TextField()
#   objects = models.Manager()
#   pdobjects = DataFrameManager()


class Train_data(models.Model):
    id = models.IntegerField(primary_key=True) # min: 3, max: 999990, mean: 499712.00722
    sex = models.PositiveSmallIntegerField(null=True, blank=True) # min: 1, max: 2, mean: 1.499904
    old = models.PositiveSmallIntegerField(null=True, blank=True) # min: 5, max: 18, mean: 10.421392
    city_sig = models.PositiveSmallIntegerField(null=True, blank=True) # min: 11, max: 49, mean: 33.614376
    height = models.PositiveSmallIntegerField(null=True, blank=True) # min: 135, max: 205, mean: 161.9795
    weight = models.PositiveSmallIntegerField(null=True, blank=True) # min: 30, max: 145, mean: 62.05638
    waist = models.PositiveSmallIntegerField(null=True, blank=True) # min: 48, max: 166, mean: 79.958884
    eye_left = models.PositiveSmallIntegerField(null=True, blank=True) # min: 0, max: 1, mean: 0.013892
    eye_right = models.PositiveSmallIntegerField(null=True, blank=True) # min: 0, max: 1, mean: 0.014052
    hearing_left = models.PositiveSmallIntegerField(null=True, blank=True) # min: 1, max: 2, mean: 1.030424
    hearing_right = models.PositiveSmallIntegerField(null=True, blank=True) # min: 1, max: 2, mean: 1.029456
    systolic_pressure = models.PositiveSmallIntegerField(null=True, blank=True) # min: 70, max: 236, mean: 121.438776
    diastolic_pressure = models.PositiveSmallIntegerField(null=True, blank=True) # min: 39, max: 151, mean: 75.451088
    fbs = models.PositiveSmallIntegerField(null=True, blank=True) # min: 18, max: 685, mean: 98.937808
    total_cholesterol = models.PositiveSmallIntegerField(null=True, blank=True) # min: 51, max: 296, mean: 192.881128
    triglycerides = models.PositiveSmallIntegerField(null=True, blank=True) # min: 1, max: 297, mean: 113.388876
    hdl = models.PositiveSmallIntegerField(null=True, blank=True) # min: 1, max: 97, mean: 56.790048
    ldl = models.FloatField(null=True, blank=True) # min: -12.2, max: 204.0, mean: 113.38690240000004
    hemoglobin = models.FloatField(null=True, blank=True) # min: 3.1, max: 24.0, mean: 14.080745199999802
    up = models.PositiveSmallIntegerField(null=True, blank=True) # min: 1, max: 6, mean: 1.086776
    serum_creatinine = models.FloatField(null=True, blank=True) # min: 0.1, max: 87.0, mean: 0.8616396000000133
    ast = models.PositiveSmallIntegerField(null=True, blank=True) # min: 1, max: 2890, mean: 24.997716
    alt = models.PositiveSmallIntegerField(null=True, blank=True) # min: 1, max: 5206, mean: 24.341336
    gamma = models.PositiveSmallIntegerField(null=True, blank=True) # min: 1, max: 999, mean: 33.369892
    smoke = models.PositiveSmallIntegerField(null=True, blank=True) # min: 1, max: 3, mean: 1.57258
    cavity_screen = models.PositiveSmallIntegerField(null=True, blank=True) # min: 0, max: 1, mean: 0.401572
    diabetes = models.PositiveSmallIntegerField(null=True, blank=True) # min: 0, max: 1, mean: 0.064648
    hypertension = models.PositiveSmallIntegerField(null=True, blank=True) # min: 0, max: 1, mean: 0.0378
    liver = models.PositiveSmallIntegerField(null=True, blank=True) # min: 0, max: 1, mean: 0.033004
    alcohol_hepatitis = models.PositiveSmallIntegerField(null=True, blank=True) # min: 0, max: 1, mean: 0.041848



class Person(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField(blank=True)
    birth_date = models.DateField()
    location = models.CharField(max_length=100, blank=True)

