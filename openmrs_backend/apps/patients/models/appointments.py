from django.db import models
import uuid

# Create your models here.
class AppointmentService(models.Model):
    appointment_service_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True, null=True)
    start_time = models.TimeField(blank=True, null=True)
    end_time = models.TimeField(blank=True, null=True)
    location = models.ForeignKey('Location', models.DO_NOTHING, blank=True, null=True)
    speciality = models.ForeignKey('AppointmentSpeciality', models.DO_NOTHING, blank=True, null=True)
    max_appointments_limit = models.IntegerField(blank=True, null=True)
    duration_mins = models.IntegerField(blank=True, null=True)
    color = models.CharField(max_length=8, blank=True, null=True)
    date_created = models.DateTimeField()
    creator = models.IntegerField()
    date_changed = models.DateTimeField(blank=True, null=True)
    changed_by = models.IntegerField(blank=True, null=True)
    voided = models.IntegerField(blank=True, null=True)
    voided_by = models.IntegerField(blank=True, null=True)
    date_voided = models.DateTimeField(blank=True, null=True)
    void_reason = models.CharField(max_length=255, blank=True, null=True)
    uuid = models.CharField(unique=True, max_length=38, default=uuid.uuid4)
    initial_appointment_status = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        # managed = False
        db_table = 'appointment_service'


class AppointmentServiceType(models.Model):
    appointment_service_type_id = models.AutoField(primary_key=True)
    appointment_service = models.ForeignKey(AppointmentService, models.DO_NOTHING)
    name = models.CharField(max_length=50)
    duration_mins = models.IntegerField(blank=True, null=True)
    date_created = models.DateTimeField()
    creator = models.IntegerField()
    date_changed = models.DateTimeField(blank=True, null=True)
    changed_by = models.IntegerField(blank=True, null=True)
    voided = models.IntegerField(blank=True, null=True)
    voided_by = models.IntegerField(blank=True, null=True)
    date_voided = models.DateTimeField(blank=True, null=True)
    void_reason = models.CharField(max_length=255, blank=True, null=True)
    uuid = models.CharField(unique=True, max_length=38, default=uuid.uuid4)

    class Meta:
        # managed = False
        db_table = 'appointment_service_type'


class AppointmentServiceWeeklyAvailability(models.Model):
    service_weekly_availability_id = models.AutoField(primary_key=True)
    service = models.ForeignKey(AppointmentService, models.DO_NOTHING)
    day_of_week = models.CharField(max_length=45)
    start_time = models.TimeField(blank=True, null=True)
    end_time = models.TimeField(blank=True, null=True)
    max_appointments_limit = models.IntegerField(blank=True, null=True)
    uuid = models.CharField(unique=True, max_length=38, default=uuid.uuid4)
    voided = models.IntegerField(blank=True, null=True)
    voided_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='voided_by', blank=True, null=True)
    date_voided = models.DateTimeField(blank=True, null=True)
    void_reason = models.CharField(max_length=255, blank=True, null=True)
    date_created = models.DateTimeField()
    creator = models.ForeignKey('Users', models.DO_NOTHING, db_column='creator', related_name='appointmentserviceweeklyavailability_creator_set')
    date_changed = models.DateTimeField(blank=True, null=True)
    changed_by = models.IntegerField(blank=True, null=True)

    class Meta:
        # managed = False
        db_table = 'appointment_service_weekly_availability'


class AppointmentSpeciality(models.Model):
    speciality_id = models.AutoField(primary_key=True)
    name = models.CharField(unique=True, max_length=50)
    date_created = models.DateTimeField()
    creator = models.IntegerField()
    date_changed = models.DateTimeField(blank=True, null=True)
    changed_by = models.IntegerField(blank=True, null=True)
    uuid = models.CharField(unique=True, max_length=38, default=uuid.uuid4)
    voided = models.IntegerField(blank=True, null=True)

    class Meta:
        # managed = False
        db_table = 'appointment_speciality'

