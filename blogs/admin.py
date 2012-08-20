# vim: set fileencoding=utf-8 :
from django.contrib import admin
from models import Article


class ArticleAdmin(admin.ModelAdmin):
    # Adminサイトのモデルに対するカスタマイズはこのように
    # admin.ModelAdminを継承したクラスで行う
    date_hierarchy = 'updated_at'                       # 更新日ベースで絞り込み
    list_display = ('title', 'summary', 'updated_at')   # リスト表示で表示する項目
    search_fields = ('title', 'body')                   # 検索に使用する項目

    def summary(self, obj):
        # 本文そのままだと長いので要約する。要約にはテンプレートタグを使用する
        from django.template.defaultfilters import truncatechars
        from django.template.defaultfilters import truncatewords
        # 英文が多い場合は truncatewords を使用し日本語分がメインの場合には
        # truncatechars を使用するように各自変更
        summary = truncatewords(obj.body, 20)
        # 改行をスペースに変換
        summary = summary.replace("\n", " ")
        return summary

# ArticleモデルをArticleAdminと結びつけて登録
admin.site.register(Article, ArticleAdmin)
