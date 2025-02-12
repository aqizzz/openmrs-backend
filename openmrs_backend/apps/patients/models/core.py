from django.db import models


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
    uuid = models.CharField(unique=True, max_length=38)

    class Meta:
        # managed = False
        db_table = 'metadatamapping_metadata_set'


class MetadatamappingMetadataSetMember(models.Model):
    metadata_set_member_id = models.AutoField(primary_key=True)
    metadata_set = models.ForeignKey(MetadatamappingMetadataSet, models.DO_NOTHING)
    metadata_class = models.CharField(max_length=1024)
    metadata_uuid = models.CharField(max_length=38)
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
    uuid = models.CharField(unique=True, max_length=38)

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
    uuid = models.CharField(unique=True, max_length=38)

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
    uuid = models.CharField(unique=True, max_length=38)

    class Meta:
        # managed = False
        db_table = 'metadatamapping_metadata_term_mapping'
        unique_together = (('metadata_source', 'code'),)


class MetadatasharingExportedPackage(models.Model):
    exported_package_id = models.AutoField(primary_key=True)
    uuid = models.CharField(unique=True, max_length=38)
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
    uuid = models.CharField(max_length=38)
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
    uuid = models.CharField(unique=True, max_length=38)
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

class GlobalProperty(models.Model):
    property = models.CharField(primary_key=True, max_length=255)
    property_value = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    uuid = models.CharField(unique=True, max_length=38)
    datatype = models.CharField(max_length=255, blank=True, null=True)
    datatype_config = models.TextField(blank=True, null=True)
    preferred_handler = models.CharField(max_length=255, blank=True, null=True)
    handler_config = models.TextField(blank=True, null=True)
    date_changed = models.DateTimeField(blank=True, null=True)
    changed_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='changed_by', blank=True, null=True)

    class Meta:
        # managed = False
        db_table = 'global_property'


class Concept(models.Model):
    concept_id = models.AutoField(primary_key=True)
    retired = models.IntegerField()
    short_name = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    form_text = models.TextField(blank=True, null=True)
    datatype = models.ForeignKey('ConceptDatatype', models.DO_NOTHING)
    class_field = models.ForeignKey('ConceptClass', models.DO_NOTHING, db_column='class_id')  # Field renamed because it was a Python reserved word.
    is_set = models.IntegerField()
    creator = models.ForeignKey('Users', models.DO_NOTHING, db_column='creator')
    date_created = models.DateTimeField()
    version = models.CharField(max_length=50, blank=True, null=True)
    changed_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='changed_by', related_name='concept_changed_by_set', blank=True, null=True)
    date_changed = models.DateTimeField(blank=True, null=True)
    retired_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='retired_by', related_name='concept_retired_by_set', blank=True, null=True)
    date_retired = models.DateTimeField(blank=True, null=True)
    retire_reason = models.CharField(max_length=255, blank=True, null=True)
    uuid = models.CharField(unique=True, max_length=38)

    class Meta:
        # managed = False
        db_table = 'concept'


class ConceptAnswer(models.Model):
    concept_answer_id = models.AutoField(primary_key=True)
    concept = models.ForeignKey(Concept, models.DO_NOTHING)
    answer_concept = models.ForeignKey(Concept, models.DO_NOTHING, db_column='answer_concept', related_name='conceptanswer_answer_concept_set', blank=True, null=True)
    answer_drug = models.ForeignKey('Drug', models.DO_NOTHING, db_column='answer_drug', blank=True, null=True)
    creator = models.ForeignKey('Users', models.DO_NOTHING, db_column='creator')
    date_created = models.DateTimeField()
    sort_weight = models.FloatField(blank=True, null=True)
    uuid = models.CharField(unique=True, max_length=38)

    class Meta:
        # managed = False
        db_table = 'concept_answer'


class ConceptAttribute(models.Model):
    concept_attribute_id = models.AutoField(primary_key=True)
    concept = models.ForeignKey(Concept, models.DO_NOTHING)
    attribute_type = models.ForeignKey('ConceptAttributeType', models.DO_NOTHING)
    value_reference = models.TextField()
    uuid = models.CharField(unique=True, max_length=38)
    creator = models.ForeignKey('Users', models.DO_NOTHING, db_column='creator')
    date_created = models.DateTimeField()
    changed_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='changed_by', related_name='conceptattribute_changed_by_set', blank=True, null=True)
    date_changed = models.DateTimeField(blank=True, null=True)
    voided = models.IntegerField()
    voided_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='voided_by', related_name='conceptattribute_voided_by_set', blank=True, null=True)
    date_voided = models.DateTimeField(blank=True, null=True)
    void_reason = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        # managed = False
        db_table = 'concept_attribute'


class ConceptAttributeType(models.Model):
    concept_attribute_type_id = models.AutoField(primary_key=True)
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
    changed_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='changed_by', related_name='conceptattributetype_changed_by_set', blank=True, null=True)
    date_changed = models.DateTimeField(blank=True, null=True)
    retired = models.IntegerField()
    retired_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='retired_by', related_name='conceptattributetype_retired_by_set', blank=True, null=True)
    date_retired = models.DateTimeField(blank=True, null=True)
    retire_reason = models.CharField(max_length=255, blank=True, null=True)
    uuid = models.CharField(unique=True, max_length=38)

    class Meta:
        # managed = False
        db_table = 'concept_attribute_type'


class ConceptClass(models.Model):
    concept_class_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255, blank=True, null=True)
    creator = models.ForeignKey('Users', models.DO_NOTHING, db_column='creator')
    date_created = models.DateTimeField()
    retired = models.IntegerField()
    retired_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='retired_by', related_name='conceptclass_retired_by_set', blank=True, null=True)
    date_retired = models.DateTimeField(blank=True, null=True)
    retire_reason = models.CharField(max_length=255, blank=True, null=True)
    uuid = models.CharField(unique=True, max_length=38)
    date_changed = models.DateTimeField(blank=True, null=True)
    changed_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='changed_by', related_name='conceptclass_changed_by_set', blank=True, null=True)

    class Meta:
        # managed = False
        db_table = 'concept_class'


