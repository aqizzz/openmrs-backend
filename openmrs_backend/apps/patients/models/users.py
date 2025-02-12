from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from .patients import Person

# Create your models here.

class UsersManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("Email is required")
        email = self.normalize_email(email)
        person_data = extra_fields.get('person_data', {})
        person = Person.objects.create(
            gender=person_data.get('gender', ''),
            **person_data
        )
        user = self.model(email=email, **extra_fields)
        user.set_password(password)  # Django Default password encryption
        user.person = person
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)

class Users(AbstractBaseUser, PermissionsMixin):
    user_id = models.AutoField(primary_key=True)
    system_id = models.CharField(max_length=50)
    username = models.CharField(max_length=50, blank=True, null=True, unique=True)
    password = models.CharField(max_length=128, blank=True, null=True)
    salt = models.CharField(max_length=128, blank=True, null=True)
    secret_question = models.CharField(max_length=255, blank=True, null=True)
    secret_answer = models.CharField(max_length=255, blank=True, null=True)
    creator = models.ForeignKey('self', models.DO_NOTHING, db_column='creator', to_field='user_id', blank=True, null=True, related_name='users_creator')
    date_created = models.DateTimeField(auto_now_add=True)
    changed_by = models.ForeignKey(
        'self', models.DO_NOTHING, db_column='changed_by',
        related_name='users_changed_by_set', blank=True, null=True
    )
    date_changed = models.DateTimeField(blank=True, null=True)
    person = models.ForeignKey('Person', models.DO_NOTHING)
    retired = models.IntegerField(default=0)
    retired_by = models.ForeignKey(
        'self', models.DO_NOTHING, db_column='retired_by',
        related_name='users_retired_by_set', blank=True, null=True
    )
    date_retired = models.DateTimeField(blank=True, null=True)
    retire_reason = models.CharField(max_length=255, blank=True, null=True)
    uuid = models.CharField(max_length=38)
    activation_key = models.CharField(max_length=255, blank=True, null=True)
    email = models.CharField(unique=True, max_length=255, blank=True, null=True)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UsersManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
            return str(self.user_id)
    
    class Meta:
        # managed = False
        db_table = 'users'

class UserProperty(models.Model):
    user = models.OneToOneField('Users', models.DO_NOTHING, primary_key=True)  # The composite primary key (user_id, property) found, that is not supported. The first column is selected.
    property = models.CharField(max_length=255)
    property_value = models.TextField(blank=True, null=True)

    class Meta:
        # managed = False
        db_table = 'user_property'
        unique_together = (('user', 'property'),)

class Role(models.Model):
    role = models.CharField(primary_key=True, max_length=50)
    description = models.CharField(max_length=255, blank=True, null=True)
    uuid = models.CharField(unique=True, max_length=38)

    class Meta:
        # managed = False
        db_table = 'role'

class UserRole(models.Model):
    user = models.OneToOneField('Users', models.DO_NOTHING, primary_key=True)  # The composite primary key (user_id, role) found, that is not supported. The first column is selected.
    role = models.ForeignKey(Role, models.DO_NOTHING, db_column='role')

    class Meta:
        # managed = False
        db_table = 'user_role'
        unique_together = (('user', 'role'),)

class Privilege(models.Model):
    privilege = models.CharField(primary_key=True, max_length=255)
    description = models.TextField(blank=True, null=True)
    uuid = models.CharField(unique=True, max_length=38)

    class Meta:
        # # managed = False
        db_table = 'privilege'


class Provider(models.Model):
    provider_id = models.AutoField(primary_key=True)
    person = models.ForeignKey('patients.Person', models.DO_NOTHING, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    identifier = models.CharField(max_length=255, blank=True, null=True)
    creator = models.ForeignKey('Users', models.DO_NOTHING, db_column='creator')
    date_created = models.DateTimeField()
    changed_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='changed_by', related_name='provider_changed_by_set', blank=True, null=True)
    date_changed = models.DateTimeField(blank=True, null=True)
    retired = models.IntegerField()
    retired_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='retired_by', related_name='provider_retired_by_set', blank=True, null=True)
    date_retired = models.DateTimeField(blank=True, null=True)
    retire_reason = models.CharField(max_length=255, blank=True, null=True)
    uuid = models.CharField(unique=True, max_length=38)
    role = models.ForeignKey('Concept', models.DO_NOTHING, blank=True, null=True)
    speciality = models.ForeignKey('Concept', models.DO_NOTHING, related_name='provider_speciality_set', blank=True, null=True)

    class Meta:
        # managed = False
        db_table = 'provider'


class ProviderAttribute(models.Model):
    provider_attribute_id = models.AutoField(primary_key=True)
    provider = models.ForeignKey(Provider, models.DO_NOTHING)
    attribute_type = models.ForeignKey('ProviderAttributeType', models.DO_NOTHING)
    value_reference = models.TextField()
    uuid = models.CharField(unique=True, max_length=38)
    creator = models.ForeignKey('Users', models.DO_NOTHING, db_column='creator')
    date_created = models.DateTimeField()
    changed_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='changed_by', related_name='providerattribute_changed_by_set', blank=True, null=True)
    date_changed = models.DateTimeField(blank=True, null=True)
    voided = models.IntegerField()
    voided_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='voided_by', related_name='providerattribute_voided_by_set', blank=True, null=True)
    date_voided = models.DateTimeField(blank=True, null=True)
    void_reason = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        # managed = False
        db_table = 'provider_attribute'


class ProviderAttributeType(models.Model):
    provider_attribute_type_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=1024, blank=True, null=True)
    datatype = models.CharField(max_length=255, blank=True, null=True)
    datatype_config = models.TextField(blank=True, null=True)
    preferred_handler = models.CharField(max_length=255, blank=True, null=True)
    handler_config = models.TextField(blank=True, null=True)
    min_occurs = models.IntegerField()
    max_occurs = models.IntegerField(blank=True, null=True)
    creator = models.ForeignKey('Users', models.DO_NOTHING, db_column='creator')
    date_created = models.DateTimeField()
    changed_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='changed_by', related_name='providerattributetype_changed_by_set', blank=True, null=True)
    date_changed = models.DateTimeField(blank=True, null=True)
    retired = models.IntegerField()
    retired_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='retired_by', related_name='providerattributetype_retired_by_set', blank=True, null=True)
    date_retired = models.DateTimeField(blank=True, null=True)
    retire_reason = models.CharField(max_length=255, blank=True, null=True)
    uuid = models.CharField(unique=True, max_length=38)

    class Meta:
        # managed = False
        db_table = 'provider_attribute_type'


