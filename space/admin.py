from django.contrib import admin
from . models import Products, Register

class RegisterAdmin(admin.ModelAdmin):
    list_display=('name','address','gender','phone','email')
admin.site.register (Register,RegisterAdmin)
class ProductsAdmin(admin.ModelAdmin):
    list_display=('product','price','desc','image')
admin.site.register (Products,ProductsAdmin)    
