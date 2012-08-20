# vim: set fileencoding=utf-8 :
# DjangoにはGenericViewと呼ばれる決まりきった処理を行うViewが予め用意されている
# 今回のArticleは
#   1. リスト表示
#   2. 詳細表示
# の簡単なことしか行わないためGenericViewと継承し、対象となるモデルを指定するだ
# けでViewは完了する
from django.views.generic import ListView
from django.views.generic import DetailView

from blogs.models import Article


class ArticleListView(ListView):
    model = Article


class ArticleDetailView(DetailView):
    model = Article

