# -*- coding: utf-8 -*-
__author__ = 'xiao'
import xadmin
from xadmin import views
from .models import InformationPublish


class MainDashboard(object):
    widgets = [
        [
            {"type": "html", "title": "问候语",
             "content": "<h3>欢迎来到后台管理系统</h3><p>开发团队: <br/>联系方式:451314789@qq.com</p>"},
            {"type": "list", "model": "accounts.user", 'params': {
                'o': '-create_time'}},
        ],
        [
            {"type": "qbutton", "title": "快捷窗口",
             "btns": [{'model': InformationPublish}]},
            {"type": "addform", "model": InformationPublish},
        ]
    ]


class BaseSetting(object):
    enable_themes = True
    use_bootswatch = True


class GlobalSetting(object):
    site_title = u'后台中心'
    site_footer = u'Powered by youran'
    apps_label_title = {
        'accounts': u'权限管理',
        'content': u'信息管理',
    }


class InformationPublishAdmin(object):
    def open_detail(self, instance):
        return "<a href='/center_intro/information_detail/?id=%s' target='_blank'>详情</a>" % instance.id

    open_detail.short_description = u'详情'
    open_detail.allow_tags = True
    open_detail.is_column = True
    list_display = ('title', 'create_time', 'origin', 'editor', 'status', 'open_detail')
    list_display_links = ('title',)
    list_editable = ('title', 'status',)
    ordering = ('-create_time', )
    # exclude = ('views',)
    list_per_page = 20
    search_fields = ['title']
    list_filter = ['origin', 'editor', 'status', ]
    style_fields = {'content': 'ueditor'}

xadmin.site.register(views.website.IndexView, MainDashboard)
xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(views.CommAdminView, GlobalSetting)
xadmin.site.register(InformationPublish, InformationPublishAdmin)