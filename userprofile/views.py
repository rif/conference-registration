# -*- coding: utf-8 -*-
from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import get_object_or_404
from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from django.views.generic.list_detail import object_list, object_detail
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.core.mail import EmailMessage
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from userprofile.models import About, Accomodation, Status
from userprofile.forms import AboutForm, AccomodationForm, StatusForm, NamesForm


@user_passes_test(lambda u: u.is_staff)
def restricted_object_detail(*args, **kwargs):
    return object_detail(*args, **kwargs)

@user_passes_test(lambda u: u.is_staff)
def restricted_object_list(*args, **kwargs):
    return object_list(*args, **kwargs)

@user_passes_test(lambda u: u.is_authenticated() and not u.is_staff)
def home(request):
    return render_to_response('userprofile/home.html',
    {'object': request.user}, context_instance=RequestContext(request))

def register(request):
    if request.user.is_authenticated():
        return HttpResponse("You ar allready registered. Please user Edit an existing profile")
    if request.method == 'POST':
        usercreationform = UserCreationForm(request.POST)
        aboutform = AboutForm(request.POST)
        accomodationform = AccomodationForm(request.POST)
        statusform = StatusForm(request.POST)
        if usercreationform.is_valid() and aboutform.is_valid() and accomodationform.is_valid() and statusform.is_valid():
            nu = usercreationform.save(commit=False)
            nu.first_name = aboutform.cleaned_data['first_name']
            nu.email = aboutform.cleaned_data['email']
            nu.last_name = aboutform.cleaned_data['last_name']
            nu.save()
            # create shopping cart
            sc = ShoppingCart(user = nu)
            sc.save()
            na = aboutform.save(commit=False)
            na.user = nu
            na.save()
            nacc = accomodationform.save(commit=False)
            nacc.user = nu
            nacc.save()
            ns = statusform.save(commit=False)
            ns.user = nu
            ns.save()
            #login the created user (must call authenticate first)
            username = usercreationform.cleaned_data['username']
            password = usercreationform.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            __send_welcome_email(request, password)
            return redirect('userprofile:home')
    else:
        usercreationform = UserCreationForm()
        aboutform = AboutForm()
        accomodationform = AccomodationForm()
        statusform = StatusForm()

    return render_to_response('userprofile/register_forms.html', {
        'usercreationform': usercreationform,
        'aboutform': aboutform,
        'accomodationform': accomodationform,
        'statusform': statusform,
    }, context_instance=RequestContext(request))

def __send_welcome_email(request, password):
    user = request.user
    email_body = render_to_response('userprofile/welcome_email.txt', {
        'object': user,
        'password': password
    })
    email_body = str(email_body).split("\n")
    email_body = "\n".join(email_body[1:])
    email = EmailMessage('Welcome to ICSM 2010', email_body, 'info@icsm2010.upt.ro',
            [user.about.email], ['info@icsm2010.upt.ro'],
            headers = {'Reply-To': 'info@icsm2010.upt.ro'})
    email.send(fail_silently=False)

def __send_update_email(request):
    user = request.user
    email_body = render_to_response('userprofile/update_email.txt', {
        'object': user,
    })
    email_body = str(email_body).split("\n")
    email_body = "\n".join(email_body[1:])
    email = EmailMessage('[ICSM 2010] Profile Update', email_body, 'info@icsm2010.upt.ro',
            [user.about.email], ['info@icsm2010.upt.ro'],
            headers = {'Reply-To': 'info@icsm2010.upt.ro'})
    email.send(fail_silently=False)

@user_passes_test(lambda u: u.is_authenticated() and not u.is_staff)
def edit(request):
    about = get_object_or_404(About, user=request.user)
    accomodation = get_object_or_404(Accomodation, user=request.user)
    status= get_object_or_404(Status, user=request.user)
    if request.method == 'POST':
        aboutform = AboutForm(request.POST, instance=about)
        accomodationform = AccomodationForm(request.POST, instance=accomodation)
        statusform = StatusForm(request.POST, instance=status)
        if aboutform.is_valid() and accomodationform.is_valid() and statusform.is_valid():
            aboutform.save()
            accomodationform.save()
            statusform.save()
            # update user too
            user = request.user
            user.first_name = aboutform.cleaned_data['first_name']
            user.email = aboutform.cleaned_data['email']
            user.last_name = aboutform.cleaned_data['last_name']
            user.save()
            __send_update_email(request)
            return redirect('userprofile:home')
    else:
        aboutform = AboutForm(instance=about)
        accomodationform = AccomodationForm(instance=accomodation)
        statusform = StatusForm(instance=status)

    return render_to_response('userprofile/register_forms.html', {
        'aboutform': aboutform,
        'accomodationform': accomodationform,
        'statusform': statusform,
    }, context_instance=RequestContext(request))

