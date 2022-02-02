from django.contrib import admin
from .models import CustomUser
from .models import Claim
from .models import Meeting, Agenda
from .models import Voting, Vote, Variant, VariantsVoting


admin.site.register(CustomUser)
admin.site.register(Claim)
admin.site.register(Meeting)
admin.site.register(Agenda)
admin.site.register(Voting)
admin.site.register(Vote)
admin.site.register(Variant)
admin.site.register(VariantsVoting)