class ConceptComplex(models.Model):
    concept = models.OneToOneField(Concept, models.DO_NOTHING, primary_key=True)
    handler = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        # managed = False
        db_table = 'concept_complex'


class ConceptDatatype(models.Model):
    concept_datatype_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    hl7_abbreviation = models.CharField(max_length=3, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    creator = models.ForeignKey('Users', models.DO_NOTHING, db_column='creator')
    date_created = models.DateTimeField()
    retired = models.IntegerField()
    retired_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='retired_by', related_name='conceptdatatype_retired_by_set', blank=True, null=True)
    date_retired = models.DateTimeField(blank=True, null=True)
    retire_reason = models.CharField(max_length=255, blank=True, null=True)
    uuid = models.CharField(unique=True, max_length=38)

    class Meta:
        # managed = False
        db_table = 'concept_datatype'


class ConceptDescription(models.Model):
    concept_description_id = models.AutoField(primary_key=True)
    concept = models.ForeignKey(Concept, models.DO_NOTHING)
    description = models.TextField()
    locale = models.CharField(max_length=50)
    creator = models.ForeignKey('Users', models.DO_NOTHING, db_column='creator')
    date_created = models.DateTimeField()
    changed_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='changed_by', related_name='conceptdescription_changed_by_set', blank=True, null=True)
    date_changed = models.DateTimeField(blank=True, null=True)
    uuid = models.CharField(unique=True, max_length=38)

    class Meta:
        # managed = False
        db_table = 'concept_description'


class ConceptMapType(models.Model):
    concept_map_type_id = models.AutoField(primary_key=True)
    name = models.CharField(unique=True, max_length=255)
    description = models.CharField(max_length=255, blank=True, null=True)
    creator = models.ForeignKey('Users', models.DO_NOTHING, db_column='creator')
    date_created = models.DateTimeField()
    changed_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='changed_by', related_name='conceptmaptype_changed_by_set', blank=True, null=True)
    date_changed = models.DateTimeField(blank=True, null=True)
    is_hidden = models.IntegerField()
    retired = models.IntegerField()
    retired_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='retired_by', related_name='conceptmaptype_retired_by_set', blank=True, null=True)
    date_retired = models.DateTimeField(blank=True, null=True)
    retire_reason = models.CharField(max_length=255, blank=True, null=True)
    uuid = models.CharField(unique=True, max_length=38)

    class Meta:
        # managed = False
        db_table = 'concept_map_type'


class ConceptName(models.Model):
    concept_name_id = models.AutoField(primary_key=True)
    concept = models.ForeignKey(Concept, models.DO_NOTHING, blank=True, null=True)
    name = models.CharField(max_length=255)
    locale = models.CharField(max_length=50)
    locale_preferred = models.IntegerField(blank=True, null=True)
    creator = models.ForeignKey('Users', models.DO_NOTHING, db_column='creator')
    date_created = models.DateTimeField()
    concept_name_type = models.CharField(max_length=50, blank=True, null=True)
    voided = models.IntegerField()
    voided_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='voided_by', related_name='conceptname_voided_by_set', blank=True, null=True)
    date_voided = models.DateTimeField(blank=True, null=True)
    void_reason = models.CharField(max_length=255, blank=True, null=True)
    uuid = models.CharField(unique=True, max_length=38)
    date_changed = models.DateTimeField(blank=True, null=True)
    changed_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='changed_by', related_name='conceptname_changed_by_set', blank=True, null=True)

    class Meta:
        # managed = False
        db_table = 'concept_name'


class ConceptNameTag(models.Model):
    concept_name_tag_id = models.AutoField(primary_key=True)
    tag = models.CharField(unique=True, max_length=50)
    description = models.TextField(blank=True, null=True)
    creator = models.IntegerField()
    date_created = models.DateTimeField()
    voided = models.IntegerField()
    voided_by = models.IntegerField(blank=True, null=True)
    date_voided = models.DateTimeField(blank=True, null=True)
    void_reason = models.CharField(max_length=255, blank=True, null=True)
    uuid = models.CharField(unique=True, max_length=38)
    date_changed = models.DateTimeField(blank=True, null=True)
    changed_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='changed_by', blank=True, null=True)

    class Meta:
        # managed = False
        db_table = 'concept_name_tag'


class ConceptNameTagMap(models.Model):
    concept_name = models.ForeignKey(ConceptName, models.DO_NOTHING)
    concept_name_tag = models.ForeignKey(ConceptNameTag, models.DO_NOTHING)

    class Meta:
        # managed = False
        db_table = 'concept_name_tag_map'


class ConceptNumeric(models.Model):
    concept = models.OneToOneField(Concept, models.DO_NOTHING, primary_key=True)
    hi_absolute = models.FloatField(blank=True, null=True)
    hi_critical = models.FloatField(blank=True, null=True)
    hi_normal = models.FloatField(blank=True, null=True)
    low_absolute = models.FloatField(blank=True, null=True)
    low_critical = models.FloatField(blank=True, null=True)
    low_normal = models.FloatField(blank=True, null=True)
    units = models.CharField(max_length=50, blank=True, null=True)
    allow_decimal = models.IntegerField(blank=True, null=True)
    display_precision = models.IntegerField(blank=True, null=True)

    class Meta:
        # managed = False
        db_table = 'concept_numeric'


