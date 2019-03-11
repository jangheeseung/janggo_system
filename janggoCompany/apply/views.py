from django.shortcuts import render, redirect
from django.utils import translation, timezone
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Hire, Apply
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.
def hire_list(request):
    hires = Hire.objects.filter(end_date__gte=timezone.now())
    applys = Apply.objects.all()
    paginator = Paginator(hires, 5) # Show 25 contacts per page
    page = request.GET.get('page')
    message = ""
    error = False

    if request.session.get('message', False):
        message = request.session['message']
        del request.session['message']
    if request.session.get('error', False):
        error = request.session['error']
        del request.session['error']

    try:
        contacts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        contacts = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        contacts = paginator.page(paginator.num_pages)
    
    context = {
        'contacts': contacts, 
        'site': "apply", 'message':message, 
        'error':error, 'hires':hires, 
        'apply_len':len(applys)
        }
    return render(request, 'apply/hire/hire_list.html', context)

def hire_create(request):
    if request.method == 'POST':
        kind = request.POST.get('kind')
        num = request.POST.get('num')
        hire_type = request.POST.get('hire_type')
        start_date = request.POST.get('start_date')
        end_date = request.POST.get('end_date')
        content1 = request.POST.get('content1')
        content2 = request.POST.get('content2')
        hire = Hire(
            kind = kind,
            num = num,
            hire_type = hire_type,
            start_date = start_date,
            end_date = end_date,
            content1 = content1,
            content2 = content2
            )
        hire.save()
        return redirect(reverse('hire_list'))
    hire = ''
    context = {'hire': hire, 'site': "apply"}
    return render(request, 'apply/hire/hire_form.html', context)

def hire_view(request, pk):
    hire = Hire.objects.get(pk = pk)
    context = {'hire': hire, 'site': "apply"}
    return render(request, 'apply/hire/hire_view.html', context)

def apply_create(request, pk):
    if request.method == 'POST':
        e_mail = request.POST.get('e_mail')
        if Apply.objects.filter(e_mail = e_mail).exists():
            request.session['error'] = False
            request.session['message'] = "이미 존재하는 이메일 입니다."
            return redirect(reverse('hire_list'))
        apply = Apply(
            name = request.POST.get('name'),
            age = request.POST.get('age'),
            phone = request.POST.get('phone'),
            e_mail = e_mail,
            address = request.POST.get('address'),
            college = request.POST.get('college'),
            major = request.POST.get('major'),
            graduate = request.POST.get('graduate'),
            document = request.FILES.get('document'),
            hire = Hire.objects.get(pk = pk),
            password = request.POST.get('password')
        )
        apply.save()
        return redirect(reverse('hire_list'))
    hire = Hire.objects.get(pk = pk)
    context = {'hire':hire, 'pk':pk}
    return render(request, 'apply/apply_form.html', context)

def apply_update(request):
    try:
        apply_pk = request.POST.get('apply_pk')
        hire_pk = request.POST.get('hire_pk')
        apply = Apply.objects.get(pk = apply_pk)
        apply.name = request.POST.get('name')
        apply.age = request.POST.get('age')
        apply.phone = request.POST.get('phone')
        apply.address = request.POST.get('address')
        apply.college = request.POST.get('college')
        apply.major = request.POST.get('major')
        apply.graduate = request.POST.get('graduate')
        apply.hire = Hire.objects.get(pk = hire_pk)
        apply.password = request.POST.get('password')
        apply.document.delete()
        apply.document = request.FILES.get('document')

        apply.save()
    except:
        request.session['error'] = True
        request.session['message'] = "업데이트에 실패하였습니다." 

    return redirect(reverse('hire_list'))

def check_apply(request):
    hires = Hire.objects.filter(end_date__gte=timezone.now())
    try:
        password = request.POST.get('password')
        e_mail = request.POST.get('e_mail')
        apply = Apply.objects.get(e_mail = e_mail)
        if apply.e_mail == str(e_mail):
            if apply.password == password or apply.password == str(password):
                message = "해당 신청서를 찾았습니다."
                error = False
                context = {'message':message, 'error':error, 'hire':apply.hire, 'pk':apply.hire.pk, 'apply':apply}
                return render(request, 'apply/apply_form.html', context)
            else:
                message = "Password가 일치하지 않습니다."
                error = True
        else:
            message = "해당 이메일로 신청 된 신청내역이 없습니다."
            error = True
    except:
        message = "잘못된 요청입니다."
        error = True

    request.session['error'] = error
    request.session['message'] = message
    return redirect(reverse('hire_list'))