class PatientAppointment(models.Model):
    patient_appointment_id = models.AutoField(primary_key=True)
    provider = models.ForeignKey('users.Provider', models.DO_NOTHING, blank=True, null=True)
    appointment_number = models.CharField(max_length=50)
    patient = models.ForeignKey('Patient', models.DO_NOTHING)
    start_date_time = models.DateTimeField(blank=True, null=True)
    end_date_time = models.DateTimeField(blank=True, null=True)
    appointment_service = models.ForeignKey(AppointmentService, models.DO_NOTHING, blank=True, null=True)
    appointment_service_type = models.ForeignKey(AppointmentServiceType, models.DO_NOTHING, blank=True, null=True)
    status = models.CharField(max_length=45, db_comment='scheduled, checked in, started, completed, cancelled, missed')
    location = models.ForeignKey('Location', models.DO_NOTHING, blank=True, null=True)
    appointment_kind = models.CharField(max_length=45, db_comment='scheduled, walk in')
    comments = models.CharField(max_length=255, blank=True, null=True)
    uuid = models.CharField(unique=True, max_length=38, default=uuid.uuid4)
    date_created = models.DateTimeField()
    creator = models.IntegerField()
    date_changed = models.DateTimeField(blank=True, null=True)
    changed_by = models.IntegerField(blank=True, null=True)
    voided = models.IntegerField(blank=True, null=True)
    voided_by = models.IntegerField(blank=True, null=True)
    date_voided = models.DateTimeField(blank=True, null=True)
    void_reason = models.CharField(max_length=255, blank=True, null=True)
    related_appointment = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    tele_health_video_link = models.CharField(max_length=255, blank=True, null=True)
    priority = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        # managed = False
        db_table = 'patient_appointment'


class PatientAppointmentAudit(models.Model):
    patient_appointment_audit_id = models.AutoField(primary_key=True)
    appointment = models.ForeignKey(PatientAppointment, models.DO_NOTHING)
    uuid = models.CharField(unique=True, max_length=38, default=uuid.uuid4)
    date_created = models.DateTimeField()
    creator = models.IntegerField()
    date_changed = models.DateTimeField(blank=True, null=True)
    changed_by = models.IntegerField(blank=True, null=True)
    voided = models.IntegerField(blank=True, null=True)
    voided_by = models.IntegerField(blank=True, null=True)
    date_voided = models.DateTimeField(blank=True, null=True)
    void_reason = models.CharField(max_length=255, blank=True, null=True)
    status = models.CharField(max_length=45)
    notes = models.CharField(max_length=1000, blank=True, null=True)

    class Meta:
        # managed = False
        db_table = 'patient_appointment_audit'


class PatientAppointmentOccurrence(models.Model):
    patient_appointment_timings = models.ForeignKey('PatientAppointmentRecurringTime', models.DO_NOTHING, blank=True, null=True)
    patient_appointment = models.ForeignKey(PatientAppointment, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        # managed = False
        db_table = 'patient_appointment_occurrence'


class PatientAppointmentProvider(models.Model):
    patient_appointment_provider_id = models.AutoField(primary_key=True)
    patient_appointment = models.ForeignKey(PatientAppointment, models.DO_NOTHING)
    provider = models.ForeignKey('users.Provider', models.DO_NOTHING)
    response = models.CharField(max_length=32, blank=True, null=True)
    comments = models.CharField(max_length=1000, blank=True, null=True)
    date_created = models.DateTimeField()
    creator = models.IntegerField()
    date_changed = models.DateTimeField(blank=True, null=True)
    changed_by = models.IntegerField(blank=True, null=True)
    voided = models.IntegerField(blank=True, null=True)
    voided_by = models.IntegerField(blank=True, null=True)
    date_voided = models.DateTimeField(blank=True, null=True)
    void_reason = models.CharField(max_length=255, blank=True, null=True)
    uuid = models.CharField(unique=True, max_length=38, default=uuid.uuid4)

    class Meta:
        # managed = False
        db_table = 'patient_appointment_provider'


class PatientAppointmentRecurringTime(models.Model):
    patient_appointment_timings_id = models.AutoField(primary_key=True)
    recurrence_type = models.CharField(max_length=20)
    period = models.IntegerField()
    frequency = models.IntegerField(blank=True, null=True)
    end_date = models.DateTimeField(blank=True, null=True)
    days_of_week = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        # managed = False
        db_table = 'patient_appointment_recurring_time'

