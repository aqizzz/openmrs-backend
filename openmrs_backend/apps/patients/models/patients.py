from django.db import models
import uuid

# Create your models here.
class Conditions(models.Model):
    condition_id = models.AutoField(primary_key=True)
    additional_detail = models.CharField(max_length=255, blank=True, null=True)
    previous_version = models.ForeignKey('self', models.DO_NOTHING, db_column='previous_version', blank=True, null=True)
    condition_coded = models.ForeignKey('Concept', models.DO_NOTHING, db_column='condition_coded', blank=True, null=True)
    condition_non_coded = models.CharField(max_length=255, blank=True, null=True)
    condition_coded_name = models.ForeignKey('ConceptName', models.DO_NOTHING, db_column='condition_coded_name', blank=True, null=True)
    clinical_status = models.CharField(max_length=50)
    verification_status = models.CharField(max_length=50, blank=True, null=True)
    onset_date = models.DateTimeField(blank=True, null=True)
    date_created = models.DateTimeField()
    voided = models.IntegerField()
    date_voided = models.DateTimeField(blank=True, null=True)
    void_reason = models.CharField(max_length=255, blank=True, null=True)
    uuid = models.CharField(unique=True, max_length=38, blank=True, null=True)
    creator = models.ForeignKey('Users', models.DO_NOTHING, db_column='creator')
    voided_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='voided_by', related_name='conditions_voided_by_set', blank=True, null=True)
    changed_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='changed_by', related_name='conditions_changed_by_set', blank=True, null=True)
    patient = models.ForeignKey('Patient', models.DO_NOTHING)
    end_date = models.DateTimeField(blank=True, null=True)
    date_changed = models.DateTimeField(blank=True, null=True)
    encounter = models.ForeignKey('Encounter', models.DO_NOTHING, blank=True, null=True)
    form_namespace_and_path = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        # managed = False
        db_table = 'conditions'

class Modality(models.Model):
    name = models.CharField(max_length=25, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    ip = models.CharField(max_length=20)
    port = models.IntegerField()
    timeout = models.IntegerField()
    order_type = models.ForeignKey('OrderType', models.DO_NOTHING)

    class Meta:
        # managed = False
        db_table = 'modality'

class Patient(models.Model):
    patient = models.OneToOneField('Person', models.DO_NOTHING, primary_key=True)
    creator = models.ForeignKey('Users', models.DO_NOTHING, db_column='creator')
    date_created = models.DateTimeField()
    changed_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='changed_by', related_name='patient_changed_by_set', blank=True, null=True)
    date_changed = models.DateTimeField(blank=True, null=True)
    voided = models.IntegerField()
    voided_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='voided_by', related_name='patient_voided_by_set', blank=True, null=True)
    date_voided = models.DateTimeField(blank=True, null=True)
    void_reason = models.CharField(max_length=255, blank=True, null=True)
    allergy_status = models.CharField(max_length=50)

    class Meta:
        # managed = False
        db_table = 'patient'

class PatientIdentifier(models.Model):
    patient_identifier_id = models.AutoField(primary_key=True)
    patient = models.ForeignKey(Patient, models.DO_NOTHING)
    identifier = models.CharField(max_length=50)
    identifier_type = models.ForeignKey('PatientIdentifierType', models.DO_NOTHING, db_column='identifier_type')
    preferred = models.IntegerField()
    location = models.ForeignKey('Location', models.DO_NOTHING, blank=True, null=True)
    creator = models.ForeignKey('Users', models.DO_NOTHING, db_column='creator')
    date_created = models.DateTimeField()
    date_changed = models.DateTimeField(blank=True, null=True)
    changed_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='changed_by', related_name='patientidentifier_changed_by_set', blank=True, null=True)
    voided = models.IntegerField()
    voided_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='voided_by', related_name='patientidentifier_voided_by_set', blank=True, null=True)
    date_voided = models.DateTimeField(blank=True, null=True)
    void_reason = models.CharField(max_length=255, blank=True, null=True)
    uuid = models.CharField(unique=True, max_length=38, default=uuid.uuid4)
    patient_program = models.ForeignKey('PatientProgram', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        # managed = False
        db_table = 'patient_identifier'


class PatientIdentifierType(models.Model):
    patient_identifier_type_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True, null=True)
    format = models.CharField(max_length=255, blank=True, null=True)
    check_digit = models.IntegerField()
    creator = models.ForeignKey('Users', models.DO_NOTHING, db_column='creator')
    date_created = models.DateTimeField()
    required = models.IntegerField()
    format_description = models.CharField(max_length=255, blank=True, null=True)
    validator = models.CharField(max_length=200, blank=True, null=True)
    location_behavior = models.CharField(max_length=50, blank=True, null=True)
    retired = models.IntegerField()
    retired_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='retired_by', related_name='patientidentifiertype_retired_by_set', blank=True, null=True)
    date_retired = models.DateTimeField(blank=True, null=True)
    retire_reason = models.CharField(max_length=255, blank=True, null=True)
    uuid = models.CharField(unique=True, max_length=38, default=uuid.uuid4)
    uniqueness_behavior = models.CharField(max_length=50, blank=True, null=True)
    date_changed = models.DateTimeField(blank=True, null=True)
    changed_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='changed_by', related_name='patientidentifiertype_changed_by_set', blank=True, null=True)

    class Meta:
        # managed = False
        db_table = 'patient_identifier_type'

