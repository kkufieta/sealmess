from .shared import app
from .errors import *
from .views import *
from .customer_views import *
from .provider_views import *
from .order_views import *
from .menu_item_views import *

setup_db(app)