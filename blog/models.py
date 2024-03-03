from django.db import models
from django.contrib.auth.models import User 
from cloudinary.models import CloudinaryField

STATUS = ((0, "Draft"), (1, "Published"))

# Create your models here.
class Post(models.Model):
  """ 
  Stores a single blog post entry related to :model:`auth.User`.
  """
  title = models.CharField(max_length = 200, unique = True)
  slug = models.SlugField(max_length = 200, unique = True)
  author = models.ForeignKey(
    User, on_delete=models.CASCADE, related_name="blog_posts"
  )
  featured_image = CloudinaryField('image', default='placeholder')
  content = models.TextField()
  created_on = models.DateTimeField(auto_now_add = True)
  status = models.IntegerField(choices=STATUS, default=0)
  excerpt = models.TextField(blank=True)
  updated_on = models.DateTimeField(auto_now = True)

  class Meta:
    ordering = ["created_on"]

  def __str__(self):
    return f"{self.title} | written by {self.author}"

class Comment(models.Model):
  """ 
  Stores a single comment entry related to :model:`auth.User`
  and :model:`blog.Post`.
  """
  post = models.ForeignKey(
    Post, on_delete=models.CASCADE, related_name="comments"
  )
  author = models.ForeignKey(
    User, on_delete=models.CASCADE, related_name="comment_author"
  )
  body = models.TextField()
  approved = models.BooleanField(default=False)
  created_on = models.DateTimeField(auto_now_add=True)

  class Meta:
    ordering = ["created_on"]
  
  def __str__(self):
    return f"Comment {self.body} by {self.author}"

# EXAMPLES:

# class Event(models.Model):
#   event_name = models.CharField(max_length = 200, unique = True)
#   location = models.CharField(max_length = 200, unique = True)
#   date = models.DateTimeField()

#   def __str__(self):
#     return self.event_name

# class Ticket(models.Model):
#   ticket_holder = models.ForeignKey(
#     User, on_delete=models.CASCADE, related_name="user_tickets"
#   )
#   date_issued = models.DateTimeField(auto_now_add = True)
#   event = models.ForeignKey(
#     Event,
#     on_delete=models.CASCADE,
#     related_name="event_ticekts"
#   )

#   def __str__(self):
#     return f"Ticekt for {self.ticket_holder}"