from django.db import models
import uuid


class Form(models.Model):
    form_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    version = models.CharField(max_length=50)
    build = models.IntegerField(blank=True, null=True)
    published = models.IntegerField()
    xslt = models.TextField(blank=True, null=True)
    template = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    encounter_type = models.ForeignKey('EncounterType', models.DO_NOTHING, db_column='encounter_type', blank=True, null=True)
    creator = models.ForeignKey('Users', models.DO_NOTHING, db_column='creator')
    date_created = models.DateTimeField()
    changed_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='changed_by', related_name='form_changed_by_set', blank=True, null=True)
    date_changed = models.DateTimeField(blank=True, null=True)
    retired = models.IntegerField()
    retired_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='retired_by', related_name='form_retired_by_set', blank=True, null=True)
    date_retired = models.DateTimeField(blank=True, null=True)
    retired_reason = models.CharField(max_length=255, blank=True, null=True)
    uuid = models.CharField(unique=True, max_length=38, default=uuid.uuid4)

    class Meta:
        # managed = False
        db_table = 'form'


class FormField(models.Model):
    form_field_id = models.AutoField(primary_key=True)
    form = models.ForeignKey(Form, models.DO_NOTHING)
    field = models.ForeignKey('Field', models.DO_NOTHING)
    field_number = models.IntegerField(blank=True, null=True)
    field_part = models.CharField(max_length=5, blank=True, null=True)
    page_number = models.IntegerField(blank=True, null=True)
    parent_form_field = models.ForeignKey('self', models.DO_NOTHING, db_column='parent_form_field', blank=True, null=True)
    min_occurs = models.IntegerField(blank=True, null=True)
    max_occurs = models.IntegerField(blank=True, null=True)
    required = models.IntegerField()
    changed_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='changed_by', blank=True, null=True)
    date_changed = models.DateTimeField(blank=True, null=True)
    creator = models.ForeignKey('Users', models.DO_NOTHING, db_column='creator', related_name='formfield_creator_set')
    date_created = models.DateTimeField()
    sort_weight = models.FloatField(blank=True, null=True)
    uuid = models.CharField(unique=True, max_length=38, default=uuid.uuid4)

    class Meta:
        # managed = False
        db_table = 'form_field'


class FormResource(models.Model):
    form_resource_id = models.AutoField(primary_key=True)
    form = models.ForeignKey(Form, models.DO_NOTHING)
    name = models.CharField(max_length=255)
    value_reference = models.TextField()
    datatype = models.CharField(max_length=255, blank=True, null=True)
    datatype_config = models.TextField(blank=True, null=True)
    preferred_handler = models.CharField(max_length=255, blank=True, null=True)
    handler_config = models.TextField(blank=True, null=True)
    uuid = models.CharField(unique=True, max_length=38, default=uuid.uuid4)
    date_changed = models.DateTimeField(blank=True, null=True)
    changed_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='changed_by', blank=True, null=True)

    class Meta:
        # managed = False
        db_table = 'form_resource'
        unique_together = (('form', 'name'),)

class Field(models.Model):
    field_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    field_type = models.ForeignKey('FieldType', models.DO_NOTHING, db_column='field_type', blank=True, null=True)
    concept = models.ForeignKey('Concept', models.DO_NOTHING, blank=True, null=True)
    table_name = models.CharField(max_length=50, blank=True, null=True)
    attribute_name = models.CharField(max_length=50, blank=True, null=True)
    default_value = models.TextField(blank=True, null=True)
    select_multiple = models.IntegerField()
    creator = models.ForeignKey('Users', models.DO_NOTHING, db_column='creator')
    date_created = models.DateTimeField()
    changed_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='changed_by', related_name='field_changed_by_set', blank=True, null=True)
    date_changed = models.DateTimeField(blank=True, null=True)
    retired = models.IntegerField()
    retired_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='retired_by', related_name='field_retired_by_set', blank=True, null=True)
    date_retired = models.DateTimeField(blank=True, null=True)
    retire_reason = models.CharField(max_length=255, blank=True, null=True)
    uuid = models.CharField(unique=True, max_length=38, default=uuid.uuid4)

    class Meta:
        # managed = False
        db_table = 'field'


class FieldAnswer(models.Model):
    field = models.OneToOneField('Field', models.DO_NOTHING, primary_key=True)  # The composite primary key (field_id, answer_id) found, that is not supported. The first column is selected.
    answer = models.ForeignKey('Concept', models.DO_NOTHING)
    creator = models.ForeignKey('Users', models.DO_NOTHING, db_column='creator')
    date_created = models.DateTimeField()
    uuid = models.CharField(unique=True, max_length=38, default=uuid.uuid4)

    class Meta:
        # managed = False
        db_table = 'field_answer'
        unique_together = (('field', 'answer'),)


class FieldType(models.Model):
    field_type_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    is_set = models.IntegerField()
    creator = models.ForeignKey('Users', models.DO_NOTHING, db_column='creator')
    date_created = models.DateTimeField()
    uuid = models.CharField(unique=True, max_length=38, default=uuid.uuid4)

    class Meta:
        # managed = False
        db_table = 'field_type'

