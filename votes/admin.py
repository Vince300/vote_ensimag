from django.contrib import admin

# Register your models here.
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from import_export import resources
import import_export.admin

from votes.models import TypeListe, Liste, Vote, Votant
from votes_ensimag import settings


class VotantResource(resources.ModelResource):
    class Meta:
        model = Votant

class VotantAdmin(import_export.admin.ImportExportModelAdmin):
    resource_class = VotantResource
    search_fields = ('id', 'prenom', 'nom', 'annee', 'login', 'apprenti', 'phelmag')
    list_filter = ('annee', 'a_vote', 'apprenti', 'phelmag')
    list_display = ('prenom', 'nom', 'annee', 'login', 'a_vote', 'apprenti', 'phelmag')

    if not settings.DEBUG:
        readonly_fields = ('prenom', 'nom', 'annee', 'login', 'apprenti', 'phelmag')

class ListeAdmin(admin.ModelAdmin):
    list_display = ('nom', 'color_box', 'logo', 'type', 'get_nombre_votes_1', 'get_nombre_votes_2')

class VoteResource(resources.ModelResource):
    class Meta:
        model = Vote

class VoteAdmin(import_export.admin.ImportExportModelAdmin):
    resource_class = VoteResource
    search_fields = ('ip', 'date', 'liste__nom', 'est_second_tour', 'votant__prenom', 'votant__nom', 'votant__annee')
    list_filter = ('liste', 'liste__type', 'liste__est_vote_blanc', 'est_second_tour', 'votant__apprenti', 'votant__phelmag')
    list_display = ('votant', 'ip', 'date', 'color_liste', 'vote_type', 'est_second_tour')
    raw_id_fields = ('votant',)

class TypeListeAdmin(admin.ModelAdmin):
    list_display = ('nom', 'deux_tours')

class VotantInline(admin.StackedInline):
    model = Votant
    can_delete = False
    verbose_name_plural = 'Votants'

class UserAdmin(UserAdmin):
    inlines = (VotantInline,)

# ------------------------------ Historique d'administration -------------------------------
from django.contrib.admin.models import LogEntry, DELETION
from django.utils.html import escape
from django.core.urlresolvers import reverse


class LogEntryAdmin(admin.ModelAdmin):

    date_hierarchy = 'action_time'

    readonly_fields = [field.name for field in LogEntry._meta.get_fields()]

    list_filter = [
        'user',
        'content_type',
        'action_flag'
    ]

    search_fields = [
        'object_repr',
        'change_message'
    ]


    list_display = [
        'action_time',
        'user',
        'content_type',
        'object_link',
        'action_flag',
        'change_message',
    ]

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return request.user.is_superuser and request.method != 'POST'

    def has_delete_permission(self, request, obj=None):
        return False

    def object_link(self, obj):
        if obj.action_flag == DELETION:
            link = escape(obj.object_repr)
        else:
            ct = obj.content_type
            link = u'<a href="%s">%s</a>' % (
                reverse('admin:%s_%s_change' % (ct.app_label, ct.model), args=[obj.object_id]),
                escape(obj.object_repr),
            )
        return link
    object_link.allow_tags = True
    object_link.admin_order_field = 'object_repr'
    object_link.short_description = u'object'
    
    def queryset(self, request):
        return super(LogEntryAdmin, self).queryset(request) \
            .prefetch_related('content_type')


admin.site.register(LogEntry, LogEntryAdmin)

# ------------------------------ Historique d'administration -------------------------------

admin.site.unregister(User)
admin.site.register(User, UserAdmin)

admin.site.register(TypeListe, TypeListeAdmin)
admin.site.register(Liste, ListeAdmin)
admin.site.register(Votant, VotantAdmin)
admin.site.register(Vote, VoteAdmin)
