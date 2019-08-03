# coding:utf-8

from haystack import indexes
from .models import *

class HeroInfoIndex(indexes.SearchIndex,indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)

    def get_model(self):
        return textEditer
    #定义对于那些数据进行检索，可以使用过滤器进行定义
    def index_queryset(self, using=None):
        return self.get_model().objects.all()
