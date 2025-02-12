from django.db import models
import uuid

# Create your models here.

# Meta and setting related models
class MetadatamappingMetadataSet(models.Model):
    metadata_set_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    description = models.CharField(max_length=1024, blank=True, null=True)
    creator = models.ForeignKey('Users', models.DO_NOTHING, db_column='creator')
    date_created = models.DateTimeField()
    changed_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='changed_by', related_name='metadatamappingmetadataset_changed_by_set', blank=True, null=True)
    date_changed = models.DateTimeField(blank=True, null=True)
    retired = models.IntegerField()
    date_retired = models.DateTimeField(blank=True, null=True)
    retired_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='retired_by', related_name='metadatamappingmetadataset_retired_by_set', blank=True, null=True)
    retire_reason = models.CharField(max_length=255, blank=True, null=True)
    uuid = models.CharField(unique=True, max_length=38, default=uuid.uuid4)

    class Meta:
        # managed = False
        db_table = 'metadatamapping_metadata_set'


class MetadatamappingMetadataSetMember(models.Model):
    metadata_set_member_id = models.AutoField(primary_key=True)
    metadata_set = models.ForeignKey(MetadatamappingMetadataSet, models.DO_NOTHING)
    metadata_class = models.CharField(max_length=1024)
    metadata_uuid = models.CharField(max_length=38, default=uuid.uuid4)
    sort_weight = models.FloatField(blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    description = models.CharField(max_length=1024, blank=True, null=True)
    creator = models.ForeignKey('Users', models.DO_NOTHING, db_column='creator')
    date_created = models.DateTimeField()
    changed_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='changed_by', related_name='metadatamappingmetadatasetmember_changed_by_set', blank=True, null=True)
    date_changed = models.DateTimeField(blank=True, null=True)
    retired = models.IntegerField()
    date_retired = models.DateTimeField(blank=True, null=True)
    retired_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='retired_by', related_name='metadatamappingmetadatasetmember_retired_by_set', blank=True, null=True)
    retire_reason = models.CharField(max_length=255, blank=True, null=True)
    uuid = models.CharField(unique=True, max_length=38, default=uuid.uuid4)

    class Meta:
        # managed = False
        db_table = 'metadatamapping_metadata_set_member'
        unique_together = (('metadata_set', 'metadata_uuid'),)


class MetadatamappingMetadataSource(models.Model):
    metadata_source_id = models.AutoField(primary_key=True)
    name = models.CharField(unique=True, max_length=255)
    description = models.CharField(max_length=1024, blank=True, null=True)
    creator = models.ForeignKey('Users', models.DO_NOTHING, db_column='creator')
    changed_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='changed_by', related_name='metadatamappingmetadatasource_changed_by_set', blank=True, null=True)
    date_created = models.DateTimeField()
    date_changed = models.DateTimeField(blank=True, null=True)
    retired = models.IntegerField()
    date_retired = models.DateTimeField(blank=True, null=True)
    retired_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='retired_by', related_name='metadatamappingmetadatasource_retired_by_set', blank=True, null=True)
    retire_reason = models.CharField(max_length=255, blank=True, null=True)
    uuid = models.CharField(unique=True, max_length=38, default=uuid.uuid4)

    class Meta:
        # managed = False
        db_table = 'metadatamapping_metadata_source'


class MetadatamappingMetadataTermMapping(models.Model):
    metadata_term_mapping_id = models.AutoField(primary_key=True)
    metadata_source = models.ForeignKey(MetadatamappingMetadataSource, models.DO_NOTHING)
    code = models.CharField(max_length=255)
    metadata_class = models.CharField(max_length=1024, blank=True, null=True)
    metadata_uuid = models.CharField(max_length=38, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    description = models.CharField(max_length=1024, blank=True, null=True)
    creator = models.ForeignKey('Users', models.DO_NOTHING, db_column='creator')
    date_created = models.DateTimeField()
    changed_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='changed_by', related_name='metadatamappingmetadatatermmapping_changed_by_set', blank=True, null=True)
    date_changed = models.DateTimeField(blank=True, null=True)
    retired = models.IntegerField()
    date_retired = models.DateTimeField(blank=True, null=True)
    retired_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='retired_by', related_name='metadatamappingmetadatatermmapping_retired_by_set', blank=True, null=True)
    retire_reason = models.CharField(max_length=255, blank=True, null=True)
    uuid = models.CharField(unique=True, max_length=38, default=uuid.uuid4)

    class Meta:
        # managed = False
        db_table = 'metadatamapping_metadata_term_mapping'
        unique_together = (('metadata_source', 'code'),)


