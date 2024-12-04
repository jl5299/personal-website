from django.db import models

# Create your models here.

from django.urls import reverse

class User(models.Model):
    name = models.CharField(max_length=30, help_text='User\'s name')

    def get_absolute_url(self):
        """Returns the URL to access a particular instance of MyModelName."""
        return reverse('user', args=[str(self.name)])

    class Meta:
        ordering = ['-name']

    def __str__(self):
        return self.name

class Friend(models.Model):
    """A friend."""

    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=20, help_text='Friend\'s name')

    class Meta:
        ordering = ['-name']

    def get_absolute_url(self):
        """Returns the URL to access a particular instance of MyModelName."""
        return reverse('friend', args=[str(self.name)])

    def __str__(self):
        """String for representing the MyModelName object (in Admin site etc.)."""
        return self.name

class FriendNote(models.Model):
    """A note on a friend."""

    content = models.CharField(max_length=10_000, help_text='The information for this note')
    friend = models.ForeignKey(Friend, on_delete=models.CASCADE)

    class Meta:
      pass

    def get_absolute_url(self):
        """Returns the URL to access a particular instance of MyModelName."""
        return reverse('friendnote', args=[str(self.friend), str(self.content)])

    def __str__(self):
        """String for representing the MyModelName object (in Admin site etc.)."""
        return str(self.friend) + ": " + self.content