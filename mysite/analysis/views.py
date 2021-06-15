from django.views.generic import CreateView, ListView, UpdateView, DeleteView, View
from .models import Job, Purpose, Trigger, UserProfile
from .forms import AnalysisForm, RegisterForm
from django.urls import reverse_lazy
from django.db.models import Count

from django.shortcuts import render, redirect
from django.contrib.auth.models import User


# ログイン画面
def topview(request):
	return render(request, 'analysis/top.html')


# 管理者用の一覧画面
class AnalysisListView(ListView):
	model = UserProfile
	template_name = 'analysis/analysis_list.html'


class AnalysisCreateView(CreateView):
	model = UserProfile
	form_class = AnalysisForm
	success_url = reverse_lazy('analysis:create_done')


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
	success_url = reverse_lazy('analysis:update_done')


# 更新完了画面
def update_done(request):
	return render(request, 'analysis/update_done.html')


# 削除画面
class AnalysisDeleteView(DeleteView):
	# 利用するモデルを指定
	model = UserProfile
	# 削除処理が正常終了した場合の遷移先を指定
	success_url = reverse_lazy('analysis:delete_done')


# 削除完了画面
def delete_done(request):
	return render(request, 'analysis/delete_done.html')


def topview(request):
	return render(request, 'analysis/top.html')


# Create your views here.
def show_gender_circle_graph(request):
	# 全データ数とgroupbyを取得
	total = len(UserProfile.objects.all())
	pros = UserProfile.objects.values('gender').annotate(dcount=Count('gender'))

	#
	gender_dict = {}
	for i, item in enumerate(pros):
		num = item["dcount"]
		ratio = int((num / total) * 100)
		gender_dict[item["gender"]] = ratio

	return render(request, 'analysis/gender_circle.html', {
		'gender_dict': gender_dict,
	})
