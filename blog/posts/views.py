from django.http import JsonResponse
from django.shortcuts import get_object_or_404

from .models import BlogContent
from .models import Tags


#Maybe this shouldn't be called "post" given it is a GET Endpoint... maybe get_post and get_posts
def post(request, slug):
    #probably need to do some authentication with the request
    post = get_object_or_404(BlogContent, Slug=slug)
    try:
        tags = Tags.objects.filter(Slug=slug)[:5]
        tag_attributes = [tag.Tag for tag in tags]
    except Tags.DoesNotExist: ##maybe should be an exception as if no tag something very wrong has happened
        tag_attributes = []     
    serialized_post = {
        'title': post.Title,
        'author': post.Author,
        'content': post.Content,
        'tags': tag_attributes
    }
    
    response = JsonResponse({'post': serialized_post})
    response['Access-Control-Allow-Origin'] = "http://localhost:3000"

    return response

def posts(request):
    #probably need to do some authentication with the request
    blog_posts = BlogContent.objects.all()
    print(len(blog_posts))
    serialized_blog_posts = [
        {
            'title': blog.Title,
            'slug': blog.Slug
        }
        for blog in blog_posts
    ]
    
    response = JsonResponse({'post': serialized_blog_posts})
    response["Access-Control-Allow-Origin"] = "http://localhost:3000"
   
    return response
   