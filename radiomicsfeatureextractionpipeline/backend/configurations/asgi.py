import os
import django
from channels.layers import get_channel_layer
from channels.routing import ProtocolTypeRouter, URLRouter
from django.conf.urls import url

from pipelineapp.consumers import MessageConsumer
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.configurations.settings')
django.setup()
#channel_layer = get_channel_layer()

application = ProtocolTypeRouter({
    # (http->django views is added by default)
    'websocket': URLRouter(
        [
            url(r"^progress-message/$", MessageConsumer),
        ]
    )
})
