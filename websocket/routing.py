from channels.routing import route


channel_routing = [
    route("http.request", "dchannels.consumers.http_consumer"),
]