class ConceptProposal(models.Model):
    concept_proposal_id = models.AutoField(primary_key=True)
    concept = models.ForeignKey(Concept, models.DO_NOTHING, blank=True, null=True)
    encounter = models.ForeignKey('Encounter', models.DO_NOTHING, blank=True, null=True)
    original_text = models.CharField(max_length=255)
    final_text = models.CharField(max_length=255, blank=True, null=True)
    obs = models.ForeignKey('Obs', models.DO_NOTHING, blank=True, null=True)
    obs_concept = models.ForeignKey(Concept, models.DO_NOTHING, related_name='conceptproposal_obs_concept_set', blank=True, null=True)
    state = models.CharField(max_length=32)
    comments = models.CharField(max_length=255, blank=True, null=True)
    creator = models.ForeignKey('Users', models.DO_NOTHING, db_column='creator')
    date_created = models.DateTimeField()
    changed_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='changed_by', related_name='conceptproposal_changed_by_set', blank=True, null=True)
    date_changed = models.DateTimeField(blank=True, null=True)
    locale = models.CharField(max_length=50)
    uuid = models.CharField(unique=True, max_length=38)

    class Meta:
        # managed = False
        db_table = 'concept_proposal'


class ConceptProposalTagMap(models.Model):
    concept_proposal = models.ForeignKey(ConceptProposal, models.DO_NOTHING)
    concept_name_tag = models.ForeignKey(ConceptNameTag, models.DO_NOTHING)

    class Meta:
        # managed = False
        db_table = 'concept_proposal_tag_map'


class ConceptReferenceMap(models.Model):
    concept_map_id = models.AutoField(primary_key=True)
    concept_reference_term = models.ForeignKey('ConceptReferenceTerm', models.DO_NOTHING)
    concept_map_type = models.ForeignKey(ConceptMapType, models.DO_NOTHING)
    creator = models.ForeignKey('Users', models.DO_NOTHING, db_column='creator')
    date_created = models.DateTimeField()
    concept = models.ForeignKey(Concept, models.DO_NOTHING)
    changed_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='changed_by', related_name='conceptreferencemap_changed_by_set', blank=True, null=True)
    date_changed = models.DateTimeField(blank=True, null=True)
    uuid = models.CharField(unique=True, max_length=38)

    class Meta:
        # managed = False
        db_table = 'concept_reference_map'


class ConceptReferenceSource(models.Model):
    concept_source_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    description = models.TextField()
    hl7_code = models.CharField(unique=True, max_length=50, blank=True, null=True)
    creator = models.ForeignKey('Users', models.DO_NOTHING, db_column='creator')
    date_created = models.DateTimeField()
    retired = models.IntegerField()
    retired_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='retired_by', related_name='conceptreferencesource_retired_by_set', blank=True, null=True)
    date_retired = models.DateTimeField(blank=True, null=True)
    retire_reason = models.CharField(max_length=255, blank=True, null=True)
    uuid = models.CharField(unique=True, max_length=38)
    unique_id = models.CharField(unique=True, max_length=250, blank=True, null=True)
    date_changed = models.DateTimeField(blank=True, null=True)
    changed_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='changed_by', related_name='conceptreferencesource_changed_by_set', blank=True, null=True)

    class Meta:
        # managed = False
        db_table = 'concept_reference_source'


class ConceptReferenceTerm(models.Model):
    concept_reference_term_id = models.AutoField(primary_key=True)
    concept_source = models.ForeignKey(ConceptReferenceSource, models.DO_NOTHING)
    name = models.CharField(max_length=255, blank=True, null=True)
    code = models.CharField(max_length=255)
    version = models.CharField(max_length=255, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    creator = models.ForeignKey('Users', models.DO_NOTHING, db_column='creator')
    date_created = models.DateTimeField()
    date_changed = models.DateTimeField(blank=True, null=True)
    changed_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='changed_by', related_name='conceptreferenceterm_changed_by_set', blank=True, null=True)
    retired = models.IntegerField()
    retired_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='retired_by', related_name='conceptreferenceterm_retired_by_set', blank=True, null=True)
    date_retired = models.DateTimeField(blank=True, null=True)
    retire_reason = models.CharField(max_length=255, blank=True, null=True)
    uuid = models.CharField(unique=True, max_length=38)

    class Meta:
        # managed = False
        db_table = 'concept_reference_term'


class ConceptReferenceTermMap(models.Model):
    concept_reference_term_map_id = models.AutoField(primary_key=True)
    term_a = models.ForeignKey(ConceptReferenceTerm, models.DO_NOTHING)
    term_b = models.ForeignKey(ConceptReferenceTerm, models.DO_NOTHING, related_name='conceptreferencetermmap_term_b_set')
    a_is_to_b = models.ForeignKey(ConceptMapType, models.DO_NOTHING)
    creator = models.ForeignKey('Users', models.DO_NOTHING, db_column='creator')
    date_created = models.DateTimeField()
    changed_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='changed_by', related_name='conceptreferencetermmap_changed_by_set', blank=True, null=True)
    date_changed = models.DateTimeField(blank=True, null=True)
    uuid = models.CharField(unique=True, max_length=38)

    class Meta:
        # managed = False
        db_table = 'concept_reference_term_map'


class ConceptSet(models.Model):
    concept_set_id = models.AutoField(primary_key=True)
    concept_id = models.IntegerField(default=0)
    concept_set_ref = models.ForeignKey(Concept, models.DO_NOTHING, db_column='concept_set', to_field='concept_id', related_name='concept_sets', related_query_name='concept_set', default=0)
    sort_weight = models.FloatField(blank=True, null=True)
    creator = models.ForeignKey('Users', models.DO_NOTHING, db_column='creator', default=0)
    date_created = models.DateTimeField()
    uuid = models.CharField(unique=True, max_length=38)

    class Meta:
        # managed = False
        db_table = 'concept_set'


