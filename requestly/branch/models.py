from django.db import models
from base.models import BaseModel

class Branch(BaseModel):
        branch_number =  models.CharField(max_length=10, null=True,blank=True)
        branch_type = models.CharField(max_length=20, null=True,blank=True)
        branch_name = models.CharField(max_length=70,blank=True)
        branch_address = models.CharField(max_length=60,blank=True)
        branch_city = models.CharField(max_length=20,blank=True)
        branch_province = models.CharField(max_length=10,blank=True)
        branch_pc = models.CharField(max_length=10, blank=True)
        branch_phone = models.CharField(max_length=15,blank=True)
        branch_fax = models.CharField(max_length=15, blank=True)
        branch_url = models.CharField(max_length=70, blank=True)

        def __str__(self):
                return self.branch_name
        class Meta:
                verbose_name_plural = "Branch"

        
