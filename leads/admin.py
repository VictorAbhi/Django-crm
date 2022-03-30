from django.contrib import admin
from leads.models import Agent, Lead, User

admin.site.register(
    [
        Agent,
        Lead,
        User
    ]
)


