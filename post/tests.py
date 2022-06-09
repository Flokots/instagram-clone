from django.test import TestCase
from .models import Tag, Post

# Create your tests here.

class TagTestClass(TestCase):
    # Set up method
    def setUp(self):
        self.test_tag= Tag(id=1, title='Tag')

    def tearDown(self):
        Tag.objects.all().delete()

    # Testing instance
    def test_instance(self):
        self.assertTrue(isinstance(self.test_tag, Tag))

    # Testing save method
    def test_save_method(self):
        self.test_tag.save_tag()
        tags = Tag.objects.all()
        self.assertTrue(len(tags) > 0)

    
    def test_delete_method(self):
        self.test_tag.delete_category()
        tags = Tag.objects.all()
        self.assertTrue(len(tags) == 0)
    

    def test_update_category(self):
        self.test_tag.title = 'Tag'
        self.test_tag.save_tag()
        self.assertEqual(self.test_tag.title, 'Tag')


class PostTestClass(TestCase):
    # Set up method
    def setUp(self):
        # Creating a new Tag and saving it
        self.new_tag = Tag(id=1, title='Tag')
        self.new_tag.save()

        # Creating a new image and saving it
        self.new_image = Post(id=1, name="Post", description="Post Description", tag=self.new_tag)
        self.new_image.save()

    
    def tearDown(self):
        Post.objects.all().delete()
        Tag.objects.all().delete()
        Post.objects.all().delete()

    
    def test_instance(self):
        self.assertTrue(isinstance(self.new_image, Post))
    

    def test_save_method(self):
        self.new_image.save_image()
        images = Post.objects.all()
        self.assertTrue(len(images) > 0)
    

    def test_delete_method(self):
        self.new_image.delete()
        images = Post.objects.all()
        self.assertTrue(len(images) == 0)
    
    def test_update_method(self):
        self.new_image.name = 'New Post'
        self.new_image.save_image()
        self.assertEqual(self.new_image.name, 'New Post')


    def test_get_image_by_id(self):
        self.image = Post.objects.get(id=1)

        self.assertEqual(self.image.name, 'Post')


    
    def test_search_image_category(self):
        self.image = Post.objects.get(category=self.new_tag)

        self.assertEqual(self.image.name, 'Post')
