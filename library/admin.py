from django.contrib import admin
from .models import Book, Review, Delivery

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author')

class ReviewAdmin(admin.ModelAdmin):
    list_display = ('book', 'rating', 'admin_confirmed')
    list_filter = ('book', 'rating', 'admin_confirmed')

class DeliveryAdmin(admin.ModelAdmin):
    list_display = ('book', 'area', 'deliverd')
    list_filter = ('deliverd',)

admin.site.register(Book, BookAdmin)
admin.site.register(Review, ReviewAdmin)
admin.site.register(Delivery, DeliveryAdmin)
