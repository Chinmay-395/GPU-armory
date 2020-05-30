from django.db import models

# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=100)
    Architecture = models.TextField(blank=True, null=True)
    Boost_Clock = models.IntegerField(blank=True, null=True)
    Core_Speed = models.IntegerField(blank=True, null=True)
    Memory = models.IntegerField(blank=True, null=True)
    Memory_Speed = models.CharField(max_length=20, blank=True, null=True)
    Memory_Bandwidth = models.CharField(max_length=20, blank=True, null=True)
    DVI_Connection = models.CharField(max_length=20, blank=True, null=True)
    Dedicated = models.CharField(max_length=20, blank=True, null=True)
    Direct_X = models.CharField(max_length=20, blank=True, null=True)
    HDMI_Connection = models.CharField(max_length=20, blank=True, null=True)
    Integrated = models.CharField(max_length=20, blank=True, null=True)
    L2_Cache = models.CharField(max_length=20, blank=True, null=True)
    Manufacturer = models.CharField(max_length=20, blank=True, null=True)
    Max_Power = models.CharField(max_length=20, blank=True, null=True)
    # The `Memory_Bus` field should be remained unchanged
    Memory_Bus = models.CharField(max_length=20, blank=True, null=True)

    Memory_Type = models.CharField(max_length=20, blank=True, null=True)
    Power_Connector = models.TextField(blank=True, null=True)
    Process = models.CharField(max_length=20, blank=True, null=True)
    Resolution_WxH = models.CharField(max_length=20, blank=True, null=True)
    SLI_Crossfire = models.CharField(max_length=20, blank=True, null=True)
    price = models.CharField(max_length=20, blank=True, null=True)
    url_name = models.TextField(blank=True, null=True)
    # image field
    img_of_gpu = models.ImageField(upload_to='pics', blank=True, null=True)

    def __str__(self):
        return f'{self.name} -->  {self.id}'


#wine_csv = open('ProjectGpu-withoutID.csv', 'r', encoding = "utf-8")
