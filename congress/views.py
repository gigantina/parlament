from pyexpat import model
from tempfile import template
from django.forms import fields
from django.shortcuts import render, reverse, HttpResponseRedirect
from allauth.socialaccount.models import SocialAccount
from .models import CustomUser
from .models import Meeting, Agenda, Voting, Vote
import utils.vk
from datetime import datetime
from django.contrib.auth.decorators import login_required
from utils.object import get_object_or_none, get_years
from utils.session import new_key
from congress.forms import VotingForm


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
            if request.session['form'] == request.POST['sessid']:
                year = request.POST['years']
    all_meetings = Meeting.objects.filter(date__year=year)
    current_meetung = Meeting.objects.latest('date')
    context['current_meeting'] = current_meetung
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
        votings = Voting.objects.filter(meeting=meeting)

        context['votings'] = votings
        context['agendas'] = all_agenda

    context['meeting'] = date.strftime('%d-%m-%Y')

    return render(request, 'meeting_detail.html', context=context)


@login_required
def voting_list(request):
    context = {}
    context['years'] = get_years()
    year = datetime.now().year
    print(request.session.session_key)
    if request.method == 'GET':
        if 'years' in request.GET:
            year = request.GET['years']
    all_meetings = Voting.objects.filter(date__year=year)
    current_votings = Voting.objects.filter(is_active=True)
    context['current_votings'] = current_votings
    context['all_votings'] = all_meetings
    print('all_votings')
    return render(request, 'voting_list.html', context=context)


@login_required
def voting_detail(request, title):
    context = {}
    form = None
    context['is_form'] = True
    voting = get_object_or_none(Voting, title=title)
    if voting:
        if request.method == 'POST':
            form = VotingForm(request.POST)
            if form.is_valid():
                result = form.cleaned_data.get('vote_choice')
                comment = form.cleaned_data.get('comment')

                if not get_object_or_none(Vote, voting=voting, user=request.user):
                    new_vote = Vote()
                    new_vote.voting = voting
                    new_vote.user = request.user
                    new_vote.status = result
                    if comment:
                        new_vote.comment = comment

                    new_vote.save()
                    return HttpResponseRedirect(reverse("voting_detail", args=[title]))
                else:
                    context['is_form'] = False
                    form = None
        else:
            form = VotingForm
            if get_object_or_none(Vote, voting=voting, user=request.user):
                form = None

        context['form'] = form

        true_votes = len(Vote.objects.filter(status='y'))
        false_votes = len(Vote.objects.filter(status='n'))
        neutral_votes = len(Vote.objects.filter(status='a'))

        context['true_votes'] = true_votes
        context['false_votes'] = false_votes
        context['neutral_votes'] = neutral_votes
        context['all_votes'] = true_votes + false_votes + neutral_votes

    context['voting'] = voting

    return render(request, 'voting_detail.html', context=context)
