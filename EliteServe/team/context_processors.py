from userprofile.models import Userprofile  # Adjust the import path according to your project structure
from team.models import Team

def active_team(request):
    if request.user.is_authenticated:
        try:
            user_profile = Userprofile.objects.get(user=request.user)
            active_team = user_profile.get_active_team()
            if active_team is None:
                # Handle case where there is no active team
                teams = Team.objects.filter(created_by=request.user)
                active_team = teams.first()  # Returns None if the queryset is empty
            return {'active_team': active_team}
        except Userprofile.DoesNotExist:
            return {'active_team': None}
    return {}
