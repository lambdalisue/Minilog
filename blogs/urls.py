# vim: set fileencoding=utf-8 :
from django.conf.urls import patterns, url

#
# urls.py は各アプリ毎で作成するのが慣例になっている
# 各アプリで作成することでそのアプリの使い回しがしやすくなるのが目的
#
# これは個人的好みだが各URLマッピングには
#   <app_label>-<model_name>-<view_name>
# というルールで名前をつけることにしている。以下例を示す
#   + blogs-article-list    ~ blogsアプリのArticleモデルのリスト表示
#   + blogs-article-detail  ~ blogsアプリのArticleモデルの詳細表示
#   + blogs-article-create  ~ blogsアプリのArticleモデルの新規作成
#   + blogs-article-update  ~ blogsアプリのArticleモデルの編集
#   + blogs-article-delete  ~ blogsアプリのArticleモデルの削除
#
# また、Django本家チュートリアルではGenericViewをurls.pyで使用しているが
# 以下の点から個人的には推奨しない
#   + urls.py はViewの機能的側面を書く場所じゃない気がする
#   + views.py に必ず書くことで views.py を見れば機能がわかる
#   + 後で拡張しようと思った時に urls.py に書いていた場合面倒臭い
#   + 後で拡張しようと思った時に views に継承で書いてあれば簡単
# なのでこのサンプルプログラムでは不必要だが views に GenericViewを継承した
# Viewを作成して使用している
#
import views
urlpatterns = patterns('',
    url(r'^$', views.ArticleListView.as_view(), name='blogs-article-list'),
    # GenericViewのDetailViewは以下のどちらかを特定のオブジェクトを
    # 指定するために要求する
    #   1. object.pk                    ~ pk
    #   2. object.__dict__[slug_name]   ~ slug
    # ここでは正規表現で pk を 数値の一度以上の繰り返しとしている。このように
    # 正規表現グループしたものは View の dispatch に kwargs として渡され、先の 
    # pk や slug は DetailView においてオブジェクトを一意に決定する際に使用される
    url(r'^(?P<pk>\d+)/$', views.ArticleDetailView.as_view(),
        name='blogs-article-detail'),
)
