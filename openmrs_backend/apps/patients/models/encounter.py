from django.db import models
import uuid

class Encounter(models.Model):
    encounter_id = models.AutoField(primary_key=True)
    encounter_type = models.ForeignKey('EncounterType', models.DO_NOTHING, db_column='encounter_type')
    patient = models.ForeignKey('Patient', models.DO_NOTHING)
    location = models.ForeignKey('Location', models.DO_NOTHING, blank=True, null=True)
    form = models.ForeignKey('Form', models.DO_NOTHING, blank=True, null=True)
    encounter_datetime = models.DateTimeField()
    creator = models.ForeignKey('Users', models.DO_NOTHING, db_column='creator')
    date_created = models.DateTimeField()
    voided = models.IntegerField()
    voided_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='voided_by', related_name='encounter_voided_by_set', blank=True, null=True)
    date_voided = models.DateTimeField(blank=True, null=True)
    void_reason = models.CharField(max_length=255, blank=True, null=True)
    changed_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='changed_by', related_name='encounter_changed_by_set', blank=True, null=True)
    date_changed = models.DateTimeField(blank=True, null=True)
    visit = models.ForeignKey('Visit', models.DO_NOTHING, blank=True, null=True)
    uuid = models.CharField(unique=True, max_length=38, default=uuid.uuid4)

    class Meta:
        # managed = False
        db_table = 'encounter'

class EncounterDiagnosis(models.Model):
    diagnosis_id = models.AutoField(primary_key=True)
    diagnosis_coded = models.ForeignKey('Concept', models.DO_NOTHING, db_column='diagnosis_coded', blank=True, null=True)
    diagnosis_non_coded = models.CharField(max_length=255, blank=True, null=True)
    diagnosis_coded_name = models.ForeignKey('ConceptName', models.DO_NOTHING, db_column='diagnosis_coded_name', blank=True, null=True)
    encounter = models.ForeignKey('Encounter', models.DO_NOTHING)
    patient = models.ForeignKey('Patient', models.DO_NOTHING)
    condition = models.ForeignKey('Conditions', models.DO_NOTHING, blank=True, null=True)
    certainty = models.CharField(max_length=255)
    dx_rank = models.IntegerField()
    uuid = models.CharField(unique=True, max_length=38, default=uuid.uuid4)
    creator = models.ForeignKey('Users', models.DO_NOTHING, db_column='creator')
    date_created = models.DateTimeField()
    changed_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='changed_by', related_name='encounterdiagnosis_changed_by_set', blank=True, null=True)
    date_changed = models.DateTimeField(blank=True, null=True)
    voided = models.IntegerField()
    voided_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='voided_by', related_name='encounterdiagnosis_voided_by_set', blank=True, null=True)
    date_voided = models.DateTimeField(blank=True, null=True)
    void_reason = models.CharField(max_length=255, blank=True, null=True)
    form_namespace_and_path = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        # managed = False
        db_table = 'encounter_diagnosis'

class EncounterProvider(models.Model):
    encounter_provider_id = models.AutoField(primary_key=True)
    encounter = models.ForeignKey('Encounter', models.DO_NOTHING)
    provider = models.ForeignKey('Provider', models.DO_NOTHING)
    encounter_role = models.ForeignKey('EncounterRole', models.DO_NOTHING)
    creator = models.ForeignKey('Users', models.DO_NOTHING, db_column='creator')
    date_created = models.DateTimeField()
    changed_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='changed_by', related_name='encounterprovider_changed_by_set', blank=True, null=True)
    date_changed = models.DateTimeField(blank=True, null=True)
    voided = models.IntegerField()
    date_voided = models.DateTimeField(blank=True, null=True)
    voided_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='voided_by', related_name='encounterprovider_voided_by_set', blank=True, null=True)
    void_reason = models.CharField(max_length=255, blank=True, null=True)
    uuid = models.CharField(unique=True, max_length=38, default=uuid.uuid4)

    class Meta:
        # managed = False
        db_table = 'encounter_provider'

class EncounterRole(models.Model):
    encounter_role_id = models.AutoField(primary_key=True)
    name = models.CharField(unique=True, max_length=255)
    description = models.CharField(max_length=1024, blank=True, null=True)
    creator = models.ForeignKey('Users', models.DO_NOTHING, db_column='creator')
    date_created = models.DateTimeField()
    changed_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='changed_by', related_name='encounterrole_changed_by_set', blank=True, null=True)
    date_changed = models.DateTimeField(blank=True, null=True)
    retired = models.IntegerField()
    retired_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='retired_by', related_name='encounterrole_retired_by_set', blank=True, null=True)
    date_retired = models.DateTimeField(blank=True, null=True)
    retire_reason = models.CharField(max_length=255, blank=True, null=True)
    uuid = models.CharField(unique=True, max_length=38, default=uuid.uuid4)

    class Meta:
        # managed = False
        db_table = 'encounter_role'

class EncounterType(models.Model):
    encounter_type_id = models.AutoField(primary_key=True)
    name = models.CharField(unique=True, max_length=50)
    description = models.TextField(blank=True, null=True)
    creator = models.ForeignKey('Users', models.DO_NOTHING, db_column='creator')
    date_created = models.DateTimeField()
    retired = models.IntegerField()
    retired_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='retired_by', related_name='encountertype_retired_by_set', blank=True, null=True)
    date_retired = models.DateTimeField(blank=True, null=True)
    retire_reason = models.CharField(max_length=255, blank=True, null=True)
    uuid = models.CharField(unique=True, max_length=38, default=uuid.uuid4)
    edit_privilege = models.ForeignKey('Privilege', models.DO_NOTHING, db_column='edit_privilege', blank=True, null=True)
    view_privilege = models.ForeignKey('Privilege', models.DO_NOTHING, db_column='view_privilege', related_name='encountertype_view_privilege_set', blank=True, null=True)
    changed_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='changed_by', related_name='encountertype_changed_by_set', blank=True, null=True)
    date_changed = models.DateTimeField(blank=True, null=True)

    class Meta:
        # managed = False
        db_table = 'encounter_type'

