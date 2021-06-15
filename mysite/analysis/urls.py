from django.urls import path
from . import views

# from django.contrib.auth.models import User

# analysisという名前空間を設定
app_name = 'analysis'

urlpatterns = [
	path('top/', views.topview, name='topview'),
	path('analysis_list/', views.AnalysisListView.as_view(), name='analysis_list'),
	path('analysis_create/', views.AnalysisCreateView.as_view(), name='analysis_create'),
	path('create_done/', views.create_done, name='create_done'),
	path('update/<int:pk>/', views.AnalysisUpdateView.as_view(), name='analysis_update'),
	path('update_done/', views.update_done, name='update_done'),
	path('delete/<int:pk>/', views.AnalysisDeleteView.as_view(), name='analysis_delete'),
	path('delete_done/', views.delete_done, name='delete_done'),
	# ログイン画面
	path('top/', views.topview, name='topview'),
	# 管理者用の一覧画面
	path('analysis_list/', views.AnalysisListView.as_view(), name='analysis_list'),
	# 新規登録：ユーザー名，パスワード等画面
	path('register_create/', views.AnalysisRegisterView.as_view(), name='register_create'),
	# ユーザ登録完了画面
	path('register_done/', views.register_done, name='register_done'),
	# 新規登録：個人情報を登録する画面
	path('analysis_create/<int:pk>/', views.AnalysisCreateView.as_view(), name='analysis_create'),
	# 新規登録完了画面
	path('create_done/', views.create_done, name='create_done'),
	# 更新画面
	path('update/<int:pk>/', views.AnalysisUpdateView.as_view(), name='analysis_update'),
	# 更新完了画面
	path('update_done/', views.update_done, name='update_done'),
	# 削除画面
	path('delete/<int:pk>/', views.AnalysisDeleteView.as_view(), name='analysis_delete'),
	# 削除完了画面
	path('delete_done/', views.delete_done, name='delete_done'),
	# 円グラフ表示
	path('circle/', views.show_gender_circle_graph, name='gender_circle'),
]
