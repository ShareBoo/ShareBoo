from django.contrib import admin

from .models import Book, Lending, LendingLog, User, Volume


admin.site.register(Book)
admin.site.register(Lending)
admin.site.register(LendingLog)
admin.site.register(User)
admin.site.register(Volume)