class ConceptStateConversion(models.Model):
    concept_state_conversion_id = models.AutoField(primary_key=True)
    concept = models.ForeignKey(Concept, models.DO_NOTHING, blank=True, null=True)
    program_workflow = models.ForeignKey('ProgramWorkflow', models.DO_NOTHING, blank=True, null=True)
    program_workflow_state = models.ForeignKey('ProgramWorkflowState', models.DO_NOTHING, blank=True, null=True)
    uuid = models.CharField(unique=True, max_length=38)

    class Meta:
        # managed = False
        db_table = 'concept_state_conversion'
        unique_together = (('program_workflow', 'concept'),)


class ConceptStopWord(models.Model):
    concept_stop_word_id = models.AutoField(primary_key=True)
    word = models.CharField(max_length=50)
    locale = models.CharField(max_length=50, blank=True, null=True)
    uuid = models.CharField(max_length=38)

    class Meta:
        # managed = False
        db_table = 'concept_stop_word'
        unique_together = (('word', 'locale'),)

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
    uuid = models.CharField(unique=True, max_length=38)

    class Meta:
        # managed = False
        db_table = 'care_setting'

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
    uuid = models.CharField(unique=True, max_length=38)
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
    location_type_concept = models.ForeignKey(Concept, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        # managed = False
        db_table = 'location'


class LocationAttribute(models.Model):
    location_attribute_id = models.AutoField(primary_key=True)
    location = models.ForeignKey(Location, models.DO_NOTHING)
    attribute_type = models.ForeignKey('LocationAttributeType', models.DO_NOTHING)
    value_reference = models.TextField()
    uuid = models.CharField(unique=True, max_length=38)
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
    uuid = models.CharField(unique=True, max_length=38)

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
    uuid = models.CharField(unique=True, max_length=38)
    changed_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='changed_by', related_name='locationtag_changed_by_set', blank=True, null=True)
    date_changed = models.DateTimeField(blank=True, null=True)

    class Meta:
        # managed = False
        db_table = 'location_tag'


class LocationTagMap(models.Model):
    location = models.OneToOneField(Location, models.DO_NOTHING, primary_key=True)  # The composite primary key (location_id, location_tag_id) found, that is not supported. The first column is selected.
    location_tag = models.ForeignKey(LocationTag, models.DO_NOTHING)

    class Meta:
        # managed = False
        db_table = 'location_tag_map'
        unique_together = (('location', 'location_tag'),)

# Diagnosis and drug related models
class DiagnosisAttribute(models.Model):
    diagnosis_attribute_id = models.AutoField(primary_key=True)
    diagnosis = models.ForeignKey('EncounterDiagnosis', models.DO_NOTHING)
    attribute_type = models.ForeignKey('DiagnosisAttributeType', models.DO_NOTHING)
    value_reference = models.TextField()
    uuid = models.CharField(unique=True, max_length=38)
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
    uuid = models.CharField(unique=True, max_length=38)

    class Meta:
        # managed = False
        db_table = 'diagnosis_attribute_type'


class Drug(models.Model):
    drug_id = models.AutoField(primary_key=True)
    concept = models.ForeignKey(Concept, models.DO_NOTHING)
    name = models.CharField(max_length=255, blank=True, null=True)
    combination = models.IntegerField()
    dosage_form = models.ForeignKey(Concept, models.DO_NOTHING, db_column='dosage_form', related_name='drug_dosage_form_set', blank=True, null=True)
    maximum_daily_dose = models.FloatField(blank=True, null=True)
    minimum_daily_dose = models.FloatField(blank=True, null=True)
    route = models.ForeignKey(Concept, models.DO_NOTHING, db_column='route', related_name='drug_route_set', blank=True, null=True)
    creator = models.ForeignKey('Users', models.DO_NOTHING, db_column='creator')
    date_created = models.DateTimeField()
    retired = models.IntegerField()
    changed_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='changed_by', related_name='drug_changed_by_set', blank=True, null=True)
    date_changed = models.DateTimeField(blank=True, null=True)
    retired_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='retired_by', related_name='drug_retired_by_set', blank=True, null=True)
    date_retired = models.DateTimeField(blank=True, null=True)
    retire_reason = models.CharField(max_length=255, blank=True, null=True)
    uuid = models.CharField(unique=True, max_length=38)
    strength = models.CharField(max_length=255, blank=True, null=True)
    dose_limit_units = models.ForeignKey(Concept, models.DO_NOTHING, db_column='dose_limit_units', related_name='drug_dose_limit_units_set', blank=True, null=True)

    class Meta:
        # managed = False
        db_table = 'drug'


class DrugIngredient(models.Model):
    drug = models.OneToOneField(Drug, models.DO_NOTHING, primary_key=True)  # The composite primary key (drug_id, ingredient_id) found, that is not supported. The first column is selected.
    ingredient = models.ForeignKey(Concept, models.DO_NOTHING)
    uuid = models.CharField(unique=True, max_length=38)
    strength = models.FloatField(blank=True, null=True)
    units = models.ForeignKey(Concept, models.DO_NOTHING, db_column='units', related_name='drugingredient_units_set', blank=True, null=True)

    class Meta:
        # managed = False
        db_table = 'drug_ingredient'
        unique_together = (('drug', 'ingredient'),)


