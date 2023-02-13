from django.shortcuts import render

from .models import User, Friend, FriendNote

def friends(request):
    """View function for home page of site."""

    num_users = User.objects.count()
    # Generate counts of some of the main objects
    num_friends = Friend.objects.all().count()
    num_notes = FriendNote.objects.all().count()

    context = {
        'num_users': num_users,
        'num_friends': num_friends,
        'num_notes': num_notes,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'friends.html', context=context)

from django.views import generic

class FriendNoteListView(generic.ListView):
    model = FriendNote