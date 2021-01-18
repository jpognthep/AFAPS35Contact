from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# Username & Password => admin abc@@123

class TProvince(models.Model):
    name = models.CharField(max_length = 50,null = False)
    regione_CHOICES = (
        ('ภาคเหนือ', 'North'),
        ('ภาคใต้', 'South'),
        ('ภาคกลาง', 'Central'),
        ('ภาคตะวันออก', 'East'),
        ('ภาคตะวันออกเฉียงเหนือ', 'NorthEast'),
        ('ภาคตะวันตก', 'West'),
    )
    region = models.CharField(max_length=30, default='Central', choices = regione_CHOICES)

    def __str__(self):
        return "%20s : %s " % (self.region,self.name)

class TUserData(models.Model):
    isAdmin = models.OneToOneField(User,  null=True, blank=True,on_delete=models.CASCADE)
    title = models.CharField(max_length = 30, null = False)
    fName = models.CharField(max_length = 100, null = False)
    lName = models.CharField(max_length = 100, null = False)
    nickName = models.CharField(max_length = 50, null = False)
    service_CHOICES = (
        ('Army', 'Army'),
        ('Navy', 'Navy'),
        ('Airforce', 'Airforce'),
        ('Police', 'Police')
    )
    service = models.CharField(max_length=10, default='Airforce', choices=service_CHOICES)

    birthDay = models.DateField(blank = True)
    province = models.ForeignKey(TProvince, on_delete=models.DO_NOTHING, related_name='provinceWork')
    Domicile =  models.ForeignKey(TProvince, models.DO_NOTHING, related_name='provinceBirth',default = None, verbose_name = 'ภูมิลำเนา')
    officeName = models.CharField(max_length=200, verbose_name = 'หน่วยงาน/ที่ทำงาน',blank = True)
    mobilePhone = models.CharField(max_length=50,blank = True)
    officePhone = models.CharField(max_length=50,blank = True)
    business = models.TextField(blank = True, verbose_name = 'งานเสริม')
    hobby = models.TextField(blank = True, verbose_name = 'งานอดิเรก')
    note = models.TextField(blank = True , verbose_name ='บันทึก')
    shirtSize = models.CharField(max_length=50,null = True, verbose_name = 'เบอร์เสื้อ')
    wifeShirtSize = models.CharField(max_length=50,blank = True)
    kidShirtSize = models.CharField(max_length=50,blank = True)
    socialContact = models.CharField(max_length=50,blank = True)
    
    photo = models.ImageField(null = True,blank = True)

    def __str__(self):
        return "%s %s %s [%s] : %s" % (self.title,self.fName, self.lName, self.nickName,self.mobilePhone)


