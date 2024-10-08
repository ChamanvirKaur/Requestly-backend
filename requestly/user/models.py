from django.db import models
from base.models import BaseModel
from django.contrib.auth.models import AbstractUser
from shortuuidfield import ShortUUIDField
from autodatetimefields.models import AutoDateTimeField
from branch.models import Branch

class UserDetail(BaseModel,AbstractUser):
           phone=models.CharField(max_length=14,unique=True, null=True)
           street_address=models.CharField(max_length=50, null=True, blank= True)
           province=models.CharField(max_length=50,null=True,blank=True)

           def __str__(self):
                   return self.email
        
           class Meta:
                   verbose_name_plural = 'User Detail'
           
           
class ticket(models.Model):
        state=(
                ('New', 'New'),
                ('In Progress', 'In Progress'),
                ('On Hold', 'On Hold'),
                ('Complete', 'Complete'),
                ('Rejected','Rejected')

        )

        ticket_number=ShortUUIDField(unique=True)
        ticket_type = models.CharField(max_length=70, blank= True)
        ticket_category=models.CharField(max_length=30, null= True, blank=True)
        description=models.TextField(max_length=200)
        budget = models.CharField(max_length=10, blank=True, null=True)
        file_upload = models.FileField(blank=True, null=True)
        created_by=models.ForeignKey(UserDetail, on_delete=models.DO_NOTHING)
        estimated_completion=models.DateTimeField(blank=True, null=True)
        created_on = models.DateTimeField(auto_now_add=True)
        modified_on = AutoDateTimeField(auto_now=True)
        # requested_branch = models.ForeignKey(Branch, on_delete=models.CASCADE)
        requested_branch = models.CharField(max_length=90, null=True, blank=True)
        ticket_state = models.CharField(max_length=30, choices=state,null=True,blank=True,default='New')
        comments = models.TextField(max_length=250, null=True,blank=True)  

        def __str__(self):
                return self.ticket_number
        class Meta:
                verbose_name_plural = "Ticket"

# class Branch(BaseModel):
#         branch_number =  models.CharField(max_length=10, null=True,blank=True)
#         branch_type = models.CharField(max_length=20, null=True,blank=True)
#         branch_name = models.CharField(max_length=70,blank=True)
#         branch_address = models.CharField(max_length=60,blank=True)
#         branch_city = models.CharField(max_length=20,blank=True)
#         branch_province = models.CharField(max_length=10,blank=True)
#         branch_pc = models.CharField(max_length=10, blank=True)
#         branch_phone = models.CharField(max_length=15,blank=True)
#         branch_fax = models.CharField(max_length=15, blank=True)
#         branch_url = models.CharField(max_length=70, blank=True)

#         def __str__(self):
#                 return self.branch_name
#         class Meta:
#                 verbose_name_plural = "Branch"



        
                




        

        
