from django.db import models
from django.db.models.fields import CharField


# Create your models here.

class Users(models.Model):
    userid = models.IntegerField(primary_key=True)
    age = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'users'


class Userrole(models.Model):
    user_address = models.CharField(max_length=255, blank=True, null=True)
    user_role = models.CharField(max_length=255, blank=True, null=True)
    userid = models.IntegerField()
    id = models.IntegerField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'userrole'


class Students(models.Model):
    student_id = models.IntegerField(primary_key=True)
    student_dept = models.CharField(max_length=45)
    student_name = models.CharField(max_length=45, blank=True, null=True)
    student_address = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'students'
        unique_together = (('student_id', 'student_dept'),)


class StudentDept(models.Model):
    id = models.IntegerField(primary_key=True)
    student = models.ForeignKey('Students', models.DO_NOTHING, blank=True, null=True)
    student_dept = models.CharField(max_length=45, blank=True, null=True)
    campus = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'student_dept'


class Customer(models.Model):
    customer_id = models.AutoField(db_column='CUSTOMER_ID', primary_key=True)  # Field name made lowercase.
    customer_namr = models.CharField(db_column='CUSTOMER_NAMR', max_length=45, blank=True, null=True)  # Field name made lowercase.
    customer_add = models.CharField(db_column='CUSTOMER_ADD', max_length=45, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'customer'