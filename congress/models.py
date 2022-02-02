from django.contrib.auth.models import AbstractUser
from django.db import models
import uuid


class CustomUser(AbstractUser):
    is_congressman = models.BooleanField(default=False)


class Claim(models.Model):
    claim_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    title = models.CharField(blank=False, max_length=200)
    text = models.TextField(blank=False)
    photo = models.FileField(blank=True)
    date = models.DateField(auto_now=True)

    def __str__(self):
        return self.title


class Meeting(models.Model):
    meet_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    date = models.DateField(blank=False)

    def __str__(self):
        return self.date.strftime('%d-%m-%Y')


class Agenda(models.Model):
    agenda_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    meet = models.ForeignKey(Meeting, on_delete=models.CASCADE)
    text = models.TextField(blank=False)
    is_hidden = models.BooleanField(default=False)

    def __str__(self):
        return self.text


class Voting(models.Model):
    voting_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(blank=False, max_length=200)
    date = models.DateField(blank=False, auto_now_add=True)
    is_active = models.BooleanField(default=True)
    is_public = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class Variant(models.Model):
    variant_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(blank=False, max_length=200)

    def __str__(self):
        return self.title


class VariantsVoting(models.Model):
    varvot_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    variant = models.ForeignKey(Variant, on_delete=models.CASCADE)
    voting = models.ForeignKey(Voting, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.voting.title}-{self.variant.title}'


class Vote(models.Model):
    vote_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    variant = models.ForeignKey(VariantsVoting, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user.first_name} {self.variant.title}'
