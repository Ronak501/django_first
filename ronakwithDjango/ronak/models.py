from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class RonakVarity(models.Model):
      RONAK_TYPE_CHOICES = [
            ('ML', 'Type 1'),
            ('GR', 'Type 2'),
            ('KL', 'Type 3'),
            ('PL', 'Type 4'),
            ('EL', 'Type 5'),
      ]
      name = models.CharField(max_length=100)
      image = models.ImageField(upload_to='ronaks/')
      date_added = models.DateTimeField(default=timezone.now)
      type= models.CharField(max_length=2, choices=RONAK_TYPE_CHOICES, default='ML')
      description = models.TextField(blank=True, null=True)

      def __str__(self):
            return self.name

#one to many relationship
class RonakReview(models.Model):
      ronak = models.ForeignKey(RonakVarity, on_delete=models.CASCADE, related_name='reviews')
      user = models.ForeignKey(User ,on_delete=models.CASCADE)
      rating = models.IntegerField(default=1)
      comment = models.TextField(blank=True, null=True)
      date_added = models.DateTimeField(default=timezone.now)

      def __str__(self):
            return f"{self.user.username} Review For {self.ronak.name}"
      
#Many to many relationship
class Store(models.Model):
      name = models.CharField(max_length=100)
      location = models.CharField(max_length=255)
      ronaks = models.ManyToManyField(RonakVarity, related_name='stores')

      def __str__(self):
            return self.name
      
#one to one relationship
class RonakCertificate(models.Model):
      ronak = models.OneToOneField(RonakVarity, on_delete=models.CASCADE, related_name='certificate')
      issued_date = models.DateTimeField(default=timezone.now)
      valid_until = models.DateTimeField()

      def __str__(self):
            return f"Certificate for {self.ronak.name}"