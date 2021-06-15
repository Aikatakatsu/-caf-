from django.shortcuts import render
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from .models import Job, Purpose, Trigger, UserProfile
from .forms import AnalysisForm
from django.urls import reverse_lazy

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
