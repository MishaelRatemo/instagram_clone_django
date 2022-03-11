from django.test import TestCase

from .models import Profile, Post , Comment
from django.contrib.auth.models import User


class TestProfile(TestCase):
    def setUp(self):
        self.user = User(username='Mishael')
        self.user.save()

        self.profile_test = Profile(id=1, user='Mishael', image='default.jpg', bio='this is a test profile',
                                    user=self.user)

    def test_instance(self):
        self.assertTrue(isinstance(self.profile_test, Profile))

    def test_save_profile(self):
        self.profile_test.save_profile()
        after = Profile.objects.all()
        self.assertTrue(len(after) > 0)


class TestPost(TestCase):
    def setUp(self):
        self.profile_test = Profile(user='Mishael', user=User(username='Mishael'))
        self.profile_test.save()

        self.image_test = Post(image='food.png', title='test', description='test test test', user=self.profile_test)

    def test_insatance(self):
        self.assertTrue(isinstance(self.image_test, Post))

    def test_save_image(self):
        self.image_test.save_image()
        images = Post.objects.all()
        self.assertTrue(len(images) > 0)

    def test_delete_image(self):
        self.image_test.delete_image()
        after = Profile.objects.all()
        self.assertTrue(len(after) < 1)
        
class TestComment(TestCase):
    def setUp(self):
        self.test_comment = User(author='Mishael')
        self.test_comment.save()
        self.test_comment = Comment(content='Woow this is nice')
    