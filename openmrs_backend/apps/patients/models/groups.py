from django.db import models
import uuid

class Cohort(models.Model):
    cohort_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=1000, blank=True, null=True)
    creator = models.ForeignKey('Users', models.DO_NOTHING, db_column='creator')
    date_created = models.DateTimeField()
    voided = models.IntegerField()
    voided_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='voided_by', related_name='cohort_voided_by_set', blank=True, null=True)
    date_voided = models.DateTimeField(blank=True, null=True)
    void_reason = models.CharField(max_length=255, blank=True, null=True)
    changed_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='changed_by', related_name='cohort_changed_by_set', blank=True, null=True)
    date_changed = models.DateTimeField(blank=True, null=True)
    uuid = models.CharField(unique=True, max_length=38, default=uuid.uuid4)
    location = models.ForeignKey('Location', models.DO_NOTHING, blank=True, null=True)
    startdate = models.DateTimeField(db_column='startDate', blank=True, null=True)  # Field name made lowercase.
    enddate = models.DateTimeField(db_column='endDate', blank=True, null=True)  # Field name made lowercase.
    is_group_cohort = models.IntegerField(blank=True, null=True)
    cohort_type = models.ForeignKey('CohortType', models.DO_NOTHING, blank=True, null=True)
    definition_handler = models.CharField(max_length=255, blank=True, null=True)
    definition_handler_config = models.TextField(blank=True, null=True)

    class Meta:
        # managed = False
        db_table = 'cohort'


class CohortAttribute(models.Model):
    cohort_attribute_id = models.AutoField(primary_key=True)
    cohort = models.ForeignKey(Cohort, models.DO_NOTHING)
    value_reference = models.CharField(max_length=255)
    attribute_type = models.ForeignKey('CohortAttributeType', models.DO_NOTHING)
    date_created = models.DateTimeField()
    creator = models.ForeignKey('Users', models.DO_NOTHING, db_column='creator')
    changed_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='changed_by', related_name='cohortattribute_changed_by_set', blank=True, null=True)
    date_changed = models.DateTimeField(blank=True, null=True)
    voided = models.IntegerField()
    voided_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='voided_by', related_name='cohortattribute_voided_by_set', blank=True, null=True)
    date_voided = models.DateTimeField(blank=True, null=True)
    void_reason = models.CharField(max_length=255, blank=True, null=True)
    uuid = models.CharField(max_length=255)

    class Meta:
        # managed = False
        db_table = 'cohort_attribute'


class CohortAttributeType(models.Model):
    cohort_attribute_type_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255, blank=True, null=True)
    datatype = models.CharField(max_length=255, blank=True, null=True)
    datatype_config = models.TextField(blank=True, null=True)
    preferred_handler = models.CharField(max_length=255, blank=True, null=True)
    handler_config = models.TextField(blank=True, null=True)
    max_occurs = models.IntegerField(blank=True, null=True)
    min_occurs = models.IntegerField()
    date_created = models.DateTimeField()
    creator = models.ForeignKey('Users', models.DO_NOTHING, db_column='creator')
    changed_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='changed_by', related_name='cohortattributetype_changed_by_set', blank=True, null=True)
    date_changed = models.DateTimeField(blank=True, null=True)
    retired = models.IntegerField()
    retired_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='retired_by', related_name='cohortattributetype_retired_by_set', blank=True, null=True)
    date_retired = models.DateTimeField(blank=True, null=True)
    retire_reason = models.CharField(max_length=255, blank=True, null=True)
    uuid = models.CharField(max_length=255)

    class Meta:
        # managed = False
        db_table = 'cohort_attribute_type'


class CohortMember(models.Model):
    cohort = models.ForeignKey(Cohort, models.DO_NOTHING)
    patient = models.ForeignKey('Patient', models.DO_NOTHING)
    cohort_member_id = models.AutoField(primary_key=True)
    start_date = models.DateTimeField(blank=True, null=True)
    end_date = models.DateTimeField(blank=True, null=True)
    creator = models.ForeignKey('Users', models.DO_NOTHING, db_column='creator')
    date_created = models.DateTimeField()
    voided = models.IntegerField()
    voided_by = models.IntegerField(blank=True, null=True)
    date_voided = models.DateTimeField(blank=True, null=True)
    void_reason = models.CharField(max_length=255, blank=True, null=True)
    uuid = models.CharField(unique=True, max_length=38, default=uuid.uuid4)
    date_changed = models.DateField(blank=True, null=True)
    changed_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='changed_by', related_name='cohortmember_changed_by_set', blank=True, null=True)

    class Meta:
        # managed = False
        db_table = 'cohort_member'


