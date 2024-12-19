from django.shortcuts import redirect
from .models import Contact
from django.contrib import messages
from listings.models import Listing

# Create your views here.

def contact(request):
    if request.method == "POST":
        listing_id = request.POST['listing_id']
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        user_id = request.POST['user_id']
        realtor_email = request.POST['realtor_email']
        
        contact = Contact(
            listing=Listing.objects.get(id=listing_id),
            name=name,
            email=email,
            phone=phone,
            message=message,
            user_id=user_id,
            realtor_email=realtor_email
        )

        contact.save()

        messages.success(request, 'Your inquiry has been submitted. A realtor will soon reach out to you.')

        return redirect('/listings/'+listing_id)