class DrugOrder(models.Model):
    order = models.OneToOneField('Orders', models.DO_NOTHING, primary_key=True)
    drug_inventory = models.ForeignKey(Drug, models.DO_NOTHING, blank=True, null=True)
    dose = models.FloatField(blank=True, null=True)
    as_needed = models.IntegerField(blank=True, null=True)
    dosing_type = models.CharField(max_length=255, blank=True, null=True)
    quantity = models.FloatField(blank=True, null=True)
    as_needed_condition = models.CharField(max_length=255, blank=True, null=True)
    num_refills = models.IntegerField(blank=True, null=True)
    dosing_instructions = models.TextField(blank=True, null=True)
    duration = models.IntegerField(blank=True, null=True)
    duration_units = models.ForeignKey(Concept, models.DO_NOTHING, db_column='duration_units', blank=True, null=True)
    quantity_units = models.ForeignKey(Concept, models.DO_NOTHING, db_column='quantity_units', related_name='drugorder_quantity_units_set', blank=True, null=True)
    route = models.ForeignKey(Concept, models.DO_NOTHING, db_column='route', related_name='drugorder_route_set', blank=True, null=True)
    dose_units = models.ForeignKey(Concept, models.DO_NOTHING, db_column='dose_units', related_name='drugorder_dose_units_set', blank=True, null=True)
    frequency = models.ForeignKey('OrderFrequency', models.DO_NOTHING, db_column='frequency', blank=True, null=True)
    brand_name = models.CharField(max_length=255, blank=True, null=True)
    dispense_as_written = models.IntegerField()
    drug_non_coded = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        # managed = False
        db_table = 'drug_order'


class DrugReferenceMap(models.Model):
    drug_reference_map_id = models.AutoField(primary_key=True)
    drug = models.ForeignKey(Drug, models.DO_NOTHING)
    term = models.ForeignKey(ConceptReferenceTerm, models.DO_NOTHING)
    concept_map_type = models.ForeignKey(ConceptMapType, models.DO_NOTHING, db_column='concept_map_type')
    creator = models.ForeignKey('Users', models.DO_NOTHING, db_column='creator')
    date_created = models.DateTimeField()
    retired = models.IntegerField()
    retired_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='retired_by', related_name='drugreferencemap_retired_by_set', blank=True, null=True)
    date_retired = models.DateTimeField(blank=True, null=True)
    retire_reason = models.CharField(max_length=255, blank=True, null=True)
    changed_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='changed_by', related_name='drugreferencemap_changed_by_set', blank=True, null=True)
    date_changed = models.DateTimeField(blank=True, null=True)
    uuid = models.CharField(unique=True, max_length=38)

    class Meta:
        # managed = False
        db_table = 'drug_reference_map'



# Order-related models
class OrderAttribute(models.Model):
    order_attribute_id = models.AutoField(primary_key=True)
    order = models.ForeignKey('Orders', models.DO_NOTHING)
    attribute_type = models.ForeignKey('OrderAttributeType', models.DO_NOTHING)
    value_reference = models.TextField()
    uuid = models.CharField(unique=True, max_length=38)
    creator = models.ForeignKey('Users', models.DO_NOTHING, db_column='creator')
    date_created = models.DateTimeField()
    changed_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='changed_by', related_name='orderattribute_changed_by_set', blank=True, null=True)
    date_changed = models.DateTimeField(blank=True, null=True)
    voided = models.IntegerField()
    voided_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='voided_by', related_name='orderattribute_voided_by_set', blank=True, null=True)
    date_voided = models.DateTimeField(blank=True, null=True)
    void_reason = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        # managed = False
        db_table = 'order_attribute'


class OrderAttributeType(models.Model):
    order_attribute_type_id = models.AutoField(primary_key=True)
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
    changed_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='changed_by', related_name='orderattributetype_changed_by_set', blank=True, null=True)
    date_changed = models.DateTimeField(blank=True, null=True)
    retired = models.IntegerField()
    retired_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='retired_by', related_name='orderattributetype_retired_by_set', blank=True, null=True)
    date_retired = models.DateTimeField(blank=True, null=True)
    retire_reason = models.CharField(max_length=255, blank=True, null=True)
    uuid = models.CharField(unique=True, max_length=38)

    class Meta:
        # managed = False
        db_table = 'order_attribute_type'


class OrderFrequency(models.Model):
    order_frequency_id = models.AutoField(primary_key=True)
    concept = models.OneToOneField(Concept, models.DO_NOTHING)
    frequency_per_day = models.FloatField(blank=True, null=True)
    creator = models.ForeignKey('Users', models.DO_NOTHING, db_column='creator')
    date_created = models.DateTimeField()
    retired = models.IntegerField()
    retired_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='retired_by', related_name='orderfrequency_retired_by_set', blank=True, null=True)
    date_retired = models.DateTimeField(blank=True, null=True)
    retire_reason = models.CharField(max_length=255, blank=True, null=True)
    changed_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='changed_by', related_name='orderfrequency_changed_by_set', blank=True, null=True)
    date_changed = models.DateTimeField(blank=True, null=True)
    uuid = models.CharField(unique=True, max_length=38)

    class Meta:
        # managed = False
        db_table = 'order_frequency'


class OrderGroup(models.Model):
    order_group_id = models.AutoField(primary_key=True)
    order_set = models.ForeignKey('OrderSet', models.DO_NOTHING, blank=True, null=True)
    patient = models.ForeignKey('Patient', models.DO_NOTHING)
    encounter = models.ForeignKey('Encounter', models.DO_NOTHING)
    creator = models.ForeignKey('Users', models.DO_NOTHING, db_column='creator')
    date_created = models.DateTimeField()
    voided = models.IntegerField()
    voided_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='voided_by', related_name='ordergroup_voided_by_set', blank=True, null=True)
    date_voided = models.DateTimeField(blank=True, null=True)
    void_reason = models.CharField(max_length=255, blank=True, null=True)
    changed_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='changed_by', related_name='ordergroup_changed_by_set', blank=True, null=True)
    date_changed = models.DateTimeField(blank=True, null=True)
    uuid = models.CharField(unique=True, max_length=38)
    order_group_reason = models.ForeignKey(Concept, models.DO_NOTHING, db_column='order_group_reason', blank=True, null=True)
    parent_order_group = models.ForeignKey('self', models.DO_NOTHING, db_column='parent_order_group', blank=True, null=True)
    previous_order_group = models.ForeignKey('self', models.DO_NOTHING, db_column='previous_order_group', related_name='ordergroup_previous_order_group_set', blank=True, null=True)

    class Meta:
        # managed = False
        db_table = 'order_group'


