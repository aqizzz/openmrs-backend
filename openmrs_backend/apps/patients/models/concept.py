from django.db import models
import uuid

# Create your models here.

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
    uuid = models.CharField(unique=True, max_length=38, default=uuid.uuid4)

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
    uuid = models.CharField(unique=True, max_length=38, default=uuid.uuid4)

    class Meta:
        # managed = False
        db_table = 'concept_answer'


class ConceptAttribute(models.Model):
    concept_attribute_id = models.AutoField(primary_key=True)
    concept = models.ForeignKey(Concept, models.DO_NOTHING)
    attribute_type = models.ForeignKey('ConceptAttributeType', models.DO_NOTHING)
    value_reference = models.TextField()
    uuid = models.CharField(unique=True, max_length=38, default=uuid.uuid4)
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
    uuid = models.CharField(unique=True, max_length=38, default=uuid.uuid4)

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
    uuid = models.CharField(unique=True, max_length=38, default=uuid.uuid4)
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
    uuid = models.CharField(unique=True, max_length=38, default=uuid.uuid4)

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
    uuid = models.CharField(unique=True, max_length=38, default=uuid.uuid4)

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
    uuid = models.CharField(unique=True, max_length=38, default=uuid.uuid4)

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
    uuid = models.CharField(unique=True, max_length=38, default=uuid.uuid4)
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
    uuid = models.CharField(unique=True, max_length=38, default=uuid.uuid4)
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
    uuid = models.CharField(unique=True, max_length=38, default=uuid.uuid4)

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
    uuid = models.CharField(unique=True, max_length=38, default=uuid.uuid4)

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
    uuid = models.CharField(unique=True, max_length=38, default=uuid.uuid4)
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
    uuid = models.CharField(unique=True, max_length=38, default=uuid.uuid4)

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
    uuid = models.CharField(unique=True, max_length=38, default=uuid.uuid4)

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
    uuid = models.CharField(unique=True, max_length=38, default=uuid.uuid4)

    class Meta:
        # managed = False
        db_table = 'concept_set'


class ConceptStateConversion(models.Model):
    concept_state_conversion_id = models.AutoField(primary_key=True)
    concept = models.ForeignKey(Concept, models.DO_NOTHING, blank=True, null=True)
    program_workflow = models.ForeignKey('ProgramWorkflow', models.DO_NOTHING, blank=True, null=True)
    program_workflow_state = models.ForeignKey('ProgramWorkflowState', models.DO_NOTHING, blank=True, null=True)
    uuid = models.CharField(unique=True, max_length=38, default=uuid.uuid4)

    class Meta:
        # managed = False
        db_table = 'concept_state_conversion'
        unique_together = (('program_workflow', 'concept'),)


class ConceptStopWord(models.Model):
    concept_stop_word_id = models.AutoField(primary_key=True)
    word = models.CharField(max_length=50)
    locale = models.CharField(max_length=50, blank=True, null=True)
    uuid = models.CharField(max_length=38, default=uuid.uuid4)

    class Meta:
        # managed = False
        db_table = 'concept_stop_word'
        unique_together = (('word', 'locale'),)

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
    uuid = models.CharField(unique=True, max_length=38, default=uuid.uuid4)
    strength = models.CharField(max_length=255, blank=True, null=True)
    dose_limit_units = models.ForeignKey(Concept, models.DO_NOTHING, db_column='dose_limit_units', related_name='drug_dose_limit_units_set', blank=True, null=True)

    class Meta:
        # managed = False
        db_table = 'drug'


class DrugIngredient(models.Model):
    drug = models.OneToOneField(Drug, models.DO_NOTHING, primary_key=True)  # The composite primary key (drug_id, ingredient_id) found, that is not supported. The first column is selected.
    ingredient = models.ForeignKey(Concept, models.DO_NOTHING)
    uuid = models.CharField(unique=True, max_length=38, default=uuid.uuid4)
    strength = models.FloatField(blank=True, null=True)
    units = models.ForeignKey(Concept, models.DO_NOTHING, db_column='units', related_name='drugingredient_units_set', blank=True, null=True)

    class Meta:
        # managed = False
        db_table = 'drug_ingredient'
        unique_together = (('drug', 'ingredient'),)