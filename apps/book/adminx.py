from .models import *
from apps import xadmin
from apps.user.models import *


class BookAdmin(object):
    def restAmount(self, book: Book):
        return book.amount - Borrow.objects.filter(returnTime__isnull=True).count()

    restAmount.short_description = "剩余数目"

    common = [
        'name', 'author', 'publisher', 'date', 'amount', 'ISBN'
    ]
    list_display = common + ['restAmount']
    search_fields = common
    list_editable = common
    list_filter = common


xadmin.site.register(Book, BookAdmin)
