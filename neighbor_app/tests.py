# Create your tests here.
from neighbor_app.views import neighborhood
from django.test import TestCase
from .models import Business,Profile,NeighborHood,Post
from django.contrib.auth.models import User


class BusinessTest(TestCase):
  def setUp(self):
    self.user = User.objects.create(id=1, username='obonyo')
    self.neighborhood = NeighborHood.objects.create(id=1, name='home')
    self.busines = Business.objects.create(id=1, name='Moringa business', description='Moringa business description',image='https://cloudinary url',created_at='2021,6,26',updated_at='2021,6,26', neighborhood=self.neighborhood,user=self.user,email='obonyocy@ueab.ac.ke')

  def test_instance(self):
    self.assertTrue(isinstance(self.busines, Business))

  def test_create_business(self):
    self.busines.create_business()
    business = Business.objects.all()
    self.assertTrue(len(business) > 0)

  def test_get_business(self, id):
    self.business.save()
    business = Business.get_businesss(post_id=id)
    self.assertTrue(len(business) == 1)


class TestProfile(TestCase):
  def setUp(self):
    self.user = User(id=1, username='obonyo', password='akoth1998')
    self.user.save()

  def test_instance(self):
    self.assertTrue(isinstance(self.user, User))

  def test_save_user(self):
    self.user.save()

  def test_delete_user(self):
    self.user.delete()

class PostTest(TestCase):
  def setUp(self):
    self.user = User.objects.create(id=1, username='obonyo')
    self.neighborhood = NeighborHood.objects.create(id=1, name='home')
    self.post = Post.objects.create(id=1, title='Moringa post', post='Moringa post description',image='https://cloudinary url',created_at='2021,6,26',updated_at='2021,6,26',user=self.user,neighborhood=self.neighborhood)

  def test_instance(self):
    self.assertTrue(isinstance(self.post, Post))

  def test_display_posts(self):
    self.post.save()
    posts = Post.all_posts()
    self.assertTrue(len(posts) > 0)

  def test_save_post(self):
    self.post.save_post()
    post = Post.objects.all()
    self.assertTrue(len(post) > 0)

  def test_delete_post(self):
    self.post.delete_post()
    post = Post.search_post('random_post')
    self.assertTrue(len(post) < 1)

class NeighborhoodTest(TestCase):
  def setUp(self):
    self.user = User.objects.create(id=1, username='obonyo')
    self.neighborhood = NeighborHood.objects.create(id=1, name='Moringa business', description='Moringa business description',image='https://cloudinary url',created_at='2021,6,26',updated_at='2021,6,26', neighborhood=self.neighborhood,user=self.user,email='nick@gmail.com')

  def test_create_neighborhood(self):
    self.neighborhood.create_neighborhood()
    neighborhood = NeighborHood.objects.all()
    self.assertTrue(len(neighborhood) > 0)

  def test_get_neighborhood(self, id):
    self.neighborhood.save()
    neighborhood = NeighborHood.get_neighborhood(neighborhood_id=id)
    self.assertTrue(len(neighborhood) == 1)
