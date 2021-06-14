from django.urls import path
# views.pyとurls.pyは同じディレクトリに存在しているため「from . 」（カレントディレクトリからImportする
from . import views

app_name = 'analysis'  # analysisという名前空間の中にあるものを，htmlから呼び出しがあると，それに対応したviews.pyを引き出す

# 全体のURLパスは
# 親のurls.pyの定義 |    アプリケーションのurls.pyの定義  になる
# 一番上はhttp://127.0.0.1/analysis/analysis_list/になる

urlpatterns = [
    path('top/', views.topview, name='topview'),
    path('analysis_list/', views.AnalysisListView.as_view(), name='analysis_list'),
    path('analysis_create/', views.AnalysisCreateView.as_view(), name='analysis_create'),
    path('create_done/', views.create_done, name='create_done'),
    path('update/<int:pk>/', views.AnalysisUpdateView.as_view(), name='analysis_update'),
    path('update_done/', views.update_done, name='update_done'),
    path('delete/<int:pk>/', views.AnalysisDeleteView.as_view(), name='analysis_delete'),
    path('delete_done/', views.delete_done, name='delete_done'),
    # path('login/', views.MyLoginView.as_view(), name="login"),
    # path('logout/', views.MyLogoutView.as_view(), name="logout"),
    # path('index/',views.IndexView.as_view(), name="index"),
#     aika
]
