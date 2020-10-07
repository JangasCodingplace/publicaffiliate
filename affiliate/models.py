import string
import random
import os
from django.db import models
from django.conf import settings
from django.urls import reverse


class Link(models.Model):
    key = models.CharField(
        max_length=16,
        unique=True,
        blank=True,
        help_text="If blank it gets autogenerated. **Max 16 Chars.**"
    )
    creator = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='links_created_by_user',
        on_delete=models.CASCADE
    )
    link = models.URLField()
    title = models.CharField(
        max_length=144
    )
    request_count = models.IntegerField(
        default=0,
        editable=False
    )
    creation_date = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return '{} //// current key: {}'.format(
            self.title, self.key
        )

    def save(self, *args, **kwargs):
        if self.key == '':
            self.key = self.generate_key()
        super().save(*args, **kwargs)

    def generate_key(self):
        letters_and_digits = string.ascii_letters + string.digits
        key_list = [random.choice(letters_and_digits) for i in range(6)]
        key = ''.join(key_list)
        while Link.objects.filter(key=key).exists():
            key_list = [random.choice(letters_and_digits) for i in range(6)]
            key = ''.join(key_list)
        return key

    @property
    def shared_link(self):
        if not self.pk:
            return ""
        return '{}{}'.format(
            os.getenv('BASE_URL'),
            reverse('redirection', args=[self.key])
        )

    @property
    def substring(self):
        if self.link.startswith("https://www."):
            substring = self.link[len("https://www."):]
        else:
            substring = self.link[len("https://"):]
        if substring.endswith('/'):
            return substring[:-1]
        return substring

    @property
    def desktop_link(self):
        return self.link

    @property
    def android_link(self):
        intent = "intent://#Intent;"
        package = "package=com.amazon.mShop.android.shopping;"
        scheme = "scheme=com.amazon.mobile.shopping.web://"
        link_substring = self.substring
        fallback = "S.browser_fallback_url={}".format(self.link)
        return "{}{}{}{};{}/;end".format(
            intent, package, scheme, link_substring, fallback
        )

    @property
    def apple_link(self):
        scheme = "com.amazon.mobile.shopping.web://"
        link_substring = self.substring
        # fallback = "S.browser_fallback_url={}".format(self.link)
        return "{}{}".format(
            scheme, link_substring
        )

