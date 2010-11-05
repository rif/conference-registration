from django.shortcuts import render_to_response, redirect
from django.contrib.auth.decorators import user_passes_test
from django.template import RequestContext
#from iphoneids.models import IphoneId
from iphoneids.forms import IphoneIdForm

@user_passes_test(lambda u: u.is_authenticated() and not u.is_staff)
def create(request):
    if request.method == 'POST':
        form = IphoneIdForm(request.POST)
        if form.is_valid():
            new_device = form.save(commit=False)
            new_device.user = request.user
            new_device.save()
            return redirect('userprofile:home')
    else:
        form = IphoneIdForm()

    return render_to_response('iphoneids/iphoneid_form.html', {
        'form': form,
    }, context_instance=RequestContext(request))