class MetadatasharingExportedPackage(models.Model):
    exported_package_id = models.AutoField(primary_key=True)
    uuid = models.CharField(unique=True, max_length=38, default=uuid.uuid4)
    group_uuid = models.CharField(max_length=38)
    version = models.IntegerField()
    published = models.IntegerField()
    date_created = models.DateTimeField()
    name = models.CharField(max_length=64)
    description = models.CharField(max_length=256)
    content = models.TextField(blank=True, null=True)

    class Meta:
        # managed = False
        db_table = 'metadatasharing_exported_package'


class MetadatasharingImportedItem(models.Model):
    imported_item_id = models.AutoField(primary_key=True)
    uuid = models.CharField(max_length=38, default=uuid.uuid4)
    classname = models.CharField(max_length=256)
    existing_uuid = models.CharField(max_length=38, blank=True, null=True)
    date_imported = models.DateTimeField(blank=True, null=True)
    date_changed = models.DateTimeField(blank=True, null=True)
    import_type = models.IntegerField(blank=True, null=True)
    assessed = models.IntegerField()

    class Meta:
        # managed = False
        db_table = 'metadatasharing_imported_item'


class MetadatasharingImportedPackage(models.Model):
    imported_package_id = models.AutoField(primary_key=True)
    uuid = models.CharField(unique=True, max_length=38, default=uuid.uuid4)
    group_uuid = models.CharField(max_length=38)
    subscription_url = models.CharField(max_length=512, blank=True, null=True)
    subscription_status = models.IntegerField(blank=True, null=True)
    date_created = models.DateTimeField()
    date_imported = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=64, blank=True, null=True)
    description = models.CharField(max_length=256)
    import_config = models.CharField(max_length=1024, blank=True, null=True)
    remote_version = models.IntegerField(blank=True, null=True)
    version = models.IntegerField(blank=True, null=True)

    class Meta:
        # managed = False
        db_table = 'metadatasharing_imported_package'

class CareSetting(models.Model):
    care_setting_id = models.AutoField(primary_key=True)
    name = models.CharField(unique=True, max_length=255)
    description = models.CharField(max_length=255, blank=True, null=True)
    care_setting_type = models.CharField(max_length=50)
    creator = models.ForeignKey('Users', models.DO_NOTHING, db_column='creator')
    date_created = models.DateTimeField()
    retired = models.IntegerField()
    retired_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='retired_by', related_name='caresetting_retired_by_set', blank=True, null=True)
    date_retired = models.DateTimeField(blank=True, null=True)
    retire_reason = models.CharField(max_length=255, blank=True, null=True)
    changed_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='changed_by', related_name='caresetting_changed_by_set', blank=True, null=True)
    date_changed = models.DateTimeField(blank=True, null=True)
    uuid = models.CharField(unique=True, max_length=38, default=uuid.uuid4)

    class Meta:
        # managed = False
        db_table = 'care_setting'


# Diagnosis and drug related models
class DiagnosisAttribute(models.Model):
    diagnosis_attribute_id = models.AutoField(primary_key=True)
    diagnosis = models.ForeignKey('EncounterDiagnosis', models.DO_NOTHING)
    attribute_type = models.ForeignKey('DiagnosisAttributeType', models.DO_NOTHING)
    value_reference = models.TextField()
    uuid = models.CharField(unique=True, max_length=38, default=uuid.uuid4)
    creator = models.ForeignKey('Users', models.DO_NOTHING, db_column='creator')
    date_created = models.DateTimeField()
    changed_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='changed_by', related_name='diagnosisattribute_changed_by_set', blank=True, null=True)
    date_changed = models.DateTimeField(blank=True, null=True)
    voided = models.IntegerField()
    voided_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='voided_by', related_name='diagnosisattribute_voided_by_set', blank=True, null=True)
    date_voided = models.DateTimeField(blank=True, null=True)
    void_reason = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        # managed = False
        db_table = 'diagnosis_attribute'


