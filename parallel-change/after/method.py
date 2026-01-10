class AuthenticationService:
    """
    the goal is to replace the method above with this one:
    def is_authenticated(self, role, id):
        return id == 12345
    """
    ROLES = ["admin", "user"]

    def is_authenticated(self, id):
        return id == 12345

    def is_authenticated_refactored(self, role: str = "", id: int = 0) -> bool:
        if role not in self.ROLES:
            raise ValueError("Invalid role")
        if not isinstance(id, int) or id <= 0:
            raise ValueError("Invalid id")
        return id == 12345


class AuthenticationClient:
    def __init__(self, authenticationService: AuthenticationService):
        self.authenticationService = authenticationService

    def run(self):
        authenticated = self.authenticationService.is_authenticated(33)
        authenticated_refactored = (
            self.authenticationService.is_authenticated_refactored("admin", 12345)
        )
        print("is authenticated: ", str(authenticated))
        print("is authenticated refactored: ", str(authenticated_refactored))



class YetAnotherClient:
    def run(self):
        AuthenticationService().is_authenticated(100)
        AuthenticationService().is_authenticated_refactored("admin", 12345)

if __name__ == "__main__":
    client = AuthenticationClient(AuthenticationService())
    client.run()
