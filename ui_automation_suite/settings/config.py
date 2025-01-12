import os

from dotenv import load_dotenv

load_dotenv()


class AppEnvSettings:
    def __init__(self):
        self.standard_user = None
        self.locked_out_user = None
        self.problem_user = None
        self.performance_glitch_user = None
        self.error_user = None
        self.visual_user = None
        self.wrong_username = None
        self.initialize_usernames()

        self.password = None
        self.initialize_password()

    def initialize_usernames(self):
        self.standard_user = "standard_user"
        self.locked_out_user = "locked_out_user"
        self.problem_user = "problem_user"
        self.performance_glitch_user = "performance_glitch_user"
        self.error_user = "error_user"
        self.visual_user = "visual_user"
        self.wrong_username = "wrong_username"

    def initialize_password(self):
        self.password = os.getenv("PASSWORD")

    def get_username(self, username_type: str):
        """Fetch the username based on the provided type."""
        return getattr(self, username_type, None)
