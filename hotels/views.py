# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response, redirect
from django.contrib.auth.decorators import user_passes_test
from django.template import RequestContext
from django.http import HttpResponse
from django.core.mail import EmailMessage
from hotels.models import Hotel, Reservation, Cancellation
from hotels.forms import ReservationForm

@user_passes_test(lambda u: u.is_authenticated() and not u.is_staff)
def reservation(request):
    hotels = Hotel.objects.all()
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            new_res = form.save(commit=False)
            new_res.user = request.user
            new_res.save()
            __modify_room_number(new_res, -new_res.number_of_rooms)
            email(request)
            return redirect('userprofile:home')
    else:
        u = request.user
        r = Reservation(arrival_date=u.accomodation.arrival_date, departure_date=u.accomodation.departure_date)
        form = ReservationForm(instance=r)

    return render_to_response('hotels/reservation.html', {
        'hotels': hotels,
        'form': form,
    }, context_instance=RequestContext(request))


@user_passes_test(lambda u: u.is_authenticated() and not u.is_staff)
def cancel(request):
    try:
        old_res = request.user.reservation
    except:
        old_res = False
    if old_res:
        __modify_room_number(old_res, old_res.number_of_rooms)
        if old_res.processed:
            c = Cancellation(hotel=old_res.hotel, message=old_res.cancellation_message())
            c.save()
        hotel = old_res.hotel
        old_res.delete()
        user = request.user
        email_body = "The reservation at %s for %s was canceled!\nYou can create another hotel reservation at http://icsm2010.upt.ro/registration" % (hotel, user.get_full_name())
        email = EmailMessage(' [ICSM2010] Hotel details', email_body, 'info@icsm2010.upt.ro',
            [user.about.email], ['info@icsm2010.upt.ro'],
            headers = {'Reply-To': 'info@icsm2010.upt.ro'})
        email.send(fail_silently=False)
    return redirect('userprofile:home')

def __modify_room_number(res, nr):
    hotel = res.hotel
    room_kind = res.room_kind
    if room_kind == 'SG':
        hotel.single_rooms += nr
    if room_kind == 'DL':
        hotel.double_rooms += nr
    hotel.save()

@user_passes_test(lambda u: u.is_authenticated() and not u.is_staff)
def email(request):
    user = request.user
    email_body = render_to_response('hotels/email.txt', {'res': user.reservation})
    email_body = str(email_body).split("\n")
    email_body = "\n".join(email_body[1:])
    email = EmailMessage(' [ICSM2010] Hotel details', email_body, 'info@icsm2010.upt.ro',
            [user.about.email], ['info@icsm2010.upt.ro'],
            headers = {'Reply-To': 'info@icsm2010.upt.ro'})
    email.send(fail_silently=False)
    return HttpResponse("Mail sent succesfuly to %s!" % user.about.email)

