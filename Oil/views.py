from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import ContactMessage
from .forms import ContactForm
from django.contrib.auth import authenticate, login

# ------------------- Contact Messages Management -------------------

def oil_list(request):
    oils = ContactMessage.objects.all()
    return render(request, 'oil_list.html', {'oils': oils})

# Order Page (Display Contact Messages)
def add_oil(request):
     return render(request, 'add_oil.html')

# About Us page
def about(request):
    return render(request, 'about.html')

# Contact Us Form Submission
def contact_us(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your message has been submitted successfully!")
            return redirect('/add')  # Redirect to Order Page
    else:
        form = ContactForm()
    return render(request, 'contact_us.html', {'form': form})

# Login Form Submission



def login(request):
    if request.method == 'POST':
        username = request.POST.get('contact')  # This can be email or phone
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, 'Login successful! Welcome back.')
            return redirect('home')  # Replace with your home page URL name
        else:
            messages.error(request, 'Invalid email/phone or password.')

    return render(request, 'login.html')


# Update Contact Message
def update_contact(request, id):
    message = get_object_or_404(ContactMessage, id=id)
    if request.method == "POST":
        form = ContactForm(request.POST, instance=message)
        if form.is_valid():
            form.save()
            messages.success(request, "Contact updated successfully!")
            return redirect('/add')
    else:
        form = ContactForm(instance=message)
    return render(request, 'update_contact.html', {'form': form, 'message': message})

# Delete Contact Message
def delete_contact(request, id):
    message = get_object_or_404(ContactMessage, id=id)
    message.delete()
    messages.success(request, "Contact deleted successfully!")
    return redirect('/add')
