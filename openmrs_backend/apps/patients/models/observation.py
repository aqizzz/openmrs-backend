from django.db import models
import uuid

class Obs(models.Model):
    obs_id = models.AutoField(primary_key=True)
    person = models.ForeignKey('Person', models.DO_NOTHING)
    concept = models.ForeignKey('Concept', models.DO_NOTHING)
    encounter = models.ForeignKey('Encounter', models.DO_NOTHING, blank=True, null=True)
    order = models.ForeignKey('Orders', models.DO_NOTHING, blank=True, null=True)
    obs_datetime = models.DateTimeField()
    location = models.ForeignKey('Location', models.DO_NOTHING, blank=True, null=True)
    obs_group = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    accession_number = models.CharField(max_length=255, blank=True, null=True)
    value_group_id = models.IntegerField(blank=True, null=True)
    value_coded = models.ForeignKey('Concept', models.DO_NOTHING, db_column='value_coded', related_name='obs_value_coded_set', blank=True, null=True)
    value_coded_name = models.ForeignKey('ConceptName', models.DO_NOTHING, blank=True, null=True)
    value_drug = models.ForeignKey('Drug', models.DO_NOTHING, db_column='value_drug', blank=True, null=True)
    value_datetime = models.DateTimeField(blank=True, null=True)
    value_numeric = models.FloatField(blank=True, null=True)
    value_modifier = models.CharField(max_length=2, blank=True, null=True)
    value_text = models.TextField(blank=True, null=True)
    value_complex = models.CharField(max_length=1000, blank=True, null=True)
    comments = models.CharField(max_length=255, blank=True, null=True)
    creator = models.ForeignKey('Users', models.DO_NOTHING, db_column='creator')
    date_created = models.DateTimeField()
    voided = models.IntegerField()
    voided_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='voided_by', related_name='obs_voided_by_set', blank=True, null=True)
    date_voided = models.DateTimeField(blank=True, null=True)
    void_reason = models.CharField(max_length=255, blank=True, null=True)
    uuid = models.CharField(unique=True, max_length=38, default=uuid.uuid4)
    previous_version = models.ForeignKey('self', models.DO_NOTHING, db_column='previous_version', related_name='obs_previous_version_set', blank=True, null=True)
    form_namespace_and_path = models.CharField(max_length=255, blank=True, null=True)
    status = models.CharField(max_length=16)
    interpretation = models.CharField(max_length=32, blank=True, null=True)

    class Meta:
        # managed = False
        db_table = 'obs'

class Note(models.Model):
    note_id = models.IntegerField(primary_key=True)
    note_type = models.CharField(max_length=50, blank=True, null=True)
    patient = models.ForeignKey('Patient', models.DO_NOTHING, blank=True, null=True)
    obs = models.ForeignKey('Obs', models.DO_NOTHING, blank=True, null=True)
    encounter = models.ForeignKey('Encounter', models.DO_NOTHING, blank=True, null=True)
    text = models.TextField()
    priority = models.IntegerField(blank=True, null=True)
    parent = models.ForeignKey('self', models.DO_NOTHING, db_column='parent', blank=True, null=True)
    creator = models.ForeignKey('Users', models.DO_NOTHING, db_column='creator')
    date_created = models.DateTimeField()
    changed_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='changed_by', related_name='note_changed_by_set', blank=True, null=True)
    date_changed = models.DateTimeField(blank=True, null=True)
    uuid = models.CharField(unique=True, max_length=38, default=uuid.uuid4)

    class Meta:
        # managed = False
        db_table = 'note'
