from django.contrib import admin
from .models import Book, Review, Delivery, OccupiedBook

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author')

class ReviewAdmin(admin.ModelAdmin):
    list_display = ('book','rating', 'admin_confirmed')
    list_filter = ('book', 'rating', 'admin_confirmed')

class DeliveryAdmin(admin.ModelAdmin):

    def mark_delivered(self, request, queryset):
        rows_updated = queryset.update(delivered=True)
        if rows_updated == 1:
            message_bit = "1 Delivery was"
        else:
            message_bit = "%s Deliveries were" % rows_updated
        self.message_user(request, "%s successfully marked as Delivered." % message_bit)
    mark_delivered.short_description = "Mark as Delivered"

    def mark_not_delivered(self, request, queryset):
        rows_updated = queryset.update(delivered=False)
        if rows_updated == 1:
            message_bit = "1 Delivery was"
        else:
            message_bit = "%s Deliveries were" % rows_updated
        self.message_user(request, "%s successfully marked as Not Delivered." % message_bit)
    mark_not_delivered.short_description = "Mark as Not Delivered"

    list_display = ('book', 'user', 'area', 'delivered')
    list_filter = ('area','delivered')
    actions = [mark_delivered, mark_not_delivered]

class OccupiedBookAdmin(admin.ModelAdmin):
    list_display = ('user', 'book')
    list_filter = ('user', 'book')

admin.site.register(Book, BookAdmin)
admin.site.register(Review, ReviewAdmin)
admin.site.register(Delivery, DeliveryAdmin)
admin.site.register(OccupiedBook, OccupiedBookAdmin)
admin.site.site_header = "Surya Library Admin"
admin.site.site_title = "Surya Library Admin"
admin.site.site_url = None
