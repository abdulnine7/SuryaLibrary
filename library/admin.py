from django.contrib import admin
from .models import Book, Review, Delivery, OccupiedBook

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author')

class ReviewAdmin(admin.ModelAdmin):
    list_display = ('book','rating', 'admin_confirmed')
    list_filter = ('book', 'rating', 'admin_confirmed')

class DeliveryAdmin(admin.ModelAdmin):
    list_display = ('book', 'user', 'area', 'deliverd')
    list_filter = ('deliverd',)

class OccupiedBookAdmin(admin.ModelAdmin):
    list_display = ('user', 'book')
    list_filter = ('user', 'book')

admin.site.register(Book, BookAdmin)
admin.site.register(Review, ReviewAdmin)
admin.site.register(Delivery, DeliveryAdmin)
admin.site.register(OccupiedBook, OccupiedBookAdmin)