class DiagnosisAttributeType(models.Model):
    diagnosis_attribute_type_id = models.AutoField(primary_key=True)
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
    changed_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='changed_by', related_name='diagnosisattributetype_changed_by_set', blank=True, null=True)
    date_changed = models.DateTimeField(blank=True, null=True)
    retired = models.IntegerField()
    retired_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='retired_by', related_name='diagnosisattributetype_retired_by_set', blank=True, null=True)
    date_retired = models.DateTimeField(blank=True, null=True)
    retire_reason = models.CharField(max_length=255, blank=True, null=True)
    uuid = models.CharField(unique=True, max_length=38, default=uuid.uuid4)

    class Meta:
        # managed = False
        db_table = 'diagnosis_attribute_type'


class DrugReferenceMap(models.Model):
    drug_reference_map_id = models.AutoField(primary_key=True)
    drug = models.ForeignKey('Drug', models.DO_NOTHING)
    term = models.ForeignKey('ConceptReferenceTerm', models.DO_NOTHING)
    concept_map_type = models.ForeignKey('ConceptMapType', models.DO_NOTHING, db_column='concept_map_type')
    creator = models.ForeignKey('Users', models.DO_NOTHING, db_column='creator')
    date_created = models.DateTimeField()
    retired = models.IntegerField()
    retired_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='retired_by', related_name='drugreferencemap_retired_by_set', blank=True, null=True)
    date_retired = models.DateTimeField(blank=True, null=True)
    retire_reason = models.CharField(max_length=255, blank=True, null=True)
    changed_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='changed_by', related_name='drugreferencemap_changed_by_set', blank=True, null=True)
    date_changed = models.DateTimeField(blank=True, null=True)
    uuid = models.CharField(unique=True, max_length=38, default=uuid.uuid4)

    class Meta:
        # managed = False
        db_table = 'drug_reference_map'




class RadiologyOrder(models.Model):
    order = models.OneToOneField('Orders', models.DO_NOTHING, primary_key=True)
    body_site = models.ForeignKey('Concept', models.DO_NOTHING, db_column='body_site', blank=True, null=True)
    specimen_source = models.ForeignKey('Concept', models.DO_NOTHING, db_column='specimen_source', related_name='radiologyorder_specimen_source_set', blank=True, null=True)
    specimen_type = models.ForeignKey('Concept', models.DO_NOTHING, db_column='specimen_type', related_name='radiologyorder_specimen_type_set', blank=True, null=True)
    laterality = models.CharField(max_length=20, blank=True, null=True)
    clinical_history = models.TextField(blank=True, null=True)
    frequency = models.ForeignKey('OrderFrequency', models.DO_NOTHING, db_column='frequency', blank=True, null=True)
    number_of_repeats = models.IntegerField(blank=True, null=True)
    location = models.ForeignKey('Concept', models.DO_NOTHING, db_column='location', related_name='radiologyorder_location_set', blank=True, null=True)
    radiology_status = models.CharField(max_length=20, blank=True, null=True)
    related_radiology_order = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        # managed = False
        db_table = 'radiology_order'


class RadiologyOrderQueue(models.Model):
    radiology_order = models.ForeignKey('RadiologyOrder', models.DO_NOTHING)
    status = models.CharField(max_length=20)
    urgency = models.CharField(max_length=10)
    creator = models.IntegerField()
    date_created = models.DateTimeField()
    changed_by = models.IntegerField(blank=True, null=True)
    date_changed = models.DateTimeField(blank=True, null=True)
    voided = models.IntegerField()
    voided_by = models.IntegerField(blank=True, null=True)
    date_voided = models.DateTimeField(blank=True, null=True)
    void_reason = models.CharField(max_length=255, blank=True, null=True)
    uuid = models.CharField(unique=True, max_length=38, default=uuid.uuid4)

    class Meta:
        # managed = False
        db_table = 'radiology_order_queue'

