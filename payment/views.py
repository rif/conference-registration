# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.contrib.auth.decorators import user_passes_test
from django.template import RequestContext
from django.http import HttpResponse
from django.core.mail import EmailMessage
from payment.models import PaymentPackage
from datetime import datetime

def __is_early():
    early_end = datetime(2011, 8, 17)
    return datetime.now() < early_end


@user_passes_test(lambda u: u.is_authenticated() and not u.is_staff)
def shop(request):
    user = request.user
    category = user.status.get_payment_cathegory()
    is_early = __is_early()
    print is_early
    package = PaymentPackage.objects.get(code=category, early=is_early)
    return render_to_response('payment/shop.html', {
        'pacakge': package,
        'is_early': is_early,
    }, context_instance=RequestContext(request))

@user_passes_test(lambda u: u.is_authenticated() and not u.is_staff)
def paypal(request):
    user = request.user
    paypal_list = []
    for item in __get_items(user):
        for count in range(item[1]):
            paypal_list.append([item[0], item[2]])
    return render_to_response('payment/paypal.html', {
        'items': paypal_list,
    }, context_instance=RequestContext(request))

@user_passes_test(lambda u: u.is_authenticated() and not u.is_staff)
def get_part_sum(request, item):
    sc = request.user.shoppingcart
    return HttpResponse(sc.get_part_sum(item))

@user_passes_test(lambda u: u.is_authenticated() and not u.is_staff)
def get_tot_sum(request):
    sc = request.user.shoppingcart
    return HttpResponse(sc.get_tot_sum())
@user_passes_test(lambda u: u.is_authenticated() and not u.is_staff)
def email(request):
    user = request.user
    category = user.status.get_payment_cathegory()
    is_early = __is_early()
    package = PaymentPackage.objects.get(code=category, early=is_early)
    email_body = render_to_response('payment/email.txt',
                    {'pacakge': package,
                    'user': user})
    email_body = str(email_body).split("\n")
    email_body = "\n".join(email_body[1:])
    email = EmailMessage(' [CRiSIS2011] Payment details', email_body, 'marius@cs.upt.ro',
            [user.about.email], ['marius@cs.upt.ro'],
            headers = {'Reply-To': 'marius@cs.upt.ro'})
    email.send(fail_silently=False)
    return HttpResponse("Mail sent succesfuly to %s!" % user.about.email)

@user_passes_test(lambda u: u.is_staff)
def receipts(request):
    scs = ShoppingCart.objects.all()
    return render_to_response('payment/receipts.html', {
        'shoppingcarts': scs,
    }, context_instance=RequestContext(request))
