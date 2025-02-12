from django.db import models
import uuid

# Order-related models
class OrderAttribute(models.Model):
    order_attribute_id = models.AutoField(primary_key=True)
    order = models.ForeignKey('Orders', models.DO_NOTHING)
    attribute_type = models.ForeignKey('OrderAttributeType', models.DO_NOTHING)
    value_reference = models.TextField()
    uuid = models.CharField(unique=True, max_length=38, default=uuid.uuid4)
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
    uuid = models.CharField(unique=True, max_length=38, default=uuid.uuid4)

    class Meta:
        # managed = False
        db_table = 'order_attribute_type'

class OrderFrequency(models.Model):
    order_frequency_id = models.AutoField(primary_key=True)
    concept = models.OneToOneField('Concept', models.DO_NOTHING)
    frequency_per_day = models.FloatField(blank=True, null=True)
    creator = models.ForeignKey('Users', models.DO_NOTHING, db_column='creator')
    date_created = models.DateTimeField()
    retired = models.IntegerField()
    retired_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='retired_by', related_name='orderfrequency_retired_by_set', blank=True, null=True)
    date_retired = models.DateTimeField(blank=True, null=True)
    retire_reason = models.CharField(max_length=255, blank=True, null=True)
    changed_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='changed_by', related_name='orderfrequency_changed_by_set', blank=True, null=True)
    date_changed = models.DateTimeField(blank=True, null=True)
    uuid = models.CharField(unique=True, max_length=38, default=uuid.uuid4)

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
    uuid = models.CharField(unique=True, max_length=38, default=uuid.uuid4)
    order_group_reason = models.ForeignKey('Concept', models.DO_NOTHING, db_column='order_group_reason', blank=True, null=True)
    parent_order_group = models.ForeignKey('self', models.DO_NOTHING, db_column='parent_order_group', blank=True, null=True)
    previous_order_group = models.ForeignKey('self', models.DO_NOTHING, db_column='previous_order_group', related_name='ordergroup_previous_order_group_set', blank=True, null=True)

    class Meta:
        # managed = False
        db_table = 'order_group'

class OrderGroupAttribute(models.Model):
    order_group_attribute_id = models.AutoField(primary_key=True)
    order_group = models.ForeignKey('OrderGroup', models.DO_NOTHING)
    attribute_type = models.ForeignKey('OrderGroupAttributeType', models.DO_NOTHING)
    value_reference = models.TextField()
    uuid = models.CharField(unique=True, max_length=38, default=uuid.uuid4)
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
    uuid = models.CharField(unique=True, max_length=38, default=uuid.uuid4)

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
    uuid = models.CharField(unique=True, max_length=38, default=uuid.uuid4)
    category = models.ForeignKey('Concept', models.DO_NOTHING, db_column='category', blank=True, null=True)

    class Meta:
        # managed = False
        db_table = 'order_set'


class OrderSetAttribute(models.Model):
    order_set_attribute_id = models.AutoField(primary_key=True)
    order_set = models.ForeignKey('OrderSet', models.DO_NOTHING)
    attribute_type = models.ForeignKey('OrderSetAttributeType', models.DO_NOTHING)
    value_reference = models.TextField()
    uuid = models.CharField(unique=True, max_length=38, default=uuid.uuid4)
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
    uuid = models.CharField(unique=True, max_length=38, default=uuid.uuid4)

    class Meta:
        # managed = False
        db_table = 'order_set_attribute_type'


class OrderSetMember(models.Model):
    order_set_member_id = models.AutoField(primary_key=True)
    order_type = models.ForeignKey('OrderType', models.DO_NOTHING, db_column='order_type')
    order_template = models.TextField(blank=True, null=True)
    order_template_type = models.CharField(max_length=1024, blank=True, null=True)
    order_set = models.ForeignKey('OrderSet', models.DO_NOTHING)
    sequence_number = models.IntegerField()
    concept = models.ForeignKey('Concept', models.DO_NOTHING)
    creator = models.ForeignKey('Users', models.DO_NOTHING, db_column='creator')
    date_created = models.DateTimeField()
    retired = models.IntegerField()
    retired_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='retired_by', related_name='ordersetmember_retired_by_set', blank=True, null=True)
    date_retired = models.DateTimeField(blank=True, null=True)
    retire_reason = models.CharField(max_length=255, blank=True, null=True)
    changed_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='changed_by', related_name='ordersetmember_changed_by_set', blank=True, null=True)
    date_changed = models.DateTimeField(blank=True, null=True)
    uuid = models.CharField(unique=True, max_length=38, default=uuid.uuid4)

    class Meta:
        # managed = False
        db_table = 'order_set_member'


