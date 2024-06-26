import os
import warnings

warnings.filterwarnings("ignore", category=UserWarning, module="pydantic")

os.environ["OR_SITE_URL"] = "http://aider.chat"
os.environ["OR_APP_NAME"] = "Aider"

import litellm  # noqa: E402

litellm.success_callback = ["langfuse"]
litellm.failure_callback = ["langfuse"]

__all__ = [litellm]