class CohortMemberAttribute(models.Model):
    cohort_member_attribute_id = models.AutoField(primary_key=True)
    cohort_member = models.ForeignKey(CohortMember, models.DO_NOTHING)
    value_reference = models.TextField()
    cohort_member_attribute_type = models.ForeignKey('CohortMemberAttributeType', models.DO_NOTHING)
    date_created = models.DateTimeField()
    creator = models.ForeignKey('Users', models.DO_NOTHING, db_column='creator')
    changed_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='changed_by', related_name='cohortmemberattribute_changed_by_set', blank=True, null=True)
    date_changed = models.DateTimeField(blank=True, null=True)
    voided = models.IntegerField()
    voided_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='voided_by', related_name='cohortmemberattribute_voided_by_set', blank=True, null=True)
    date_voided = models.DateTimeField(blank=True, null=True)
    void_reason = models.CharField(max_length=255, blank=True, null=True)
    uuid = models.CharField(max_length=38, default=uuid.uuid4)

    class Meta:
        # managed = False
        db_table = 'cohort_member_attribute'


class CohortMemberAttributeType(models.Model):
    cohort_member_attribute_type_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255, blank=True, null=True)
    datatype = models.CharField(max_length=255, blank=True, null=True)
    datatype_config = models.TextField(blank=True, null=True)
    preferred_handler = models.CharField(max_length=255, blank=True, null=True)
    handler_config = models.TextField(blank=True, null=True)
    max_occurs = models.IntegerField(blank=True, null=True)
    min_occurs = models.IntegerField()
    date_created = models.DateTimeField()
    creator = models.ForeignKey('Users', models.DO_NOTHING, db_column='creator')
    changed_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='changed_by', related_name='cohortmemberattributetype_changed_by_set', blank=True, null=True)
    date_changed = models.DateTimeField(blank=True, null=True)
    retired = models.IntegerField()
    retired_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='retired_by', related_name='cohortmemberattributetype_retired_by_set', blank=True, null=True)
    date_retired = models.DateTimeField(blank=True, null=True)
    retire_reason = models.CharField(max_length=255, blank=True, null=True)
    uuid = models.CharField(max_length=38, default=uuid.uuid4)

    class Meta:
        # managed = False
        db_table = 'cohort_member_attribute_type'


class CohortType(models.Model):
    cohort_type_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255, blank=True, null=True)
    date_created = models.DateTimeField()
    creator = models.ForeignKey('Users', models.DO_NOTHING, db_column='creator')
    changed_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='changed_by', related_name='cohorttype_changed_by_set', blank=True, null=True)
    date_changed = models.DateTimeField(blank=True, null=True)
    voided = models.IntegerField()
    voided_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='voided_by', related_name='cohorttype_voided_by_set', blank=True, null=True)
    date_voided = models.DateTimeField(blank=True, null=True)
    void_reason = models.CharField(max_length=255, blank=True, null=True)
    uuid = models.CharField(max_length=255)

    class Meta:
        # managed = False
        db_table = 'cohort_type'


class Program(models.Model):
    program_id = models.AutoField(primary_key=True)
    concept = models.ForeignKey('Concept', models.DO_NOTHING)
    outcomes_concept = models.ForeignKey('Concept', models.DO_NOTHING, related_name='program_outcomes_concept_set', blank=True, null=True)
    creator = models.ForeignKey('Users', models.DO_NOTHING, db_column='creator')
    date_created = models.DateTimeField()
    changed_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='changed_by', related_name='program_changed_by_set', blank=True, null=True)
    date_changed = models.DateTimeField(blank=True, null=True)
    retired = models.IntegerField()
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True, null=True)
    uuid = models.CharField(unique=True, max_length=38, default=uuid.uuid4)

    class Meta:
        # managed = False
        db_table = 'program'


class ProgramAttributeType(models.Model):
    program_attribute_type_id = models.AutoField(primary_key=True)
    name = models.CharField(unique=True, max_length=255)
    description = models.CharField(max_length=1024, blank=True, null=True)
    datatype = models.CharField(max_length=255, blank=True, null=True)
    datatype_config = models.TextField(blank=True, null=True)
    preferred_handler = models.CharField(max_length=255, blank=True, null=True)
    handler_config = models.TextField(blank=True, null=True)
    min_occurs = models.IntegerField()
    max_occurs = models.IntegerField(blank=True, null=True)
    creator = models.ForeignKey('Users', models.DO_NOTHING, db_column='creator')
    date_created = models.DateTimeField()
    changed_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='changed_by', related_name='programattributetype_changed_by_set', blank=True, null=True)
    date_changed = models.DateTimeField(blank=True, null=True)
    retired = models.IntegerField()
    retired_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='retired_by', related_name='programattributetype_retired_by_set', blank=True, null=True)
    date_retired = models.DateTimeField(blank=True, null=True)
    retire_reason = models.CharField(max_length=255, blank=True, null=True)
    uuid = models.CharField(unique=True, max_length=38, default=uuid.uuid4)

    class Meta:
        # managed = False
        db_table = 'program_attribute_type'


