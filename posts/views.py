from django.shortcuts import render
from .models import Post
from .forms import PostCreateForm
from django.contrib.auth.decorators import login_required

@login_required
def post_create(request):
    if request.method == 'POST':
        form_data = request.POST
        image_files = request.FILES
        post_form = PostCreateForm(data=form_data, files=image_files)
        if post_form.is_valid():
            new_post = post_form.save(commit=False)
            new_post.user = request.user
            new_post.save()
            # return render(request, 'posts/post_created.html')
    else:
        post_form = PostCreateForm()
        context = {
            "post_form": post_form
        }
    return render(request, 'posts/post_form.html', context)
