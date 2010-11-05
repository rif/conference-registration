# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.contrib.auth.decorators import user_passes_test
from django.template import RequestContext
from django.http import HttpResponse
from django.core.mail import EmailMessage
from payment.models import PaymentPackage, ShoppingCart

@user_passes_test(lambda u: u.is_authenticated() and not u.is_staff)
def shop(request):
    user = request.user
    category = user.status.get_payment_cathegory()
    package = PaymentPackage.objects.get(code=category)
    sc = user.shoppingcart
    return render_to_response('payment/shop.html', {
        'sc_items': (['ICSM<br><span class="note">September 13-17</span>', sc.get_item_price('sc01'), 'sc01', 'http://icsm2010.upt.ro/'],
                ['PROMISE<br><span class="note">September 12-13</span>', sc.get_item_price('sc02'), 'sc02', 'http://promisedata.org/'],
                ['SCAM<br><span class="note">September 12-13</span>', sc.get_item_price('sc03'), 'sc03', 'http://www2010.ieee-scam.org/'],
                ['WSE<br><span class="note">September 17-18</span>', sc.get_item_price('sc04'), 'sc04', 'http://www.rcost.unisannio.it/wse2010/'],
                ['Tutorial - Refactoring for Parallelism<br><span class="note">September 17 (Friday 2:00-5:30)</span>', sc.get_item_price('sc05'), 'sc05', 'http://icsm2010.upt.ro/program/tutorials/dig'],
                ['Tutorial - Migrating Software Testing to the Cloud<br><span class="note">September 13 (Monday 9:00-12:30)</span>', sc.get_item_price('sc06'), 'sc06', 'http://icsm2010.upt.ro/program/tutorials/tilleyparveen'],
                ['Tutorial - Teaching Undergraduate Software Engineering<br><span class="note">September 13 (Monday 2:00-5:30)</span>', sc.get_item_price('sc07'), 'sc07', 'http://icsm2010.upt.ro/program/tutorials/rajlich'],
                ['Tutorial - The Licensing Challenge<br><span class="note">September 13 (Monday 9:00-12:30)</span>', sc.get_item_price('sc08'), 'sc08', 'http://icsm2010.upt.ro/program/tutorials/german'],
                ['Extra - ICSM Banquet', sc.get_item_price('sc09'), 'sc09', 'http://icsm2010.upt.ro/program/socialevents'],
                ['Extra - ICSM Reception', sc.get_item_price('sc10'), 'sc10', 'http://icsm2010.upt.ro/program/socialevents'],
                ['Extra - ICSM Winetasting', sc.get_item_price('sc11'), 'sc11', 'http://icsm2010.upt.ro/program/socialevents'],
                ['Extra - ICSM Proceedings', sc.get_item_price('sc12'), 'sc12', 'http://icsm2010.upt.ro/home'],
                ['Extra - PROMISE/SCAM Dinner', sc.get_item_price('sc13'), 'sc13', 'http://icsm2010.upt.ro/program/socialevents'],
                ['Extra - PROMISE Proceedings', sc.get_item_price('sc14'), 'sc14', 'http://icsm2010.upt.ro/program/colocated'],
                ['Extra - SCAM Proceedings', sc.get_item_price('sc15'), 'sc15', 'http://icsm2010.upt.ro/program/colocated'],
                ['Extra - WSE Dinner', sc.get_item_price('sc16'), 'sc16', 'http://icsm2010.upt.ro/program/socialevents'],
                ['Extra - WSE Proceedings', sc.get_item_price('sc17'), 'sc17', 'http://icsm2010.upt.ro/program/colocated'],
                ['FAMOOSR<br><span class="note">September 17</span>', sc.get_item_price('sc18'), 'sc18', 'http://www.moosetechnology.org/events/famoosr2010'],
                ['MESOA<br><span class="note">September 17</span>', sc.get_item_price('sc19'), 'sc19', 'http://www.sei.cmu.edu/workshops/mesoa/2010/'],

        ),
        'pacakge': package,
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

def __get_items(user):
    sc = user.shoppingcart
    return (['ICSM', sc.get_item_count('sc01'), sc.get_item_price('sc01')],
                ['PROMISE', sc.get_item_count('sc02'), sc.get_item_price('sc02')],
                ['SCAM', sc.get_item_count('sc03'), sc.get_item_price('sc03')],
                ['WSE', sc.get_item_count('sc04'), sc.get_item_price('sc04')],
                ['Tutorial - Refactoring for Parallelism', sc.get_item_count('sc05'), sc.get_item_price('sc05')],
                ['Tutorial - Migrating Software Testing to the Cloud', sc.get_item_count('sc06'), sc.get_item_price('sc06')],
                ['Tutorial - Teaching Undergraduate Software Engineering', sc.get_item_count('sc07'), sc.get_item_price('sc07')],
                ['Tutorial - The Licensing Challenge', sc.get_item_count('sc08'), sc.get_item_price('sc08')],
                ['Extra - ICSM Banquet', sc.get_item_count('sc09'), sc.get_item_price('sc09')],
                ['Extra - ICSM Reception', sc.get_item_count('sc10'), sc.get_item_price('sc10')],
                ['Extra - ICSM Winetasting', sc.get_item_count('sc11'), sc.get_item_price('sc11')],
                ['Extra - ICSM Proceedings', sc.get_item_count('sc12'), sc.get_item_price('sc12')],
                ['Extra - PROMISE/SCAM Dinner', sc.get_item_count('sc13'), sc.get_item_price('sc13')],
                ['Extra - PROMISE Proceedings', sc.get_item_count('sc14'), sc.get_item_price('sc14')],
                ['Extra - SCAM Proceedings', sc.get_item_count('sc15'), sc.get_item_price('sc15')],
                ['Extra - WSE Dinner', sc.get_item_count('sc16'), sc.get_item_price('sc16')],
                ['Extra - WSE Proceedings', sc.get_item_count('sc17'), sc.get_item_price('sc17')],
    )

@user_passes_test(lambda u: u.is_authenticated() and not u.is_staff)
def modify(request):
    sc = request.user.shoppingcart
    if request.method == 'POST':
        item = request.POST['item']
        value = int(request.POST['value'])
        if item == "sc01":
            sc.ICSM += value
            if sc.ICSM < 0 or sc.ICSM > 1:
                sc.ICSM -= value
        if item == "sc02":
            sc.PROMISE += value
            if sc.PROMISE < 0 or sc.PROMISE > 1:
                sc.PROMISE -= value
        if item == "sc03":
            sc.SCAM += value
            if sc.SCAM < 0 or sc.SCAM > 1:
                sc.SCAM -= value
        if item == "sc04":
            sc.WSE += value
            if sc.WSE < 0 or sc.WSE > 1:
                sc.WSE -= value
        if item == "sc05":
            sc.tutorial_refactoring_for_parallelism += value
            if sc.tutorial_refactoring_for_parallelism < 0 or sc.tutorial_refactoring_for_parallelism > 10:
                sc.tutorial_refactoring_for_parallelism -= value
        if item == "sc06":
            sc.tutorial_migrating_software_testing_to_the_cloud += value
            if sc.tutorial_migrating_software_testing_to_the_cloud < 0 or sc.tutorial_migrating_software_testing_to_the_cloud > 10:
                sc.tutorial_migrating_software_testing_to_the_cloud -= value
        if item == "sc07":
            sc.tutorial_teaching_undergraduate_software_engineering += value
            if sc.tutorial_teaching_undergraduate_software_engineering < 0 or sc.tutorial_teaching_undergraduate_software_engineering > 10:
                sc.tutorial_teaching_undergraduate_software_engineering -= value
        if item == "sc08":
            sc.tutorial_the_licensing_challenge += value
            if sc.tutorial_the_licensing_challenge < 0 or sc.tutorial_the_licensing_challenge > 10:
                sc.tutorial_the_licensing_challenge -= value
        if item == "sc09":
            sc.extra_ICSM_banquet += value
            if sc.extra_ICSM_banquet < 0 or sc.extra_ICSM_banquet > 10:
                sc.extra_ICSM_banquet -= value
        if item == "sc10":
            sc.extra_ICSM_reception += value
            if sc.extra_ICSM_reception < 0 or sc.extra_ICSM_reception > 10:
                sc.extra_ICSM_reception -= value
        if item == "sc11":
            sc.extra_ICSM_winetasting += value
            if sc.extra_ICSM_winetasting < 0 or sc.extra_ICSM_winetasting > 10:
                sc.extra_ICSM_winetasting -= value
        if item == "sc12":
            sc.extra_ICSM_proceedings += value
            if sc.extra_ICSM_proceedings < 0 or sc.extra_ICSM_proceedings > 10:
                sc.extra_ICSM_proceedings -= value
        if item == "sc13":
            sc.extra_PROMISE_SCAM_dinner += value
            if sc.extra_PROMISE_SCAM_dinner < 0 or sc.extra_PROMISE_SCAM_dinner > 10:
                sc.extra_PROMISE_SCAM_dinner -= value
        if item == "sc14":
            sc.extra_PROMISE_proceedings += value
            if sc.extra_PROMISE_proceedings < 0 or sc.extra_PROMISE_proceedings > 10:
                sc.extra_PROMISE_proceedings -= value
        if item == "sc15":
            sc.extra_SCAM_proceedings += value
            if sc.extra_SCAM_proceedings < 0 or sc.extra_SCAM_proceedings > 10:
                sc.extra_SCAM_proceedings -= value
        if item == "sc16":
            sc.extra_WSE_dinner_price += value
            if sc.extra_WSE_dinner_price < 0 or sc.extra_WSE_dinner_price > 10:
                sc.extra_WSE_dinner_price -= value
        if item == "sc17":
            sc.extra_WSE_proceedings += value
            if sc.extra_WSE_proceedings < 0 or sc.extra_WSE_proceedings > 10:
                sc.extra_WSE_proceedings -= value
        if item == "sc18":
            sc.FAMOOSR += value
            if sc.FAMOOSR < 0 or sc.FAMOOSR > 1:
                sc.FAMOOSR -= value
        if item == "sc19":
            sc.MESOA += value
            if sc.MESOA < 0 or sc.MESOA > 1:
                sc.MESOA -= value
        sc.save()
    return HttpResponse(sc.get_item_count(item))

@user_passes_test(lambda u: u.is_authenticated() and not u.is_staff)
def get_item_count(request, item):
    try:
        sc = request.user.shoppingcart
    except:
        sc = ShoppingCart(user = request.user)
        sc.save()
    return HttpResponse(sc.get_item_count(item))

@user_passes_test(lambda u: u.is_authenticated() and not u.is_staff)
def get_part_sum(request, item):
    sc = request.user.shoppingcart
    return HttpResponse(sc.get_part_sum(item))

@user_passes_test(lambda u: u.is_authenticated() and not u.is_staff)
def get_tot_sum(request):
    sc = request.user.shoppingcart
    return HttpResponse(sc.get_tot_sum())

@user_passes_test(lambda u: u.is_authenticated() and not u.is_staff)
def set_have_paper(request):
    if request.method == 'POST':
        sc = request.user.shoppingcart
        item = request.POST['item']
        values = {'true': True, 'false': False}
        value = values[request.POST['value']]
        sc.set_have_paper(item, value)
    return HttpResponse(sc.get_item_price(item))

@user_passes_test(lambda u: u.is_authenticated() and not u.is_staff)
def get_have_paper(request, item):
    sc = request.user.shoppingcart
    return HttpResponse(sc.get_have_paper(item))

@user_passes_test(lambda u: u.is_authenticated() and not u.is_staff)
def get_paper_nb(request, item):
    sc = request.user.shoppingcart
    return HttpResponse(sc.get_paper_nb(item))

@user_passes_test(lambda u: u.is_authenticated() and not u.is_staff)
def set_paper_nb(request):
    if request.method == 'POST':
        sc = request.user.shoppingcart
        item = request.POST['item']
        value = request.POST['value']
        sc.set_paper_nb(item, value)
    return HttpResponse(sc.get_paper_nb(item))

@user_passes_test(lambda u: u.is_authenticated() and not u.is_staff)
def email(request):
    user = request.user
    category = user.status.get_payment_cathegory()
    package = PaymentPackage.objects.get(code=category)
    email_body = render_to_response('payment/email.txt',
                    {'pacakge': package,
                    'user': user,
                    'items': [item for item in __get_items(user) if item[1] > 0]})
    email_body = str(email_body).split("\n")
    email_body = "\n".join(email_body[1:])
    email = EmailMessage(' [ICSM2010] Payment details', email_body, 'info@icsm2010.upt.ro',
            [user.about.email], ['info@icsm2010.upt.ro'],
            headers = {'Reply-To': 'info@icsm2010.upt.ro'})
    email.send(fail_silently=False)
    return HttpResponse("Mail sent succesfuly to %s!" % user.about.email)

@user_passes_test(lambda u: u.is_staff)
def receipts(request):
    scs = ShoppingCart.objects.all()
    return render_to_response('payment/receipts.html', {
        'shoppingcarts': scs,
    }, context_instance=RequestContext(request))