from ai.profiles.casual import (
    CasualProfile
)

from ai.profiles.professional import (
    ProfessionalProfile
)

from config.settings import (
    DEFAULT_PROFILE
)


class ProfileFactory:

    @staticmethod
    def create():

        if DEFAULT_PROFILE == "casual":
            return CasualProfile()

        if DEFAULT_PROFILE == "professional":
            return (
                ProfessionalProfile()
            )

        raise ValueError(
            "Invalid profile"
        )