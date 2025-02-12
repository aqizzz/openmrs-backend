from django.db import models
import uuid

class Person(models.Model):
    person_id = models.AutoField(primary_key=True)
    gender = models.CharField(max_length=50, blank=True, null=True)
    birthdate = models.DateField(blank=True, null=True)
    birthdate_estimated = models.IntegerField(default=0)
    dead = models.IntegerField(default=0)
    death_date = models.DateTimeField(blank=True, null=True)
    cause_of_death = models.ForeignKey('Concept', models.DO_NOTHING, db_column='cause_of_death', blank=True, null=True)
    creator = models.ForeignKey('Users', models.DO_NOTHING, db_column='creator', blank=True, null=True, related_name='person_creator')
    date_created = models.DateTimeField(auto_now_add=True)
    changed_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='changed_by', related_name='person_changed_by_set', blank=True, null=True)
    date_changed = models.DateTimeField(blank=True, null=True)
    voided = models.IntegerField(default=0)
    voided_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='voided_by', related_name='person_voided_by_set', blank=True, null=True)
    date_voided = models.DateTimeField(blank=True, null=True)
    void_reason = models.CharField(max_length=255, blank=True, null=True)
    uuid = models.CharField(unique=True, max_length=38, default=uuid.uuid4)
    deathdate_estimated = models.IntegerField(default=0)
    birthtime = models.TimeField(blank=True, null=True)
    cause_of_death_non_coded = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        # managed = False
        db_table = 'person'

class PersonAddress(models.Model):
    person_address_id = models.AutoField(primary_key=True)
    person = models.ForeignKey('Person', models.DO_NOTHING, blank=True, null=True)
    preferred = models.IntegerField()
    address1 = models.CharField(max_length=255, blank=True, null=True)
    address2 = models.CharField(max_length=255, blank=True, null=True)
    city_village = models.CharField(max_length=255, blank=True, null=True)
    state_province = models.CharField(max_length=255, blank=True, null=True)
    postal_code = models.CharField(max_length=50, blank=True, null=True)
    country = models.CharField(max_length=50, blank=True, null=True)
    latitude = models.CharField(max_length=50, blank=True, null=True)
    longitude = models.CharField(max_length=50, blank=True, null=True)
    start_date = models.DateTimeField(blank=True, null=True)
    end_date = models.DateTimeField(blank=True, null=True)
    creator = models.ForeignKey('Users', models.DO_NOTHING, db_column='creator')
    date_created = models.DateTimeField()
    voided = models.IntegerField()
    voided_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='voided_by', related_name='personaddress_voided_by_set', blank=True, null=True)
    date_voided = models.DateTimeField(blank=True, null=True)
    void_reason = models.CharField(max_length=255, blank=True, null=True)
    county_district = models.CharField(max_length=255, blank=True, null=True)
    address3 = models.CharField(max_length=255, blank=True, null=True)
    address4 = models.CharField(max_length=255, blank=True, null=True)
    address5 = models.CharField(max_length=255, blank=True, null=True)
    address6 = models.CharField(max_length=255, blank=True, null=True)
    date_changed = models.DateTimeField(blank=True, null=True)
    changed_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='changed_by', related_name='personaddress_changed_by_set', blank=True, null=True)
    uuid = models.CharField(unique=True, max_length=38, default=uuid.uuid4)
    address7 = models.CharField(max_length=255, blank=True, null=True)
    address8 = models.CharField(max_length=255, blank=True, null=True)
    address9 = models.CharField(max_length=255, blank=True, null=True)
    address10 = models.CharField(max_length=255, blank=True, null=True)
    address11 = models.CharField(max_length=255, blank=True, null=True)
    address12 = models.CharField(max_length=255, blank=True, null=True)
    address13 = models.CharField(max_length=255, blank=True, null=True)
    address14 = models.CharField(max_length=255, blank=True, null=True)
    address15 = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        # managed = False
        db_table = 'person_address'

class PersonAttribute(models.Model):
    person_attribute_id = models.AutoField(primary_key=True)
    person = models.ForeignKey('Person', models.DO_NOTHING)
    value = models.CharField(max_length=50)
    person_attribute_type = models.ForeignKey('PersonAttributeType', models.DO_NOTHING)
    creator = models.ForeignKey('Users', models.DO_NOTHING, db_column='creator')
    date_created = models.DateTimeField()
    changed_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='changed_by', related_name='personattribute_changed_by_set', blank=True, null=True)
    date_changed = models.DateTimeField(blank=True, null=True)
    voided = models.IntegerField()
    voided_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='voided_by', related_name='personattribute_voided_by_set', blank=True, null=True)
    date_voided = models.DateTimeField(blank=True, null=True)
    void_reason = models.CharField(max_length=255, blank=True, null=True)
    uuid = models.CharField(unique=True, max_length=38, default=uuid.uuid4)

    class Meta:
        # managed = False
        db_table = 'person_attribute'

