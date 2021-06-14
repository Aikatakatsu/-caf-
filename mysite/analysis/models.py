from django.db import models
from datetime import datetime


# 【カテゴリーテーブル】
class Category(models.Model):
    class Meta:  # ①
        # テーブル名の指定
        db_table = "category"
        verbose_name = "カテゴリ"  # 追加
        verbose_name_plural = "カテゴリ"  # 追加

    # カラム名の定義
    category_name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.category_name


# 【家計簿テーブル】
class Analysis(models.Model):
    class Meta:
        # テーブル名
        db_table = "kakeibo"
        verbose_name = "家計簿"  # 追加
        verbose_name_plural = "家計簿"  # 追加

    # カラムの定義
    date = models.DateField(verbose_name="日付", default=datetime.now)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, verbose_name="カテゴリ")  # 外部キーとしてCategoryを設定
    money = models.IntegerField(verbose_name="金額", help_text="※単位は日本円")
    memo = models.CharField(verbose_name="メモ", max_length=500)

    def __str__(self):
        return self.memo

