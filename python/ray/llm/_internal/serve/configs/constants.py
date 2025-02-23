import os

ALLOW_NEW_PLACEMENT_GROUPS_IN_DEPLOYMENT = int(
    os.getenv("RAYLLM_ALLOW_NEW_PLACEMENT_GROUPS_IN_DEPLOYMENT", "1")
)


# Timeout before download in multiplex deployment fails. <=0 means no timeout.
DEFAULT_MULTIPLEX_DOWNLOAD_TIMEOUT_S = float(
    os.getenv("DEFAULT_MULTIPLEX_DOWNLOAD_TIMEOUT_S", "30")
)
if DEFAULT_MULTIPLEX_DOWNLOAD_TIMEOUT_S <= 0:
    DEFAULT_MULTIPLEX_DOWNLOAD_TIMEOUT_S = None


# Number of retries for downloading a model in multiplex deployment.
DEFAULT_MULTIPLEX_DOWNLOAD_TRIES = int(
    os.getenv("DEFAULT_MULTIPLEX_DOWNLOAD_RETRIES", "3")
)

DEFAULT_TARGET_ONGOING_REQUESTS = 16

FALLBACK_MAX_ONGOING_REQUESTS = 64
