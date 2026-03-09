
# Create your tests here.
from django.contrib.auth.models import User
from admin import *
from views import *

User.objects.filter(is_superuse=True)