class PatientflagsDisplaypoint(models.Model):
    displaypoint_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=1000, blank=True, null=True)
    creator = models.IntegerField()
    date_created = models.DateTimeField()
    changed_by = models.IntegerField(blank=True, null=True)
    date_changed = models.DateTimeField(blank=True, null=True)
    retired = models.IntegerField()
    retired_by = models.IntegerField(blank=True, null=True)
    date_retired = models.DateTimeField(blank=True, null=True)
    retire_reason = models.CharField(max_length=255, blank=True, null=True)
    uuid = models.CharField(max_length=38, default=uuid.uuid4)

    class Meta:
        # managed = False
        db_table = 'patientflags_displaypoint'


class PatientflagsFlag(models.Model):
    flag_id = models.AutoField(primary_key=True)
    name = models.CharField(unique=True, max_length=255)
    criteria = models.CharField(max_length=5000)
    message = models.CharField(max_length=255)
    enabled = models.IntegerField()
    evaluator = models.CharField(max_length=255)
    description = models.CharField(max_length=1000, blank=True, null=True)
    creator = models.IntegerField()
    date_created = models.DateTimeField()
    changed_by = models.IntegerField(blank=True, null=True)
    date_changed = models.DateTimeField(blank=True, null=True)
    retired = models.IntegerField()
    retired_by = models.IntegerField(blank=True, null=True)
    date_retired = models.DateTimeField(blank=True, null=True)
    retire_reason = models.CharField(max_length=255, blank=True, null=True)
    uuid = models.CharField(max_length=38, default=uuid.uuid4)
    priority_id = models.IntegerField(blank=True, null=True)

    class Meta:
        # managed = False
        db_table = 'patientflags_flag'


class PatientflagsFlagTag(models.Model):
    flag = models.ForeignKey(PatientflagsFlag, models.DO_NOTHING)
    tag = models.ForeignKey('PatientflagsTag', models.DO_NOTHING)

    class Meta:
        # managed = False
        db_table = 'patientflags_flag_tag'


class PatientflagsPatientFlag(models.Model):
    patient_flag_id = models.AutoField(primary_key=True)
    patient = models.ForeignKey(Patient, models.DO_NOTHING)
    flag = models.ForeignKey(PatientflagsFlag, models.DO_NOTHING)
    uuid = models.CharField(max_length=38, default=uuid.uuid4)
    message = models.CharField(max_length=255, blank=True, null=True)
    voided = models.IntegerField()
    voided_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='voided_by', blank=True, null=True)
    date_voided = models.DateTimeField(blank=True, null=True)
    void_reason = models.CharField(max_length=255, blank=True, null=True)
    creator = models.ForeignKey('Users', models.DO_NOTHING, db_column='creator', related_name='patientflagspatientflag_creator_set')
    date_created = models.DateTimeField(blank=True, null=True)
    changed_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='changed_by', related_name='patientflagspatientflag_changed_by_set', blank=True, null=True)
    date_changed = models.DateTimeField(blank=True, null=True)

    class Meta:
        # managed = False
        db_table = 'patientflags_patient_flag'


class PatientflagsPriority(models.Model):
    priority_id = models.AutoField(primary_key=True)
    name = models.CharField(unique=True, max_length=255)
    style = models.CharField(max_length=255)
    p_rank = models.IntegerField(blank=True, null=True)
    description = models.CharField(max_length=1000, blank=True, null=True)
    creator = models.IntegerField()
    date_created = models.DateTimeField()
    changed_by = models.IntegerField(blank=True, null=True)
    date_changed = models.DateTimeField(blank=True, null=True)
    retired = models.IntegerField()
    retired_by = models.IntegerField(blank=True, null=True)
    date_retired = models.DateTimeField(blank=True, null=True)
    retire_reason = models.CharField(max_length=255, blank=True, null=True)
    uuid = models.CharField(max_length=38, default=uuid.uuid4)

    class Meta:
        # managed = False
        db_table = 'patientflags_priority'