class OrderGroupAttribute(models.Model):
    order_group_attribute_id = models.AutoField(primary_key=True)
    order_group = models.ForeignKey(OrderGroup, models.DO_NOTHING)
    attribute_type = models.ForeignKey('OrderGroupAttributeType', models.DO_NOTHING)
    value_reference = models.TextField()
    uuid = models.CharField(unique=True, max_length=38)
    creator = models.ForeignKey('Users', models.DO_NOTHING, db_column='creator')
    date_created = models.DateTimeField()
    changed_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='changed_by', related_name='ordergroupattribute_changed_by_set', blank=True, null=True)
    date_changed = models.DateTimeField(blank=True, null=True)
    voided = models.IntegerField()
    voided_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='voided_by', related_name='ordergroupattribute_voided_by_set', blank=True, null=True)
    date_voided = models.DateTimeField(blank=True, null=True)
    void_reason = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        # managed = False
        db_table = 'order_group_attribute'


class OrderGroupAttributeType(models.Model):
    order_group_attribute_type_id = models.AutoField(primary_key=True)
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
    changed_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='changed_by', related_name='ordergroupattributetype_changed_by_set', blank=True, null=True)
    date_changed = models.DateTimeField(blank=True, null=True)
    retired = models.IntegerField()
    retired_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='retired_by', related_name='ordergroupattributetype_retired_by_set', blank=True, null=True)
    date_retired = models.DateTimeField(blank=True, null=True)
    retire_reason = models.CharField(max_length=255, blank=True, null=True)
    uuid = models.CharField(unique=True, max_length=38)

    class Meta:
        # managed = False
        db_table = 'order_group_attribute_type'


class OrderLog(models.Model):
    radiology_order = models.ForeignKey('RadiologyOrder', models.DO_NOTHING)
    modality = models.ForeignKey('Modality', models.DO_NOTHING)
    hl7_request = models.TextField()
    hl7_response = models.TextField()

    class Meta:
        # managed = False
        db_table = 'order_log'


class OrderSet(models.Model):
    order_set_id = models.AutoField(primary_key=True)
    operator = models.CharField(max_length=50)
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=1000, blank=True, null=True)
    creator = models.ForeignKey('Users', models.DO_NOTHING, db_column='creator')
    date_created = models.DateTimeField()
    retired = models.IntegerField()
    retired_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='retired_by', related_name='orderset_retired_by_set', blank=True, null=True)
    date_retired = models.DateTimeField(blank=True, null=True)
    retire_reason = models.CharField(max_length=255, blank=True, null=True)
    changed_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='changed_by', related_name='orderset_changed_by_set', blank=True, null=True)
    date_changed = models.DateTimeField(blank=True, null=True)
    uuid = models.CharField(unique=True, max_length=38)
    category = models.ForeignKey(Concept, models.DO_NOTHING, db_column='category', blank=True, null=True)

    class Meta:
        # managed = False
        db_table = 'order_set'


class OrderSetAttribute(models.Model):
    order_set_attribute_id = models.AutoField(primary_key=True)
    order_set = models.ForeignKey(OrderSet, models.DO_NOTHING)
    attribute_type = models.ForeignKey('OrderSetAttributeType', models.DO_NOTHING)
    value_reference = models.TextField()
    uuid = models.CharField(unique=True, max_length=38)
    creator = models.ForeignKey('Users', models.DO_NOTHING, db_column='creator')
    date_created = models.DateTimeField()
    changed_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='changed_by', related_name='ordersetattribute_changed_by_set', blank=True, null=True)
    date_changed = models.DateTimeField(blank=True, null=True)
    voided = models.IntegerField()
    voided_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='voided_by', related_name='ordersetattribute_voided_by_set', blank=True, null=True)
    date_voided = models.DateTimeField(blank=True, null=True)
    void_reason = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        # managed = False
        db_table = 'order_set_attribute'


class OrderSetAttributeType(models.Model):
    order_set_attribute_type_id = models.AutoField(primary_key=True)
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
    changed_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='changed_by', related_name='ordersetattributetype_changed_by_set', blank=True, null=True)
    date_changed = models.DateTimeField(blank=True, null=True)
    retired = models.IntegerField()
    retired_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='retired_by', related_name='ordersetattributetype_retired_by_set', blank=True, null=True)
    date_retired = models.DateTimeField(blank=True, null=True)
    retire_reason = models.CharField(max_length=255, blank=True, null=True)
    uuid = models.CharField(unique=True, max_length=38)

    class Meta:
        # managed = False
        db_table = 'order_set_attribute_type'


class OrderSetMember(models.Model):
    order_set_member_id = models.AutoField(primary_key=True)
    order_type = models.ForeignKey('OrderType', models.DO_NOTHING, db_column='order_type')
    order_template = models.TextField(blank=True, null=True)
    order_template_type = models.CharField(max_length=1024, blank=True, null=True)
    order_set = models.ForeignKey(OrderSet, models.DO_NOTHING)
    sequence_number = models.IntegerField()
    concept = models.ForeignKey(Concept, models.DO_NOTHING)
    creator = models.ForeignKey('Users', models.DO_NOTHING, db_column='creator')
    date_created = models.DateTimeField()
    retired = models.IntegerField()
    retired_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='retired_by', related_name='ordersetmember_retired_by_set', blank=True, null=True)
    date_retired = models.DateTimeField(blank=True, null=True)
    retire_reason = models.CharField(max_length=255, blank=True, null=True)
    changed_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='changed_by', related_name='ordersetmember_changed_by_set', blank=True, null=True)
    date_changed = models.DateTimeField(blank=True, null=True)
    uuid = models.CharField(unique=True, max_length=38)

    class Meta:
        # managed = False
        db_table = 'order_set_member'


