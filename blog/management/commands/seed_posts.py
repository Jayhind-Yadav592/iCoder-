from django.core.management.base import BaseCommand
from blog.models import Post, Profile
from django.contrib.auth.models import User
from django.utils.text import slugify
from django.utils import timezone

class Command(BaseCommand):
    help = "Insert default blog posts with avatar & thumbnail"

    def handle(self, *args, **kwargs):

        posts = [
            {
                "title": "Introduction to Python",
                "author": "Amit Verma",
                "content": "Python is a beginner friendly programming language.",
                "avatar": "avatars/amit.png",
                "thumbnail": "blog_thumbnails/python.png"
            },
            {
                "title": "Django vs Flask",
                "author": "Rahul Sharma",
                "content": "Django full framework hai, Flask micro framework.",
                "avatar": "avatars/rahul.png",
                "thumbnail": "blog_thumbnails/django.png"
            },
            {
                "title": "What is API?",
                "author": "Ram Singh",
                "content": "API do applications ko connect karta hai.",
                "avatar": "avatars/ram.png",
                "thumbnail": "blog_thumbnails/api.png"
            },
        ]

        for p in posts:

            # create user
            user, created = User.objects.get_or_create(username=p["author"])

            if created:
                user.set_password("12345")
                user.save()

            # update avatar
            profile = Profile.objects.get(user=user)
            profile.avatar = p["avatar"]
            profile.save()

            # create post
            Post.objects.get_or_create(
                slug=slugify(p["title"]),
                defaults={
                    "title": p["title"],
                    "author": user,
                    "content": p["content"],
                    "timeStamp": timezone.now(),
                    "thumbnail": p["thumbnail"]
                }
            )

        self.stdout.write(self.style.SUCCESS("Posts inserted successfully!"))
