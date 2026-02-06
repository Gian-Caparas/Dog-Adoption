from django.contrib import admin, messages
from .models import Dog, AdoptionRequest

@admin.register(Dog)
class DogAdmin(admin.ModelAdmin):
    list_display = ('name', 'breed', 'status') 

@admin.register(AdoptionRequest)
class AdoptionRequestAdmin(admin.ModelAdmin):
    list_display = ('name', 'dog', 'submitted_at')
    actions = ['approve_application'] 

    # INDENTATION FIX: This function is now INSIDE the class
    def approve_application(self, request, queryset):
        for application in queryset:
            dog = application.dog
            
            if dog.status == 'adopted':
                self.message_user(request, f"Error: {dog.name} is already adopted!", level=messages.ERROR)
                continue

            dog.status = 'adopted'
            dog.save()
            
            self.message_user(request, f"Adoption for {dog.name} is accepted.")

    approve_application.short_description = "Approve application (Mark dog as Adopted)"