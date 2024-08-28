import pytest 
from myapp.models import Post

def test_model_creation():
    obj = Post.objects.create(title="test post")
    assert obj.title == "test post"