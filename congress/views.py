from pyexpat import model
from tempfile import template
from django.forms import fields
from django.shortcuts import render
from allauth.socialaccount.models import SocialAccount
from .models import CustomUser
from .models import Meeting, Agenda
import utils.vk
from datetime import datetime
from django.contrib.auth.decorators import login_required
from utils.object import get_object_or_none, get_years


def index(request):
    context = {}
    print(utils.vk.isMember(request.user.id))
    vk_id = None
    if get_object_or_none(SocialAccount, user_id=request.user.id):
        vk_id = SocialAccount.objects.get(user_id=request.user.id).uid

    context['membership'] = False
    context['vk'] = vk_id
    if request.user.is_authenticated:
        if utils.vk.isMember(vk_id) or request.user.is_superuser:
            context['membership'] = True
    if request.user.is_authenticated:
        if request.user.is_congressman:
            return render(
                request, 'congressman.html', context=context)

    return render(request, 'user.html', context=context)


@login_required
def meeting_list(request):
    context = {}
    context['years'] = get_years()
    year = datetime.now().year
    if request.method == 'POST':
        if 'years' in request.POST:
            year = request.POST['years']
    all_meetings = Meeting.objects.filter(date__year=year)
    context['all_meetings'] = all_meetings
    return render(request, 'meeting_list.html', context=context)


@login_required
def meeting_detail(request, date):
    print(date)
    date = datetime.strptime(date, '%Y-%m-%d')
    context = {}
    meeting = get_object_or_none(Meeting, date=date)
    if meeting:
        all_agenda = Agenda.objects.filter(meet=meeting)
        print(all_agenda)
        context['agendas'] = all_agenda
        print(context['agendas'])
    print(meeting)
    context['meeting'] = date.strftime('%d-%m-%Y')

    return render(request, 'meeting_detail.html', context=context)

