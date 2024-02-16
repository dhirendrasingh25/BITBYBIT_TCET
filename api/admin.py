from django.contrib import admin
from .models import UserData, Transaction,User

class TransactionAdmin(admin.ModelAdmin):
    list_display = ['transaction_id', 'item_name', 'total_items']

class UserDataAdmin(admin.ModelAdmin):
    list_display = ['username', 'first_name', 'last_name', 'email', 'salary', 'occupation', 'status_paid', 'status_unpaid']
    filter_horizontal = ['transactions']

admin.site.register(Transaction, TransactionAdmin)
admin.site.register(UserData, UserDataAdmin)
admin.site.register(User)
