from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm,UserUpdateForm,ProfileUpdateForm
from  django.contrib import messages



# Create your views here.
def register(request):
    if request.method ==  'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Succefully Account Created for {username}. Please login')
            return redirect('login')
    
    else:
        form = UserRegisterForm()
    return render(request,'users/register.html', {'form':form})

@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance = request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance = request.user.profile)
        if u_form.is_valid and p_form.is_valid:
            p_form.save()
            u_form.save()
            messages.success(request, f'Succefully Account updated.')
            return redirect('profile') 
            # redirect other wise it will go to last line and send same data on same page
            #if we dont do that it we send another post request from last line 
            #and if we redirect here then it sends GET request
    else:
        u_form = UserUpdateForm(instance = request.user)
        p_form = ProfileUpdateForm(instance = request.user.profile)

    context = {
        'u_form' : u_form,
        'p_form' : p_form
    }
    return render(request,'users/profile.html',context)