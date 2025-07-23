from django.contrib import admin
from .models.core import Ward
from .models.spatial import InfrastructureType, Infrastructure, Road, Building
from .models.user import User

admin.site.register(Ward)
admin.site.register(InfrastructureType)
admin.site.register(Infrastructure)
admin.site.register(Road)
admin.site.register(Building)
admin.site.register(User)
