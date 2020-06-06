from .mixins import APIMixin, LoggerMixin


class BaseApiView(APIMixin, LoggerMixin):
    pass
