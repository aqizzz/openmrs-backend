from django.db import models
import uuid

class GlobalProperty(models.Model):
    property = models.CharField(primary_key=True, max_length=255)
    property_value = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    uuid = models.CharField(unique=True, max_length=38, default=uuid.uuid4)
    datatype = models.CharField(max_length=255, blank=True, null=True)
    datatype_config = models.TextField(blank=True, null=True)
    preferred_handler = models.CharField(max_length=255, blank=True, null=True)
    handler_config = models.TextField(blank=True, null=True)
    date_changed = models.DateTimeField(blank=True, null=True)
    changed_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='changed_by', blank=True, null=True)

    class Meta:
        # managed = False
        db_table = 'global_property'

class ReportObject(models.Model):
    report_object_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=1000, blank=True, null=True)
    report_object_type = models.CharField(max_length=255)
    report_object_sub_type = models.CharField(max_length=255)
    xml_data = models.TextField(blank=True, null=True)
    creator = models.ForeignKey('Users', models.DO_NOTHING, db_column='creator')
    date_created = models.DateTimeField()
    changed_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='changed_by', related_name='reportobject_changed_by_set', blank=True, null=True)
    date_changed = models.DateTimeField(blank=True, null=True)
    voided = models.IntegerField()
    voided_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='voided_by', related_name='reportobject_voided_by_set', blank=True, null=True)
    date_voided = models.DateTimeField(blank=True, null=True)
    void_reason = models.CharField(max_length=255, blank=True, null=True)
    uuid = models.CharField(unique=True, max_length=38, default=uuid.uuid4)

    class Meta:
        # managed = False
        db_table = 'report_object'


class ReportSchemaXml(models.Model):
    report_schema_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.TextField()
    xml_data = models.TextField()
    uuid = models.CharField(unique=True, max_length=38, default=uuid.uuid4)

    class Meta:
        # managed = False
        db_table = 'report_schema_xml'

class Hl7InArchive(models.Model):
    hl7_in_archive_id = models.AutoField(primary_key=True)
    hl7_source = models.IntegerField()
    hl7_source_key = models.CharField(max_length=255, blank=True, null=True)
    hl7_data = models.TextField()
    date_created = models.DateTimeField()
    message_state = models.IntegerField(blank=True, null=True)
    uuid = models.CharField(unique=True, max_length=38, default=uuid.uuid4)

    class Meta:
        # managed = False
        db_table = 'hl7_in_archive'


class Hl7InError(models.Model):
    hl7_in_error_id = models.AutoField(primary_key=True)
    hl7_source = models.IntegerField()
    hl7_source_key = models.TextField(blank=True, null=True)
    hl7_data = models.TextField()
    error = models.CharField(max_length=255)
    error_details = models.TextField(blank=True, null=True)
    date_created = models.DateTimeField()
    uuid = models.CharField(unique=True, max_length=38, default=uuid.uuid4)

    class Meta:
        # managed = False
        db_table = 'hl7_in_error'


class Hl7InQueue(models.Model):
    hl7_in_queue_id = models.AutoField(primary_key=True)
    hl7_source = models.ForeignKey('Hl7Source', models.DO_NOTHING, db_column='hl7_source')
    hl7_source_key = models.TextField(blank=True, null=True)
    hl7_data = models.TextField()
    message_state = models.IntegerField()
    date_processed = models.DateTimeField(blank=True, null=True)
    error_msg = models.TextField(blank=True, null=True)
    date_created = models.DateTimeField(blank=True, null=True)
    uuid = models.CharField(unique=True, max_length=38, default=uuid.uuid4)

    class Meta:
        # managed = False
        db_table = 'hl7_in_queue'


class Hl7Source(models.Model):
    hl7_source_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    creator = models.ForeignKey('Users', models.DO_NOTHING, db_column='creator')
    date_created = models.DateTimeField()
    uuid = models.CharField(unique=True, max_length=38, default=uuid.uuid4)

    class Meta:
        # managed = False
        db_table = 'hl7_source'


class ClobDatatypeStorage(models.Model):
    uuid = models.CharField(unique=True, max_length=38, default=uuid.uuid4)
    value = models.TextField()

    class Meta:
        # managed = False
        db_table = 'clob_datatype_storage'

