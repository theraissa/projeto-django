from django.contrib import admin
from .models import DespUser
from .models import Documento
from .models import Servico
from .models import Estabelecimento

admin.site.register(DespUser)
admin.site.register(Documento)
admin.site.register(Servico)
admin.site.register(Estabelecimento)

