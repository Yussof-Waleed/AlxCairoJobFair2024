from django.db import models
import uuid

# Create your models here.
class Attendee(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    email = models.CharField(max_length=255, unique=True)
    phone_number = models.CharField(max_length=20)
    name = models.CharField(max_length=255)
    location = models.TextField()
    linkedin = models.TextField()
    age = models.PositiveBigIntegerField()
    track = models.CharField(max_length=255)
    # job_interest = models.CharField(max_length=255)
    cv_url = models.TextField()
    visits = models.IntegerField(default=0)

    def __str__(self) :
        return f"{self.email} graduated from {self.track} "
    
class Recrutier(models.Model):
    # email = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    rep_name = models.CharField(max_length=255)
    job_title  = models.CharField(max_length=255)
    # days = models.IntegerField()
    # members = models.IntegerField()
    code = models.IntegerField(unique=True)
    scanned_counts = models.IntegerField(default=0)
    
    def __str__(self) :
        return f"{self.name}"
    
class ScanLog(models.Model):
    recrutier = models.ForeignKey(Recrutier, on_delete=models.CASCADE, related_name="scanned_logs")
    attendee = models.ForeignKey(Attendee, on_delete=models.CASCADE)
    comment = models.TextField()

    def __str__(self):
        return f"{self.recrutier.name} scanned {self.attendee.name}"
