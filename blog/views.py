from django.shortcuts import render, get_object_or_404, redirect
from blog.forms import CommentForm
from blog.models import Post
from django.utils import timezone
import logging
from django.views.decorators.cache import cache_page
from django.views.decorators.vary import vary_on_headers, vary_on_cookie
from django.utils.cache import patch_cache_control


logger = logging.getLogger(__name__)

# def cache_key_func(request, *args, **kwargs):
#   cache_key = f"user_{request.user.id}_{request.path}"
#   return cache_key


# Create your views here.

# @cache_page(300)
# @vary_on_headers("Cookie")
# @vary_on_cookie
def index(request):
  # from django.http import HttpResponse
  # patch_cache_control(request,private = True)
  # logger.debug("Index function is called")
  # return HttpResponse(str(request.user).encode("ascii"))
  posts = Post.objects.filter(published_at__lte=timezone.now())
  logger.debug("Got %d posts", len(posts))
  return render(request, "blog/index.html", {"posts":posts})


def post_detail(request, slug):
  post = get_object_or_404(Post, slug=slug)
  if request.user.is_active:
    if request.method == "POST":
      comment_form = CommentForm(request.POST)

      if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.content_object = post
        comment.creator = request.user
        comment.save()
        logger.info("Created comment on Post %d for user %s", post.pk, request.user)
        return redirect(request.path_info)
    else:
      comment_form = CommentForm()
  else:
    comment_form = None
  
  return render(request, "blog/post-detail.html", {"post":post, 'comment_form': comment_form})
    
