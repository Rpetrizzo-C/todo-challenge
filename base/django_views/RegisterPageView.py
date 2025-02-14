from django.shortcuts import redirect
from django.views.generic.edit import FormView
from django.urls import reverse_lazy


from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login


from django.shortcuts import redirect


class RegisterPageView(FormView):
    template_name = 'base/register.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('tasks')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(RegisterPageView, self).form_valid(form)

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('tasks')
        return super(RegisterPageView, self).get(*args, **kwargs)




