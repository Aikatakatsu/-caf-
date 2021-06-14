from django.views.generic import CreateView, ListView, UpdateView, DeleteView, View
from .models import Job, Purpose, Trigger, UserProfile
from .forms import AnalysisForm, RegisterForm
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from django.contrib.auth.models import User


# ログイン画面
def topview(request):
    return render(request, 'analysis/top.html')


# 管理者用の一覧画面
class AnalysisListView(ListView):
    model = UserProfile
    template_name = 'analysis/analysis_list.html'


# 新規登録：ユーザー名，パスワード等画面
class AnalysisRegisterView(CreateView):
    model = User
    form_class = RegisterForm
    success_url = reverse_lazy('analysis:register_done')


# ユーザー登録完了画面
def register_done(request):
    return render(request, 'analysis/register_done.html')


# 新規登録：個人情報を登録する画面
class AnalysisCreateView(UpdateView):
    model = UserProfile
    form_class = AnalysisForm
    success_url = reverse_lazy('analysis:create_done')  # 完了したら完了画面へ


# 新規登録完了画面
def create_done(request):
    return render(request, 'analysis/create_done.html')


# 更新画面
class AnalysisUpdateView(UpdateView):
    model = UserProfile
    form_class = AnalysisForm
    success_url = reverse_lazy('analysis:update_done')  # 完了したら完了画面へ


# 更新完了画面
def update_done(request):
    return render(request, 'analysis/update_done.html')


# 削除画面
class AnalysisDeleteView(DeleteView):
    model = UserProfile
    success_url = reverse_lazy('analysis:delete_done')


# 削除完了画面
def delete_done(request):
    return render(request, 'analysis/delete_done.html')
