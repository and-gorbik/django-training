from django.db import models
from django.contrib.auth import get_user_model
from django.shortcuts import reverse

from . import managers

class Profile(models.Model):
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE)
    avatar = models.ImageField(
        upload_to='likearound/profiles/',
        default='default.jpg',
        blank=True,
    )
    likes = models.PositiveSmallIntegerField(default=0)
    dislikes = models.PositiveSmallIntegerField(default=0)
    objects = managers.ProfileManager()

    def __str__(self):
        return str(self.user)

    def url(self):
        return reverse('profile', kwargs={'pk': self.pk})

    def liked(self, liker):
        """ True - если лайк, False - если дизлайк, None - если нет оценки """
        likes = Like.objects.filter(liker=liker.pk, likee=self.pk)
        if likes.count():
            return likes.first().is_positive
        return None


    def like(self, liker, is_positive=True):
        """ поставить лайк этому профилю """
        like, created = Like.objects.get_or_create(liker=liker, likee=self)
        if not created:
            if is_positive and not like.is_positive:
                self.likes += 1
                self.dislikes -= 1
            if not is_positive and like.is_positive:
                self.likes -= 1
                self.dislikes += 1
        else:
            if is_positive:
                self.likes += 1
            else:
                self.dislikes += 1
        like.is_positive = is_positive
        like.save()
        self.save()
        return like


    def recount(self):
        """ на всякий случай """
        self.likes = Like.objects.filter(is_positive=True).count()
        self.dislikes = Like.objects.filter(is_positive=False).count()
        self.save()


class Like(models.Model):
    liker = models.ForeignKey(
        'Profile',
        related_name='likers',
        on_delete=models.SET_NULL,
        null=True,
    )
    likee = models.ForeignKey(
        'Profile',
        related_name='likees',
        on_delete=models.SET_NULL,
        null=True,
    )
    is_positive = models.BooleanField(default=True)
