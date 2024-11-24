from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from .models import Task, Comment
from .forms import TaskForm, TaskFilterForm, UserRegistrationForm, CommentForm
from .mixin import UserIsCommentOwnerMixin, UserIsOwnerMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import login
from django.http import HttpResponseRedirect


class TaskList(ListView):
    model = Task
    template_name = 'task_list.html'
    context_object_name = "tasks"

    def get_queryset(self):
        queryset = super().get_queryset()
        status = self.request.GET.get("status")
        priority = self.request.GET.get("priority")

        if status:
            queryset = queryset.filter(status=status)
        if priority:
            queryset = queryset.filter(priority=priority)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["filter_form"] = TaskFilterForm(self.request.GET)

        return context


class TaskDetail(DetailView):
    model = Task
    template_name = 'task_detail.html'
    context_object_name = "task"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comments'] = self.object.comments.all()
        context['comment_form'] = CommentForm
        context["current_user"] = self.request.user

        return context

    def post(self, request, *args, **kwargs):
        form = CommentForm(request.POST, request.FILES)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.task = self.get_object()
            comment.save()

            return redirect('task-detail', pk=self.get_object().pk)
        else:
            return redirect('task-detail', pk=self.get_object().pk)


class TaskCreate(CreateView):
    model = Task
    form_class = TaskForm
    success_url = '/'
    template_name = 'task_create.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class TaskDelete(LoginRequiredMixin, UserIsOwnerMixin, DeleteView):
    model = Task
    success_url = '/'
    template_name = 'confirm_delete.html'


class TaskUpdate(LoginRequiredMixin, UserIsOwnerMixin, UpdateView):
    model = Task
    form_class = TaskForm
    success_url = '/'
    template_name = 'task_update.html'


class CommentDelete(LoginRequiredMixin, UserIsCommentOwnerMixin, DeleteView):
    model = Comment
    template_name = 'confirm_delete.html'

    def get_success_url(self):
        return reverse_lazy('task-detail', kwargs={"pk": self.get_object().task.pk})


class CommentUpdate(LoginRequiredMixin, UserIsCommentOwnerMixin, UpdateView):
    model = Comment
    form_class = CommentForm
    template_name = 'comment_update.html'

    def get_success_url(self):
        return reverse_lazy('task-detail', kwargs={"pk": self.get_object().task.pk})


class LikeView(LoginRequiredMixin, UpdateView):
    model = Comment

    def post(self, request, *args, **kwargs):
        comment = self.get_object()

        if comment.dislikes.filter(id=request.user.id).exists():
            comment.dislikes.remove(request.user)

        if comment.likes.filter(id=request.user.id).exists():
            comment.likes.remove(request.user)
        else:
            comment.likes.add(request.user)

        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        return reverse_lazy('task-detail', kwargs={'pk': self.get_object().task.pk})


class DislikeView(LoginRequiredMixin, UpdateView):
    model = Comment

    def post(self, request, *args, **kwargs):
        comment = self.get_object()

        if comment.likes.filter(id=request.user.id).exists():
            comment.likes.remove(request.user)

        if comment.dislikes.filter(id=request.user.id).exists():
            comment.dislikes.remove(request.user)
        else:
            comment.dislikes.add(request.user)

        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        return reverse_lazy('task-detail', kwargs={'pk': self.get_object().task.pk})


def register(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)

            return redirect('/')
        else:
            return render(
                request,
                'register.html',
                {'form': form}
            )
    else:
        form = UserRegistrationForm()

        return render(
            request,
            "register.html",
            {"form": form}
        )