class OrderTemplate(models.Model):
    order_template_id = models.AutoField(primary_key=True)
    uuid = models.CharField(unique=True, max_length=38, default=uuid.uuid4)
    name = models.CharField(unique=True, max_length=255)
    description = models.CharField(max_length=255)
    concept = models.ForeignKey('Concept', models.DO_NOTHING, db_column='concept')
    drug = models.ForeignKey('Drug', models.DO_NOTHING, db_column='drug', blank=True, null=True)
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
    uuid = models.CharField(unique=True, max_length=38, default=uuid.uuid4)
    java_class_name = models.CharField(max_length=255)
    parent = models.ForeignKey('self', models.DO_NOTHING, db_column='parent', blank=True, null=True)
    changed_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='changed_by', related_name='ordertype_changed_by_set', blank=True, null=True)
    date_changed = models.DateTimeField(blank=True, null=True)

    class Meta:
        # managed = False
        db_table = 'order_type'


class OrderTypeClassMap(models.Model):
    order_type = models.OneToOneField('OrderType', models.DO_NOTHING, primary_key=True)  # The composite primary key (order_type_id, concept_class_id) found, that is not supported. The first column is selected.
    concept_class = models.OneToOneField('ConceptClass', models.DO_NOTHING)

    class Meta:
        # managed = False
        db_table = 'order_type_class_map'
        unique_together = (('order_type', 'concept_class'),)


class Orders(models.Model):
    order_id = models.AutoField(primary_key=True)
    order_type = models.ForeignKey('OrderType', models.DO_NOTHING)
    concept_id = models.IntegerField()
    orderer = models.ForeignKey('Provider', models.DO_NOTHING, db_column='orderer')
    encounter = models.ForeignKey('Encounter', models.DO_NOTHING)
    instructions = models.TextField(blank=True, null=True)
    date_activated = models.DateTimeField(blank=True, null=True)
    auto_expire_date = models.DateTimeField(blank=True, null=True)
    date_stopped = models.DateTimeField(blank=True, null=True)
    order_reason = models.ForeignKey('Concept', models.DO_NOTHING, db_column='order_reason', blank=True, null=True)
    order_reason_non_coded = models.CharField(max_length=255, blank=True, null=True)
    creator = models.ForeignKey('Users', models.DO_NOTHING, db_column='creator')
    date_created = models.DateTimeField()
    voided = models.IntegerField()
    voided_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='voided_by', related_name='orders_voided_by_set', blank=True, null=True)
    date_voided = models.DateTimeField(blank=True, null=True)
    void_reason = models.CharField(max_length=255, blank=True, null=True)
    patient = models.ForeignKey('Patient', models.DO_NOTHING)
    accession_number = models.CharField(max_length=255, blank=True, null=True)
    uuid = models.CharField(unique=True, max_length=38, default=uuid.uuid4)
    urgency = models.CharField(max_length=50)
    order_number = models.CharField(max_length=50)
    previous_order = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    order_action = models.CharField(max_length=50)
    comment_to_fulfiller = models.CharField(max_length=1024, blank=True, null=True)
    care_setting = models.ForeignKey('CareSetting', models.DO_NOTHING, db_column='care_setting')
    scheduled_date = models.DateTimeField(blank=True, null=True)
    order_group = models.ForeignKey('OrderGroup', models.DO_NOTHING, blank=True, null=True)
    sort_weight = models.FloatField(blank=True, null=True)
    fulfiller_comment = models.CharField(max_length=1024, blank=True, null=True)
    fulfiller_status = models.CharField(max_length=50, blank=True, null=True)
    form_namespace_and_path = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        # managed = False
        db_table = 'orders'

class DrugOrder(models.Model):
    order = models.OneToOneField('Orders', models.DO_NOTHING, primary_key=True)
    drug_inventory = models.ForeignKey('Drug', models.DO_NOTHING, blank=True, null=True)
    dose = models.FloatField(blank=True, null=True)
    as_needed = models.IntegerField(blank=True, null=True)
    dosing_type = models.CharField(max_length=255, blank=True, null=True)
    quantity = models.FloatField(blank=True, null=True)
    as_needed_condition = models.CharField(max_length=255, blank=True, null=True)
    num_refills = models.IntegerField(blank=True, null=True)
    dosing_instructions = models.TextField(blank=True, null=True)
    duration = models.IntegerField(blank=True, null=True)
    duration_units = models.ForeignKey('Concept', models.DO_NOTHING, db_column='duration_units', blank=True, null=True)
    quantity_units = models.ForeignKey('Concept', models.DO_NOTHING, db_column='quantity_units', related_name='drugorder_quantity_units_set', blank=True, null=True)
    route = models.ForeignKey('Concept', models.DO_NOTHING, db_column='route', related_name='drugorder_route_set', blank=True, null=True)
    dose_units = models.ForeignKey('Concept', models.DO_NOTHING, db_column='dose_units', related_name='drugorder_dose_units_set', blank=True, null=True)
    frequency = models.ForeignKey('OrderFrequency', models.DO_NOTHING, db_column='frequency', blank=True, null=True)
    brand_name = models.CharField(max_length=255, blank=True, null=True)
    dispense_as_written = models.IntegerField()
    drug_non_coded = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        # managed = False
        db_table = 'drug_order'

