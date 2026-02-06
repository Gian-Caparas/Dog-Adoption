from django.shortcuts import render, redirect, get_object_or_404
from .models import Dog, AdoptionRequest

# HOME PAGE: Only shows dogs that need a home
def home(request):
    # FILTER: status='available' means adopted dogs won't show here anymore
    available_dogs = Dog.objects.filter(status='available')
    return render(request, 'home.html', {'dogs': available_dogs})

# NEW PAGE: Only shows dogs that are already adopted
def success_stories(request):
    adopted_dogs = Dog.objects.filter(status='adopted')
    return render(request, 'adopted.html', {'dogs': adopted_dogs})

def adopt_dog(request, dog_id):
    dog = get_object_or_404(Dog, pk=dog_id)
    if request.method == 'POST':
        name = request.POST.get('applicant_name')
        msg = request.POST.get('message')
        AdoptionRequest.objects.create(dog=dog, name=name, message=msg)
        return redirect('home')
    return render(request, 'adopt_form.html', {'dog': dog})