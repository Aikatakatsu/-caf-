from django.shortcuts import render
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from .models import Job, Purpose, Trigger, UserProfile
from .forms import AnalysisForm
from django.urls import reverse_lazy
# aika
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from . import forms
from django.contrib.auth import get_user_model
from django.shortcuts import render
from django.views import generic
from .forms import UserCreateForm


class AnalysisListView(ListView):
    model = UserProfile
    template_name = 'analysis/analysis_list.html'


class AnalysisCreateView(CreateView):
    model = UserProfile
    form_class = AnalysisForm
    success_url = reverse_lazy('analysis:create_done')

def create_done(request):
    return render(request, 'analysis/create_done.html')


class AnalysisUpdateView(UpdateView):
    model = UserProfile
    form_class = AnalysisForm
    success_url = reverse_lazy('analysis:update_done')


def update_done(request):
    return render(request, 'analysis/update_done.html')

class AnalysisDeleteView(DeleteView):
    # 利用するモデルを指定
    model = UserProfile
    # 削除処理が正常終了した場合の遷移先を指定
    success_url = reverse_lazy('analysis:delete_done')


def delete_done(request):
    return render(request, 'analysis/delete_done.html')


def topview(request):
    return render(request, 'analysis/top.html')

# aika
class MyLoginView(LoginView):
    form_class = forms.LoginForm
    template_name = "registration/login.html"

class MyLogoutView(LoginRequiredMixin, LogoutView):
    template_name = "registration/logout.html"

class IndexView(TemplateView):
    template_name = "registration/index.html"

# aika
User = get_user_model()


class UserList(generic.ListView):
    template_name = 'register/user_list.html'  # デフォルトUserだと、authアプリケーションのuser_list.htmlを探すため、明示的に書いておく
    model = User


class UserDataInput(generic.FormView):
    """ユーザー情報の入力

    このビューが呼ばれるのは、以下の2箇所です。
    ・初回の入力欄表示(aタグでの遷移)
    ・確認画面から戻るを押した場合(これはPOSTで飛んできます)

    初回の入力欄表示の際は、空のフォームをuser_data_input.htmlに渡し、
    戻る場合は、POSTで飛んできたフォームデータをそのままuser_data_input.htmlに渡します。

    """
    template_name = 'register/user_data_input.html'
    form_class = UserCreateForm

    def form_valid(self, form):
        return render(self.request, 'register/user_data_input.html', {'form': form})


class UserDataConfirm(generic.FormView):
    """ユーザー情報の確認

    ユーザー情報入力後、「送信」を押すとこのビューが呼ばれます。(user_data_input.htmlのform action属性がこのビュー)
    データが問題なければuser_data_confirm.html(確認ページ)を、入力内容に不備があればuser_data_input.html(入力ページ)に
    フォームデータを渡します。

    """
    form_class = UserCreateForm

    def form_valid(self, form):
        return render(self.request, 'register/user_data_confirm.html', {'form': form})

    def form_invalid(self, form):
        return render(self.request, 'register/user_data_input.html', {'form': form})


class UserDataCreate(generic.CreateView):
    """ユーザーデータの登録ビュー。ここ以外では、CreateViewを使わないでください"""
    form_class = UserCreateForm
    success_url = reverse_lazy('register:user_list')

    def form_invalid(self, form):
        """基本的にはここに飛んでこないはずです。UserDataConfrimでバリデーションは済んでるため"""
        return render(self.request, 'register/user_data_input.html', {'form': form})