class OrderTemplate(models.Model):
    order_template_id = models.AutoField(primary_key=True)
    uuid = models.CharField(unique=True, max_length=38)
    name = models.CharField(unique=True, max_length=255)
    description = models.CharField(max_length=255)
    concept = models.ForeignKey(Concept, models.DO_NOTHING, db_column='concept')
    drug = models.ForeignKey(Drug, models.DO_NOTHING, db_column='drug', blank=True, null=True)
    template = models.TextField()
    creator = models.ForeignKey('Users', models.DO_NOTHING, db_column='creator')
    date_created = models.DateTimeField()
    changed_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='changed_by', related_name='ordertemplate_changed_by_set', blank=True, null=True)
    date_changed = models.DateTimeField(blank=True, null=True)
    retired = models.IntegerField()
    retired_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='retired_by', related_name='ordertemplate_retired_by_set', blank=True, null=True)
    date_retired = models.DateTimeField(blank=True, null=True)
    retire_reason = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        # managed = False
        db_table = 'order_template'


class OrderType(models.Model):
    order_type_id = models.AutoField(primary_key=True)
    name = models.CharField(unique=True, max_length=255)
    description = models.TextField(blank=True, null=True)
    creator = models.ForeignKey('Users', models.DO_NOTHING, db_column='creator')
    date_created = models.DateTimeField()
    retired = models.IntegerField()
    retired_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='retired_by', related_name='ordertype_retired_by_set', blank=True, null=True)
    date_retired = models.DateTimeField(blank=True, null=True)
    retire_reason = models.CharField(max_length=255, blank=True, null=True)
    uuid = models.CharField(unique=True, max_length=38)
    java_class_name = models.CharField(max_length=255)
    parent = models.ForeignKey('self', models.DO_NOTHING, db_column='parent', blank=True, null=True)
    changed_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='changed_by', related_name='ordertype_changed_by_set', blank=True, null=True)
    date_changed = models.DateTimeField(blank=True, null=True)

    class Meta:
        # managed = False
        db_table = 'order_type'


class OrderTypeClassMap(models.Model):
    order_type = models.OneToOneField(OrderType, models.DO_NOTHING, primary_key=True)  # The composite primary key (order_type_id, concept_class_id) found, that is not supported. The first column is selected.
    concept_class = models.OneToOneField(ConceptClass, models.DO_NOTHING)

    class Meta:
        # managed = False
        db_table = 'order_type_class_map'
        unique_together = (('order_type', 'concept_class'),)


class Orders(models.Model):
    order_id = models.AutoField(primary_key=True)
    order_type = models.ForeignKey(OrderType, models.DO_NOTHING)
    concept_id = models.IntegerField()
    orderer = models.ForeignKey('Provider', models.DO_NOTHING, db_column='orderer')
    encounter = models.ForeignKey('Encounter', models.DO_NOTHING)
    instructions = models.TextField(blank=True, null=True)
    date_activated = models.DateTimeField(blank=True, null=True)
    auto_expire_date = models.DateTimeField(blank=True, null=True)
    date_stopped = models.DateTimeField(blank=True, null=True)
    order_reason = models.ForeignKey(Concept, models.DO_NOTHING, db_column='order_reason', blank=True, null=True)
    order_reason_non_coded = models.CharField(max_length=255, blank=True, null=True)
    creator = models.ForeignKey('Users', models.DO_NOTHING, db_column='creator')
    date_created = models.DateTimeField()
    voided = models.IntegerField()
    voided_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='voided_by', related_name='orders_voided_by_set', blank=True, null=True)
    date_voided = models.DateTimeField(blank=True, null=True)
    void_reason = models.CharField(max_length=255, blank=True, null=True)
    patient = models.ForeignKey('Patient', models.DO_NOTHING)
    accession_number = models.CharField(max_length=255, blank=True, null=True)
    uuid = models.CharField(unique=True, max_length=38)
    urgency = models.CharField(max_length=50)
    order_number = models.CharField(max_length=50)
    previous_order = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    order_action = models.CharField(max_length=50)
    comment_to_fulfiller = models.CharField(max_length=1024, blank=True, null=True)
    care_setting = models.ForeignKey(CareSetting, models.DO_NOTHING, db_column='care_setting')
    scheduled_date = models.DateTimeField(blank=True, null=True)
    order_group = models.ForeignKey(OrderGroup, models.DO_NOTHING, blank=True, null=True)
    sort_weight = models.FloatField(blank=True, null=True)
    fulfiller_comment = models.CharField(max_length=1024, blank=True, null=True)
    fulfiller_status = models.CharField(max_length=50, blank=True, null=True)
    form_namespace_and_path = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        # managed = False
        db_table = 'orders'


