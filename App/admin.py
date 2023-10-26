from django.contrib import admin

# Register your models here.
from.models import post


#class postAdmin(admin.ModelAdmin):
  # list_display = ('title','slug','status','created_on')
  # list_filter = ('status',)
   #search_fields  =  ['title','content']

@admin.register(post)
class AdminPost(admin.ModelAdmin): 
  list_display =(
    'title','content','date','author'
  )
  list_filter =(

   'author','date'


  )

#admin.site.register(post)
     

  