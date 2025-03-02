from django.contrib import admin
from .models import Post, Carousel

@admin.register(Carousel)
class CarouselAdmin(admin.ModelAdmin):
    list_display = ('title', 'active')
    list_filter = ('active',)
    search_fields = ('title',)


admin.site.register(Post)
