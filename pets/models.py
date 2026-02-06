from django.db import models

class Dog(models.Model):
    STATUS_CHOICES = [
        ('available', 'Available'),
        ('adopted', 'Adopted'),
    ]
    name = models.CharField(max_length=100)
    breed = models.CharField(max_length=100)
    description = models.TextField()
    
    # NEW: This saves the file to a folder called 'dog_images'
    image = models.ImageField(upload_to='dog_images/') 
    
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='available')

    def __str__(self):
        return self.name

# NEW: This stores the applications
class AdoptionRequest(models.Model):
    dog = models.ForeignKey(Dog, on_delete=models.CASCADE) # Links to the specific dog
    name = models.CharField(max_length=100)                # Applicant's Name
    message = models.TextField()                           # Why they want the dog
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Request for {self.dog.name} by {self.name}"