class ServiceError(Exception):
    pass


class AppNotAuthorized(ServiceError):
    pass


class LocationNotFound(ServiceError):
    pass
