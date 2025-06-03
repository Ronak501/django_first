from django.db import models
from django.utils import timezone

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