class PersonAttributeType(models.Model):
    person_attribute_type_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True, null=True)
    format = models.CharField(max_length=50, blank=True, null=True)
    foreign_key = models.IntegerField(blank=True, null=True)
    searchable = models.IntegerField()
    creator = models.ForeignKey('Users', models.DO_NOTHING, db_column='creator')
    date_created = models.DateTimeField()
    changed_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='changed_by', related_name='personattributetype_changed_by_set', blank=True, null=True)
    date_changed = models.DateTimeField(blank=True, null=True)
    retired = models.IntegerField()
    retired_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='retired_by', related_name='personattributetype_retired_by_set', blank=True, null=True)
    date_retired = models.DateTimeField(blank=True, null=True)
    retire_reason = models.CharField(max_length=255, blank=True, null=True)
    edit_privilege = models.ForeignKey('Privilege', models.DO_NOTHING, db_column='edit_privilege', blank=True, null=True)
    sort_weight = models.FloatField(blank=True, null=True)
    uuid = models.CharField(unique=True, max_length=38, default=uuid.uuid4)

    class Meta:
        # managed = False
        db_table = 'person_attribute_type'

class PersonMergeLog(models.Model):
    person_merge_log_id = models.AutoField(primary_key=True)
    winner_person = models.ForeignKey('Person', models.DO_NOTHING)
    loser_person = models.ForeignKey('Person', models.DO_NOTHING, related_name='personmergelog_loser_person_set')
    creator = models.ForeignKey('Users', models.DO_NOTHING, db_column='creator')
    date_created = models.DateTimeField()
    merged_data = models.TextField()
    uuid = models.CharField(unique=True, max_length=38, default=uuid.uuid4)
    changed_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='changed_by', related_name='personmergelog_changed_by_set', blank=True, null=True)
    date_changed = models.DateTimeField(blank=True, null=True)
    voided = models.IntegerField()
    voided_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='voided_by', related_name='personmergelog_voided_by_set', blank=True, null=True)
    date_voided = models.DateTimeField(blank=True, null=True)
    void_reason = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        # managed = False
        db_table = 'person_merge_log'

class PersonName(models.Model):
    person_name_id = models.AutoField(primary_key=True)
    preferred = models.IntegerField()
    person = models.ForeignKey('Person', models.DO_NOTHING)
    prefix = models.CharField(max_length=50, blank=True, null=True)
    given_name = models.CharField(max_length=50, blank=True, null=True)
    middle_name = models.CharField(max_length=50, blank=True, null=True)
    family_name_prefix = models.CharField(max_length=50, blank=True, null=True)
    family_name = models.CharField(max_length=50, blank=True, null=True)
    family_name2 = models.CharField(max_length=50, blank=True, null=True)
    family_name_suffix = models.CharField(max_length=50, blank=True, null=True)
    degree = models.CharField(max_length=50, blank=True, null=True)
    creator = models.ForeignKey('Users', models.DO_NOTHING, db_column='creator')
    date_created = models.DateTimeField()
    voided = models.IntegerField()
    voided_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='voided_by', related_name='personname_voided_by_set', blank=True, null=True)
    date_voided = models.DateTimeField(blank=True, null=True)
    void_reason = models.CharField(max_length=255, blank=True, null=True)
    changed_by = models.IntegerField(blank=True, null=True)
    date_changed = models.DateTimeField(blank=True, null=True)
    uuid = models.CharField(unique=True, max_length=38, default=uuid.uuid4)

    class Meta:
        # managed = False
        db_table = 'person_name'


class Relationship(models.Model):
    relationship_id = models.AutoField(primary_key=True)
    person_a = models.ForeignKey('Person', models.DO_NOTHING, db_column='person_a')
    relationship_type = models.ForeignKey('RelationshipType', models.DO_NOTHING, db_column='relationship', to_field='relationship_type_id')
    person_b = models.ForeignKey('Person', models.DO_NOTHING, db_column='person_b', related_name='relationship_person_b_set')
    start_date = models.DateTimeField(blank=True, null=True)
    end_date = models.DateTimeField(blank=True, null=True)
    creator = models.ForeignKey('Users', models.DO_NOTHING, db_column='creator')
    date_created = models.DateTimeField()
    date_changed = models.DateTimeField(blank=True, null=True)
    changed_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='changed_by', related_name='relationship_changed_by_set', blank=True, null=True)
    voided = models.IntegerField()
    voided_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='voided_by', related_name='relationship_voided_by_set', blank=True, null=True)
    date_voided = models.DateTimeField(blank=True, null=True)
    void_reason = models.CharField(max_length=255, blank=True, null=True)
    uuid = models.CharField(unique=True, max_length=38, default=uuid.uuid4)

    class Meta:
        # managed = False
        db_table = 'relationship'


class RelationshipType(models.Model):
    relationship_type_id = models.AutoField(primary_key=True)
    a_is_to_b = models.CharField(max_length=50)
    b_is_to_a = models.CharField(max_length=50)
    preferred = models.IntegerField()
    weight = models.IntegerField()
    description = models.CharField(max_length=255, blank=True, null=True)
    creator = models.ForeignKey('Users', models.DO_NOTHING, db_column='creator')
    date_created = models.DateTimeField()
    retired = models.IntegerField()
    retired_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='retired_by', related_name='relationshiptype_retired_by_set', blank=True, null=True)
    date_retired = models.DateTimeField(blank=True, null=True)
    retire_reason = models.CharField(max_length=255, blank=True, null=True)
    uuid = models.CharField(unique=True, max_length=38, default=uuid.uuid4)
    date_changed = models.DateTimeField(blank=True, null=True)
    changed_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='changed_by', related_name='relationshiptype_changed_by_set', blank=True, null=True)

    class Meta:
        # managed = False
        db_table = 'relationship_type'

