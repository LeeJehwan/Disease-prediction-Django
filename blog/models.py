from django.db import models
from django.utils import timezone
from django import forms

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
    id = models.IntegerField(primary_key=True) # 가입자일련번호
  #  name = models.CharField(max_length=30)
    sex = models.PositiveSmallIntegerField(null=True, blank=True) # 성별코드
    old = models.PositiveSmallIntegerField(null=True, blank=True) # 연령대코드(5세단위)
    city_sig = models.PositiveSmallIntegerField(null=True, blank=True) # 시도코드
    height = models.PositiveSmallIntegerField(null=True, blank=True) # 신장(5Cm단위)
    weight = models.PositiveSmallIntegerField(null=True, blank=True) # 체중(5Kg단위)
    waist = models.PositiveSmallIntegerField(null=True, blank=True) # 허리둘레
    eye_left = models.PositiveSmallIntegerField(null=True, blank=True) # 시력(좌)
    eye_right = models.PositiveSmallIntegerField(null=True, blank=True) # 시력(우)
    hearing_left = models.PositiveSmallIntegerField(null=True, blank=True) # 청력(좌)
    hearing_right = models.PositiveSmallIntegerField(null=True, blank=True) # 청력(우)
    systolic_pressure = models.PositiveSmallIntegerField(null=True, blank=True) # 수축기혈압
    diastolic_pressure = models.PositiveSmallIntegerField(null=True, blank=True) # 이완기혈압
    fbs = models.PositiveSmallIntegerField(null=True, blank=True) # 식전혈당(공복혈당)
    total_cholesterol = models.PositiveSmallIntegerField(null=True, blank=True) # 총콜레스테롤
    triglycerides = models.PositiveSmallIntegerField(null=True, blank=True) # 트리글리세라이드
    hdl = models.PositiveSmallIntegerField(null=True, blank=True) # HDL콜레스테롤
    ldl = models.FloatField(null=True, blank=True) # LDL콜레스테롤
    hemoglobin = models.FloatField(null=True, blank=True) # 혈색소
    up = models.PositiveSmallIntegerField(null=True, blank=True) # 요단백
    serum_creatinine = models.FloatField(null=True, blank=True) # 혈청크레아티닌
    ast = models.PositiveSmallIntegerField(null=True, blank=True) # (혈청지오티)AST
    alt = models.PositiveSmallIntegerField(null=True, blank=True) # (혈청지오티)ALT
    gamma = models.PositiveSmallIntegerField(null=True, blank=True) # 감마지티피
    smoke = models.PositiveSmallIntegerField(null=True, blank=True) # 흡연상태
    cavity_screen = models.PositiveSmallIntegerField(null=True, blank=True) # 구강검진 수검여부
    diabetes = models.PositiveSmallIntegerField(null=True, blank=True) # 당뇨병 의사 판정
    hypertension = models.PositiveSmallIntegerField(null=True, blank=True) # 고혈압 의사 판정
    liver = models.PositiveSmallIntegerField(null=True, blank=True) # 간기능 이상여부
    alcohol_hepatitis = models.PositiveSmallIntegerField(null=True, blank=True) # 알콜성간염여부



class Person(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField(blank=True)
    birth_date = models.DateField()
    location = models.CharField(max_length=100, blank=True)


CHOICES = (
    ('당뇨병', '당뇨병'),
    ('고혈압', '고혈압'),
    ('이상지질혈증', '이상지질혈증')
)
GEN_CHOICES = (
    (1, '남'),
    (2, '여')
)
TEE_CHOICES = (
    (0, '아니오'),
    (1, '예')
)

class Person1_train(models.Model):
    reg_no = models.AutoField(primary_key=True) # 가입자일련번호
    name = models.CharField(max_length=30) # 이름
    gender = models.IntegerField(choices=GEN_CHOICES, default="남")  # 성별코드
    age = models.PositiveSmallIntegerField()  # 연령대코드(5세단위)
    height = models.PositiveSmallIntegerField()  # 신장(5Cm단위)
    weight = models.PositiveSmallIntegerField()  # 체중(5Kg단위)
    waist = models.PositiveSmallIntegerField()  # 허리둘레
    systolic_pressure = models.PositiveSmallIntegerField()  # 수축기혈압
    diastolic_pressure = models.PositiveSmallIntegerField()  # 이완기혈압
    cavity_screen = models.IntegerField(choices=TEE_CHOICES, default="아니오")
    disease = models.CharField(choices=CHOICES, max_length=30, default="당뇨병")



    def __str__(self):
        return self.name


ALCOHOL_CHOICES=(
    (1, '알콜성 간염'),
    (0, '정상')
)

SMOKE_CHOICES=(
    (1, '비흡연'),
    (2, '금연'),
    (3, '흡연')
)
GEN_CHOICES = (
    (1, '남'),
    (2, '여')
)

LOC_CHOICES = (
    (11,'서울'),(26,'부산'),(27,'대구'),(29,'인천'),(30,'대전'),(31,'울산'),(36,'세종'),
    (41,'경기도'),(42,'강원도'),(43,'충북'),(44,'충남'),(45,'전북'),(46,'전남'),
    (47,'경북'),(48,'경남'),(49,'제주')
)

class M1_Train_data(models.Model):
    bmi = models.FloatField(null=True, blank=True)
    location = models.IntegerField(choices=LOC_CHOICES, default="서울")
    triglycerides = models.FloatField(null=True, blank=True)
    hdl = models.FloatField(null=True, blank=True)  # min: 1, max: 97, mean: 56.790048
    ldl = models.FloatField(null=True, blank=True)  # min: -12.2, max: 204.0, mean: 113.38690240000004
    sex = models.IntegerField(choices=GEN_CHOICES, default="남")  # min: 1, max: 2, mean: 1.499904
    waist = models.FloatField(null=True, blank=True)  # min: 48, max: 166, mean: 79.958884
    systolic_pressure = models.FloatField(null=True, blank=True)  # min: 70, max: 236, mean: 121.438776
    diastolic_pressure = models.FloatField(null=True, blank=True)  # min: 39, max: 151, mean: 75.451088
    fbs = models.FloatField(null=True, blank=True)  # min: 18, max: 685, mean: 98.937808
    old = models.PositiveSmallIntegerField(null=True, blank=True)  # min: 5, max: 18, mean: 10.421392
    smoke = models.IntegerField(choices=SMOKE_CHOICES, default="금연")  # min: 1, max: 3, mean: 1.57258
    alcohol_hepatitis = models.IntegerField(choices=ALCOHOL_CHOICES, default='정상')  # min: 0, max: 1, mean: 0.041848

