from .models import *
import xadmin
from xadmin import views


class UserAdmin(object):
    def borrowCounts(self, user: User):
        return Borrow.objects.filter(borrower_id=user.id).count()

    def returnCounts(self, user: User):
        return Borrow.objects.filter(borrower_id=user.id, returnTime__isnull=False).count()

    def unReturnCounts(self, user: User):
        return Borrow.objects.filter(borrower_id=user.id, returnTime__isnull=True).count()

    def overdueCounts(self, user: User):
        total = 0
        for borrow in Borrow.objects.filter(borrower_id=user.id):
            if borrow.isOverdue():
                total += 1
        return total

    borrowCounts.short_description = "历史借阅量"
    returnCounts.short_description = "已归还数目"
    unReturnCounts.short_description = "未归还数目"
    overdueCounts.short_description = "逾期数目"

    common = [
        'name', 'major', 'studentID', 'createTime', 'type', 'phone',
    ]
    list_display = common + ['borrowCounts', 'returnCounts', 'unReturnCounts', 'overdueCounts']
    search_fields = common
    list_editable = common
    list_filter = common


class BorrowAdmin(object):
    def isOverdue(self, borrow: Borrow):
        # return '已逾期' if borrow.isOverdue() else '未逾期'
        return ['未逾期', '已逾期'][borrow.isOverdue()]

    isOverdue.short_description = "是否逾期"

    common = [
        'borrower', 'borrowBook', 'createTime', 'returnTime', 'limitTime'
    ]
    list_display = common + ['isOverdue']
    search_fields = common
    list_editable = common
    list_filter = common


class BaseSetting(object):
    enable_themes = True
    use_bootswatch = True


class GlobalSetting(object):
    site_title = "图书管理系统"
    site_footer = "SZTU"


xadmin.site.register(User, UserAdmin)
xadmin.site.register(Borrow, BorrowAdmin)
xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(views.CommAdminView, GlobalSetting)
