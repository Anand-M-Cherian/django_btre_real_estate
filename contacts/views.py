from django.shortcuts import redirect
from .models import Contact
from django.contrib import messages
from listings.models import Listing

# Create your views here.

def contact(request):
    if request.method == "POST":
        listing_id = request.POST['listing_id']
        listing = Listing.objects.get(id=listing_id)
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        user_id = request.POST['user_id']
        realtor_email = request.POST['realtor_email']

        # Check if user has already made an inquiry for the listing
        if request.user.is_authenticated:
            user_id = request.user.id
            has_contacted = Contact.objects.all().filter(listing_id=listing_id, user_id=user_id)
            if has_contacted:
                messages.error(request, 'You have already made an inquiry for the listing')
                return redirect('/listings/'+listing_id)
        
        contact = Contact(
            listing=listing,
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