@user_passes_test(lambda u: u.is_authenticated() and not u.is_staff)
def cancel_everything(request):
    user = request.user
    try:
        old_res = request.user.reservation
        """Only create a cancellation if the hotel registration was processed"""
        if old_res.processed:
            from hotels.views import cancel
            cancel(request)
    except:
        pass
    user.about.delete()
    user.accomodation.delete()
    user.status.delete()
    user.shoppingcart.delete()
    logout(request)
    user.delete()
    return HttpResponse("We are sorry to see you go...")

@user_passes_test(lambda u: u.is_staff)
def statistics(request):
    scs = ShoppingCart.objects.all()
    if request.method == 'POST':
        form = StatisticsForm(request.POST)
        if form.is_valid():
            clean_data = form.cleaned_data
            if clean_data['icsm']:
                scs = scs.filter(ICSM__gte=1)
            if clean_data['promise']:
                scs = scs.filter(PROMISE__gte=1)
            if clean_data['wse']:
                scs = scs.filter(WSE__gte=1)
            if clean_data['scam']:
                scs = scs.filter(SCAM__gte=1)
            if clean_data['famoosr']:
                scs = scs.filter(FAMOOSR__gte=1)
            if clean_data['mesoa']:
                scs = scs.filter(MESOA__gte=1)
            if clean_data['tut1']:
                scs = scs.filter(tutorial_refactoring_for_parallelism__gte=1)
            if clean_data['tut2']:
                scs = scs.filter(tutorial_migrating_software_testing_to_the_cloud__gte=1)
            if clean_data['tut3']:
                scs = scs.filter(tutorial_teaching_undergraduate_software_engineering__gte=1)
            if clean_data['tut4']:
                scs = scs.filter(tutorial_the_licensing_challenge__gte=1)
            if clean_data['extra_ICSM_banquet']:
                scs = scs.filter(extra_ICSM_banquet__gte=1)
            if clean_data['extra_ICSM_reception']:
                scs = scs.filter(extra_ICSM_reception__gte=1)
            if clean_data['extra_ICSM_winetasting']:
                scs = scs.filter(extra_ICSM_winetasting__gte=1)
            if clean_data['extra_ICSM_proceedings']:
                scs = scs.filter(extra_ICSM_proceedings__gte=1)
            if clean_data['extra_PROMISE_SCAM_dinner']:
                scs = scs.filter(extra_PROMISE_SCAM_dinner__gte=1)
            if clean_data['extra_PROMISE_proceedings']:
                scs = scs.filter(extra_PROMISE_proceedings__gte=1)
            if clean_data['extra_SCAM_proceedings']:
                scs = scs.filter(extra_SCAM_proceedings__gte=1)
            if clean_data['extra_WSE_dinner_price']:
                scs = scs.filter(extra_WSE_dinner_price__gte=1)
            if clean_data['extra_WSE_proceedings']:
                scs = scs.filter(extra_WSE_proceedings__gte=1)
    else:
        form = StatisticsForm()

    return render_to_response('userprofile/statistics.html', {
        'form': form,
        'shoppingcarts': scs,
    }, context_instance=RequestContext(request))

@user_passes_test(lambda u: u.is_staff)
def names(request):
  users = User.objects.exclude(is_staff=True)
  if request.method == 'POST':
    form = NamesForm(request.POST)
    if form.is_valid():
      clean_data = form.cleaned_data
      names_array = [name.strip() for name in clean_data['names'].split(',')]
      user_array = []
      for user in users:
        for name in names_array:
          if name.lower() in user.get_full_name().lower():
            user_array.append(user)
      users = user_array
  else:
    form = NamesForm()
  return render_to_response('userprofile/names.html', {
      'form': form,
      'users': users,
  }, context_instance=RequestContext(request))