class Obs(models.Model):
    obs_id = models.AutoField(primary_key=True)
    person = models.ForeignKey('Person', models.DO_NOTHING)
    concept = models.ForeignKey(Concept, models.DO_NOTHING)
    encounter = models.ForeignKey('Encounter', models.DO_NOTHING, blank=True, null=True)
    order = models.ForeignKey('Orders', models.DO_NOTHING, blank=True, null=True)
    obs_datetime = models.DateTimeField()
    location = models.ForeignKey(Location, models.DO_NOTHING, blank=True, null=True)
    obs_group = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    accession_number = models.CharField(max_length=255, blank=True, null=True)
    value_group_id = models.IntegerField(blank=True, null=True)
    value_coded = models.ForeignKey(Concept, models.DO_NOTHING, db_column='value_coded', related_name='obs_value_coded_set', blank=True, null=True)
    value_coded_name = models.ForeignKey(ConceptName, models.DO_NOTHING, blank=True, null=True)
    value_drug = models.ForeignKey(Drug, models.DO_NOTHING, db_column='value_drug', blank=True, null=True)
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
    uuid = models.CharField(unique=True, max_length=38)
    previous_version = models.ForeignKey('self', models.DO_NOTHING, db_column='previous_version', related_name='obs_previous_version_set', blank=True, null=True)
    form_namespace_and_path = models.CharField(max_length=255, blank=True, null=True)
    status = models.CharField(max_length=16)
    interpretation = models.CharField(max_length=32, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'obs'

class Program(models.Model):
    program_id = models.AutoField(primary_key=True)
    concept = models.ForeignKey(Concept, models.DO_NOTHING)
    outcomes_concept = models.ForeignKey(Concept, models.DO_NOTHING, related_name='program_outcomes_concept_set', blank=True, null=True)
    creator = models.ForeignKey('Users', models.DO_NOTHING, db_column='creator')
    date_created = models.DateTimeField()
    changed_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='changed_by', related_name='program_changed_by_set', blank=True, null=True)
    date_changed = models.DateTimeField(blank=True, null=True)
    retired = models.IntegerField()
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True, null=True)
    uuid = models.CharField(unique=True, max_length=38)

    class Meta:
        managed = False
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
    uuid = models.CharField(unique=True, max_length=38)

    class Meta:
        managed = False
        db_table = 'program_attribute_type'


class ProgramWorkflow(models.Model):
    program_workflow_id = models.AutoField(primary_key=True)
    program = models.ForeignKey('Program', models.DO_NOTHING)
    concept = models.ForeignKey(Concept, models.DO_NOTHING)
    creator = models.ForeignKey('Users', models.DO_NOTHING, db_column='creator')
    date_created = models.DateTimeField()
    retired = models.IntegerField()
    changed_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='changed_by', related_name='programworkflow_changed_by_set', blank=True, null=True)
    date_changed = models.DateTimeField(blank=True, null=True)
    uuid = models.CharField(unique=True, max_length=38)

    class Meta:
        managed = False
        db_table = 'program_workflow'


class ProgramWorkflowState(models.Model):
    program_workflow_state_id = models.AutoField(primary_key=True)
    program_workflow = models.ForeignKey(ProgramWorkflow, models.DO_NOTHING)
    concept = models.ForeignKey(Concept, models.DO_NOTHING)
    initial = models.IntegerField()
    terminal = models.IntegerField()
    creator = models.ForeignKey('Users', models.DO_NOTHING, db_column='creator')
    date_created = models.DateTimeField()
    retired = models.IntegerField()
    changed_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='changed_by', related_name='programworkflowstate_changed_by_set', blank=True, null=True)
    date_changed = models.DateTimeField(blank=True, null=True)
    uuid = models.CharField(unique=True, max_length=38)

    class Meta:
        managed = False
        db_table = 'program_workflow_state'

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
    uuid = models.CharField(unique=True, max_length=38)

    class Meta:
        managed = False
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
    uuid = models.CharField(unique=True, max_length=38)

    class Meta:
        managed = False
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
    uuid = models.CharField(unique=True, max_length=38)
    date_changed = models.DateTimeField(blank=True, null=True)
    changed_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='changed_by', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'form_resource'
        unique_together = (('form', 'name'),)

class Field(models.Model):
    field_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    field_type = models.ForeignKey('FieldType', models.DO_NOTHING, db_column='field_type', blank=True, null=True)
    concept = models.ForeignKey(Concept, models.DO_NOTHING, blank=True, null=True)
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
    uuid = models.CharField(unique=True, max_length=38)

    class Meta:
        managed = False
        db_table = 'field'


class FieldAnswer(models.Model):
    field = models.OneToOneField(Field, models.DO_NOTHING, primary_key=True)  # The composite primary key (field_id, answer_id) found, that is not supported. The first column is selected.
    answer = models.ForeignKey(Concept, models.DO_NOTHING)
    creator = models.ForeignKey('Users', models.DO_NOTHING, db_column='creator')
    date_created = models.DateTimeField()
    uuid = models.CharField(unique=True, max_length=38)

    class Meta:
        managed = False
        db_table = 'field_answer'
        unique_together = (('field', 'answer'),)


class FieldType(models.Model):
    field_type_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    is_set = models.IntegerField()
    creator = models.ForeignKey('Users', models.DO_NOTHING, db_column='creator')
    date_created = models.DateTimeField()
    uuid = models.CharField(unique=True, max_length=38)

    class Meta:
        managed = False
        db_table = 'field_type'


class RadiologyOrder(models.Model):
    order = models.OneToOneField(Orders, models.DO_NOTHING, primary_key=True)
    body_site = models.ForeignKey(Concept, models.DO_NOTHING, db_column='body_site', blank=True, null=True)
    specimen_source = models.ForeignKey(Concept, models.DO_NOTHING, db_column='specimen_source', related_name='radiologyorder_specimen_source_set', blank=True, null=True)
    specimen_type = models.ForeignKey(Concept, models.DO_NOTHING, db_column='specimen_type', related_name='radiologyorder_specimen_type_set', blank=True, null=True)
    laterality = models.CharField(max_length=20, blank=True, null=True)
    clinical_history = models.TextField(blank=True, null=True)
    frequency = models.ForeignKey(OrderFrequency, models.DO_NOTHING, db_column='frequency', blank=True, null=True)
    number_of_repeats = models.IntegerField(blank=True, null=True)
    location = models.ForeignKey(Concept, models.DO_NOTHING, db_column='location', related_name='radiologyorder_location_set', blank=True, null=True)
    radiology_status = models.CharField(max_length=20, blank=True, null=True)
    related_radiology_order = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'radiology_order'


class RadiologyOrderQueue(models.Model):
    radiology_order = models.ForeignKey(RadiologyOrder, models.DO_NOTHING)
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
    uuid = models.CharField(unique=True, max_length=38)

    class Meta:
        managed = False
        db_table = 'radiology_order_queue'

