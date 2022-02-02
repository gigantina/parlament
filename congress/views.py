from pyexpat import model
from tempfile import template
from django.forms import fields
from django.shortcuts import render
from allauth.socialaccount.models import SocialAccount
from .models import CustomUser
from .models import Meeting
import utils.vk
from datetime import datetime
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


def meeting_list(request):
    context = {}
    context['years'] = get_years()
    year = datetime.now().year
    if request.method == 'POST':
        year = request.POST['years']
    all_meetings = Meeting.objects.filter(date__year=year)
    context['all_meetings'] = all_meetings
    return render(request, 'meeting_list.html', context=context)


def meeting_detail(request, meet_id):
    meeting = get_object_or_none(Meeting, meet_id=meet_id)

