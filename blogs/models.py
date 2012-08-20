# vim: set fileencoding=utf-8 :
from django.db import models
# ugettext_lazy は国際化のための関数だが _ でエイリアスするのが通例
from django.utils.text import ugettext_lazy as _

#
# Djangoのモデルはすべて ``django.db.models.Model`` を継承する
# 必要なフィールドはクラスのアトリビュートとして宣言するとDjangoが
# 自動的に作成・結びつけをおこなってくれる。
# なお、XxxxField の第一引数は（通常）そのフィールド名。今回は国際化を意識して
# ugettext_lazy 関数で囲んでいるが、国際化が必要なければ u"" でユニコード文字を
# 直接指定しても構わない
#
class Article(models.Model):
    # タイトルは最大文字数20文字。CharFieldはSQLでVARCHAR型になることが多い
    title = models.CharField(_('title'), max_length=20)
    # 本文は文字数制限を極力したくないためTextField。TEXT型になることが多い
    body = models.TextField(_('body'))
    # auto_now=Trueを指定すると「新規作成時」の時刻が自動的に適用される
    created_at = models.DateTimeField(
            _('date and time created'), auto_now=True)
    # auto_now_add=Trueを指定すると保存時（毎回）の時刻が自動的に適用される
    updated_at = models.DateTimeField(
            _('date and time updated'), auto_now_add=True)

    class Meta:
        # クエリの並び順をどのように決定するか
        ordering = ('updated_at', 'created_at', 'title')
        # Adminサイトなどで表示される名前
        verbose_name = _('article')
        # 同上（複数形）
        verbose_name_plural = _('articles')

    # Djangoのモデルはデフォルトで __repr__ に __unicode__ の結果を用いるため
    # __unicode__ を指定しておくとデバッグ時に便利
    def __unicode__(self):
        return self.title

    # 慣用的に get_absolute_url でこのモデルの詳細情報を表示するURLを返すことに
    # なっている。また models.permalink デコレータを使用した場合は
    # 1. URLパターン名
    # 2. 名前なし引数リスト
    # 3. 名前あり引数辞書
    # のタプル・リストを返すことで内部的に reverse を呼びURLを自動生成できる 
    @models.permalink
    def get_absolute_url(self):
        return ('blogs-article-detail', (), {'pk': self.pk})
