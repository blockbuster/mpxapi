from mpxapi.api_base import ApiBase


class UserListItem(ApiBase):
    def __init__(self, api):
        ApiBase.__init__(self, api)

        self.schema = "1.3.0"
        self.service = "User Profile Data Service"
        self.path = "/data/UserListItem"