class PatientflagsTag(models.Model):
    tag_id = models.AutoField(primary_key=True)
    name = models.CharField(unique=True, max_length=255, blank=True, null=True)
    description = models.CharField(max_length=1000, blank=True, null=True)
    creator = models.IntegerField()
    date_created = models.DateTimeField()
    changed_by = models.IntegerField(blank=True, null=True)
    date_changed = models.DateTimeField(blank=True, null=True)
    retired = models.IntegerField()
    retired_by = models.IntegerField(blank=True, null=True)
    date_retired = models.DateTimeField(blank=True, null=True)
    retire_reason = models.CharField(max_length=255, blank=True, null=True)
    uuid = models.CharField(max_length=38, default=uuid.uuid4)

    class Meta:
        # managed = False
        db_table = 'patientflags_tag'


class PatientflagsTagDisplaypoint(models.Model):
    tag = models.ForeignKey(PatientflagsTag, models.DO_NOTHING)
    displaypoint = models.ForeignKey(PatientflagsDisplaypoint, models.DO_NOTHING)

    class Meta:
        # managed = False
        db_table = 'patientflags_tag_displaypoint'


class PatientflagsTagRole(models.Model):
    tag = models.ForeignKey(PatientflagsTag, models.DO_NOTHING)
    role = models.ForeignKey('Role', models.DO_NOTHING, db_column='role')

    class Meta:
        # managed = False
        db_table = 'patientflags_tag_role'


class Visit(models.Model):
    visit_id = models.AutoField(primary_key=True)
    patient = models.ForeignKey(Patient, models.DO_NOTHING)
    visit_type = models.ForeignKey('VisitType', models.DO_NOTHING)
    date_started = models.DateTimeField()
    date_stopped = models.DateTimeField(blank=True, null=True)
    indication_concept = models.ForeignKey('Concept', models.DO_NOTHING, blank=True, null=True)
    location = models.ForeignKey('Location', models.DO_NOTHING, blank=True, null=True)
    creator = models.ForeignKey('Users', models.DO_NOTHING, db_column='creator')
    date_created = models.DateTimeField()
    changed_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='changed_by', related_name='visit_changed_by_set', blank=True, null=True)
    date_changed = models.DateTimeField(blank=True, null=True)
    voided = models.IntegerField()
    voided_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='voided_by', related_name='visit_voided_by_set', blank=True, null=True)
    date_voided = models.DateTimeField(blank=True, null=True)
    void_reason = models.CharField(max_length=255, blank=True, null=True)
    uuid = models.CharField(unique=True, max_length=38, default=uuid.uuid4)

    class Meta:
        managed = False
        db_table = 'visit'


class VisitAttribute(models.Model):
    visit_attribute_id = models.AutoField(primary_key=True)
    visit = models.ForeignKey(Visit, models.DO_NOTHING)
    attribute_type = models.ForeignKey('VisitAttributeType', models.DO_NOTHING)
    value_reference = models.TextField()
    uuid = models.CharField(unique=True, max_length=38, default=uuid.uuid4)
    creator = models.ForeignKey('Users', models.DO_NOTHING, db_column='creator')
    date_created = models.DateTimeField()
    changed_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='changed_by', related_name='visitattribute_changed_by_set', blank=True, null=True)
    date_changed = models.DateTimeField(blank=True, null=True)
    voided = models.IntegerField()
    voided_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='voided_by', related_name='visitattribute_voided_by_set', blank=True, null=True)
    date_voided = models.DateTimeField(blank=True, null=True)
    void_reason = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'visit_attribute'


class VisitAttributeType(models.Model):
    visit_attribute_type_id = models.AutoField(primary_key=True)
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
    changed_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='changed_by', related_name='visitattributetype_changed_by_set', blank=True, null=True)
    date_changed = models.DateTimeField(blank=True, null=True)
    retired = models.IntegerField()
    retired_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='retired_by', related_name='visitattributetype_retired_by_set', blank=True, null=True)
    date_retired = models.DateTimeField(blank=True, null=True)
    retire_reason = models.CharField(max_length=255, blank=True, null=True)
    uuid = models.CharField(unique=True, max_length=38, default=uuid.uuid4)

    class Meta:
        managed = False
        db_table = 'visit_attribute_type'


class VisitType(models.Model):
    visit_type_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=1024, blank=True, null=True)
    creator = models.ForeignKey('Users', models.DO_NOTHING, db_column='creator')
    date_created = models.DateTimeField()
    changed_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='changed_by', related_name='visittype_changed_by_set', blank=True, null=True)
    date_changed = models.DateTimeField(blank=True, null=True)
    retired = models.IntegerField()
    retired_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='retired_by', related_name='visittype_retired_by_set', blank=True, null=True)
    date_retired = models.DateTimeField(blank=True, null=True)
    retire_reason = models.CharField(max_length=255, blank=True, null=True)
    uuid = models.CharField(unique=True, max_length=38, default=uuid.uuid4)

    class Meta:
        managed = False
        db_table = 'visit_type'
