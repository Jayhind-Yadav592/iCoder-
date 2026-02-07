from django.core.management.base import BaseCommand
from blog.models import Post   # <-- yahi change
from django.contrib.auth.models import User
from django.utils.text import slugify
from django.utils import timezone

class Command(BaseCommand):
    help = "Insert default blog posts"

    def handle(self, *args, **kwargs):

        # user create / get
        user, created = User.objects.get_or_create(username="admin")
        if created:
            user.set_password("admin123")
            user.save()

        posts = [
            {
                "title": "Introduction to Python",
                "content": "Python is a beginner friendly programming language used in web, AI and automation.",
            },
            {
                "title": "Django vs Flask",
                "content": "Django is a full framework while Flask is micro framework. Both are powerful for backend.",
            },
            {
                "title": "What is API?",
                "content": "API allows two applications to communicate with each other using requests and responses.",
            },
        ]

        for p in posts:
            Post.objects.get_or_create(
                title=p["title"],
                defaults={
                    "author": user,
                    "slug": slugify(p["title"]),
                    "content": p["content"],
                    "timeStamp": timezone.now()
                }
            )

        self.stdout.write(self.style.SUCCESS("Posts inserted successfully!"))