class ProgramWorkflow(models.Model):
    program_workflow_id = models.AutoField(primary_key=True)
    program = models.ForeignKey('Program', models.DO_NOTHING)
    concept = models.ForeignKey('Concept', models.DO_NOTHING)
    creator = models.ForeignKey('Users', models.DO_NOTHING, db_column='creator')
    date_created = models.DateTimeField()
    retired = models.IntegerField()
    changed_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='changed_by', related_name='programworkflow_changed_by_set', blank=True, null=True)
    date_changed = models.DateTimeField(blank=True, null=True)
    uuid = models.CharField(unique=True, max_length=38, default=uuid.uuid4)

    class Meta:
        # managed = False
        db_table = 'program_workflow'

class ProgramWorkflowState(models.Model):
    program_workflow_state_id = models.AutoField(primary_key=True)
    program_workflow = models.ForeignKey('ProgramWorkflow', models.DO_NOTHING)
    concept = models.ForeignKey('Concept', models.DO_NOTHING)
    initial = models.IntegerField()
    terminal = models.IntegerField()
    creator = models.ForeignKey('Users', models.DO_NOTHING, db_column='creator')
    date_created = models.DateTimeField()
    retired = models.IntegerField()
    changed_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='changed_by', related_name='programworkflowstate_changed_by_set', blank=True, null=True)
    date_changed = models.DateTimeField(blank=True, null=True)
    uuid = models.CharField(unique=True, max_length=38, default=uuid.uuid4)

    class Meta:
        # managed = False
        db_table = 'program_workflow_state'

class PatientState(models.Model):
    patient_state_id = models.AutoField(primary_key=True)
    patient_program = models.ForeignKey('PatientProgram', models.DO_NOTHING)
    state = models.ForeignKey('ProgramWorkflowState', models.DO_NOTHING, db_column='state')
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    creator = models.ForeignKey('Users', models.DO_NOTHING, db_column='creator')
    date_created = models.DateTimeField()
    changed_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='changed_by', related_name='patientstate_changed_by_set', blank=True, null=True)
    date_changed = models.DateTimeField(blank=True, null=True)
    voided = models.IntegerField()
    voided_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='voided_by', related_name='patientstate_voided_by_set', blank=True, null=True)
    date_voided = models.DateTimeField(blank=True, null=True)
    void_reason = models.CharField(max_length=255, blank=True, null=True)
    uuid = models.CharField(unique=True, max_length=38, default=uuid.uuid4)
    form_namespace_and_path = models.CharField(max_length=255, blank=True, null=True)
    encounter = models.ForeignKey('Encounter', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        # managed = False
        db_table = 'patient_state'


class PatientProgram(models.Model):
    patient_program_id = models.AutoField(primary_key=True)
    patient = models.ForeignKey('Patient', models.DO_NOTHING)
    program = models.ForeignKey('Program', models.DO_NOTHING)
    date_enrolled = models.DateTimeField(blank=True, null=True)
    date_completed = models.DateTimeField(blank=True, null=True)
    location = models.ForeignKey('Location', models.DO_NOTHING, blank=True, null=True)
    outcome_concept = models.ForeignKey('Concept', models.DO_NOTHING, blank=True, null=True)
    creator = models.ForeignKey('Users', models.DO_NOTHING, db_column='creator')
    date_created = models.DateTimeField()
    changed_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='changed_by', related_name='patientprogram_changed_by_set', blank=True, null=True)
    date_changed = models.DateTimeField(blank=True, null=True)
    voided = models.IntegerField()
    voided_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='voided_by', related_name='patientprogram_voided_by_set', blank=True, null=True)
    date_voided = models.DateTimeField(blank=True, null=True)
    void_reason = models.CharField(max_length=255, blank=True, null=True)
    uuid = models.CharField(unique=True, max_length=38, default=uuid.uuid4)

    class Meta:
        # managed = False
        db_table = 'patient_program'

class PatientProgramAttribute(models.Model):
    patient_program_attribute_id = models.AutoField(primary_key=True)
    patient_program = models.ForeignKey('PatientProgram', models.DO_NOTHING)
    attribute_type = models.ForeignKey('ProgramAttributeType', models.DO_NOTHING)
    value_reference = models.TextField()
    uuid = models.CharField(unique=True, max_length=38, default=uuid.uuid4)
    creator = models.ForeignKey('Users', models.DO_NOTHING, db_column='creator')
    date_created = models.DateTimeField()
    changed_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='changed_by', related_name='patientprogramattribute_changed_by_set', blank=True, null=True)
    date_changed = models.DateTimeField(blank=True, null=True)
    voided = models.IntegerField()
    voided_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='voided_by', related_name='patientprogramattribute_voided_by_set', blank=True, null=True)
    date_voided = models.DateTimeField(blank=True, null=True)
    void_reason = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        # managed = False
        db_table = 'patient_program_attribute'