# Location-related models 
class Location(models.Model):
    location_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255, blank=True, null=True)
    address1 = models.CharField(max_length=255, blank=True, null=True)
    address2 = models.CharField(max_length=255, blank=True, null=True)
    city_village = models.CharField(max_length=255, blank=True, null=True)
    state_province = models.CharField(max_length=255, blank=True, null=True)
    postal_code = models.CharField(max_length=50, blank=True, null=True)
    country = models.CharField(max_length=50, blank=True, null=True)
    latitude = models.CharField(max_length=50, blank=True, null=True)
    longitude = models.CharField(max_length=50, blank=True, null=True)
    creator = models.ForeignKey('Users', models.DO_NOTHING, db_column='creator')
    date_created = models.DateTimeField()
    county_district = models.CharField(max_length=255, blank=True, null=True)
    address3 = models.CharField(max_length=255, blank=True, null=True)
    address4 = models.CharField(max_length=255, blank=True, null=True)
    address5 = models.CharField(max_length=255, blank=True, null=True)
    address6 = models.CharField(max_length=255, blank=True, null=True)
    retired = models.IntegerField()
    retired_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='retired_by', related_name='location_retired_by_set', blank=True, null=True)
    date_retired = models.DateTimeField(blank=True, null=True)
    retire_reason = models.CharField(max_length=255, blank=True, null=True)
    parent_location = models.ForeignKey('self', models.DO_NOTHING, db_column='parent_location', blank=True, null=True)
    uuid = models.CharField(unique=True, max_length=38, default=uuid.uuid4)
    changed_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='changed_by', related_name='location_changed_by_set', blank=True, null=True)
    date_changed = models.DateTimeField(blank=True, null=True)
    address7 = models.CharField(max_length=255, blank=True, null=True)
    address8 = models.CharField(max_length=255, blank=True, null=True)
    address9 = models.CharField(max_length=255, blank=True, null=True)
    address10 = models.CharField(max_length=255, blank=True, null=True)
    address11 = models.CharField(max_length=255, blank=True, null=True)
    address12 = models.CharField(max_length=255, blank=True, null=True)
    address13 = models.CharField(max_length=255, blank=True, null=True)
    address14 = models.CharField(max_length=255, blank=True, null=True)
    address15 = models.CharField(max_length=255, blank=True, null=True)
    location_type_concept = models.ForeignKey('Concept', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        # managed = False
        db_table = 'location'


class LocationAttribute(models.Model):
    location_attribute_id = models.AutoField(primary_key=True)
    location = models.ForeignKey(Location, models.DO_NOTHING)
    attribute_type = models.ForeignKey('LocationAttributeType', models.DO_NOTHING)
    value_reference = models.TextField()
    uuid = models.CharField(unique=True, max_length=38, default=uuid.uuid4)
    creator = models.ForeignKey('Users', models.DO_NOTHING, db_column='creator')
    date_created = models.DateTimeField()
    changed_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='changed_by', related_name='locationattribute_changed_by_set', blank=True, null=True)
    date_changed = models.DateTimeField(blank=True, null=True)
    voided = models.IntegerField()
    voided_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='voided_by', related_name='locationattribute_voided_by_set', blank=True, null=True)
    date_voided = models.DateTimeField(blank=True, null=True)
    void_reason = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        # managed = False
        db_table = 'location_attribute'


class LocationAttributeType(models.Model):
    location_attribute_type_id = models.AutoField(primary_key=True)
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
    changed_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='changed_by', related_name='locationattributetype_changed_by_set', blank=True, null=True)
    date_changed = models.DateTimeField(blank=True, null=True)
    retired = models.IntegerField()
    retired_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='retired_by', related_name='locationattributetype_retired_by_set', blank=True, null=True)
    date_retired = models.DateTimeField(blank=True, null=True)
    retire_reason = models.CharField(max_length=255, blank=True, null=True)
    uuid = models.CharField(unique=True, max_length=38, default=uuid.uuid4)

    class Meta:
        # managed = False
        db_table = 'location_attribute_type'


class LocationTag(models.Model):
    location_tag_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=255, blank=True, null=True)
    creator = models.ForeignKey('Users', models.DO_NOTHING, db_column='creator')
    date_created = models.DateTimeField()
    retired = models.IntegerField()
    retired_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='retired_by', related_name='locationtag_retired_by_set', blank=True, null=True)
    date_retired = models.DateTimeField(blank=True, null=True)
    retire_reason = models.CharField(max_length=255, blank=True, null=True)
    uuid = models.CharField(unique=True, max_length=38, default=uuid.uuid4)
    changed_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='changed_by', related_name='locationtag_changed_by_set', blank=True, null=True)
    date_changed = models.DateTimeField(blank=True, null=True)

    class Meta:
        # managed = False
        db_table = 'location_tag'


class LocationTagMap(models.Model):
    location = models.OneToOneField('Location', models.DO_NOTHING, primary_key=True)  # The composite primary key (location_id, location_tag_id) found, that is not supported. The first column is selected.
    location_tag = models.ForeignKey('LocationTag', models.DO_NOTHING)

    class Meta:
        # managed = False
        db_table = 'location_tag_map'
        unique_together = (('location', 'location_tag'),)
