class HomePageView(ListView):
    model = Peak
    template_name = 'index.html'


class CreatPeakView(LoginRequiredMixin, CreatView):
    model = Peak
    from_class = PeakForm
    template_name = 'post.html'

    def form_valid(self, form):
        post = form.save(commit=False)
        post.author = self.request.user
        result = Post.objects.filter(author=self.request.user).count() <= 3
        if result:
            post.save()
            return HttpResponseRedirect('/')
        else:
            return HttpResponseBedRequest('Лимит фотографий превышен. Не более 3 фотографий')

@login_required
def upload_resume(request):
    if request.method == 'Post':

        user_name = request.user.username
        form = PostForm(request.POST, request.FILES)

        if form.is_valid():
            cnt = Post.objects.filter(author=user_name).count()
            if cnt < 3:
                form.save()
                return HttpResponseRedirect("/")
            else:
                message = 'Вы не можете добавлять больше 3-х фото'
                return render(request, 'post.html',{'form':form, 'message': message})
    else:
        form = PostForm
    return render(request, 'post.html', {'form':form'})
