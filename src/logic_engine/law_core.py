"""
Law Core Module

Defines the Law class for the programmable rule framework, including metadata,
versioning, ethical validation, and logging for transparent, audit-able rule application.
"""
import uuid
import logging
from typing import Callable, Dict, Any
from advanced_modules.ethics_firewall import EthicsFirewall

# Configure module logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

class Law:
    """
    Represents a transformation rule applied to the simulation context.
    Attributes:
      - id: unique identifier for auditing
      - name: human-readable law name
      - description: purpose of the law
      - activation_func: function that transforms context
      - author: creator identifier
      - version: semantic version string
      - metadata: arbitrary key/value store
    """
    def __init__(
        self,
        name: str,
        description: str,
        activation_func: Callable[[Dict[str, Any]], Dict[str, Any]],
        author: str = None,
        version: str = "1.0.0",
        metadata: Dict[str, Any] = None
    ):
        self.id = f"law-{uuid.uuid4().hex}"
        self.name = name
        self.description = description
        self.activation_func = activation_func
        self.author = author or "unknown"
        self.version = version
        self.metadata = metadata or {}
        self._ethics = EthicsFirewall()

        # Ethical self-check at registration
        if not self._ethics.check_law(self):
            raise ValueError(f"Law '{self.name}' violates ethics rules.")
        logger.info(f"Law initialized: {self.name} (v{self.version}) by {self.author}")

    def apply(self, context: Dict[str, Any]) -> Dict[str, Any]:
        """
        Apply the activation function to a copy of the context and return the new context.
        """
        logger.debug(f"Applying law {self.name} (v{self.version})")
        new_ctx = context.copy()
        try:
            result = self.activation_func(new_ctx)
            if not isinstance(result, dict):
                raise TypeError("Activation function must return a dict context")
            return result
        except Exception as e:
            logger.error(f"Law '{self.name}' application error: {e}")
            raise

    def update_version(self, new_version: str):
        """
        Update the law's semantic version and log the change.
        """
        logger.info(f"Updating law {self.name} from v{self.version} to v{new_version}")
        self.version = new_version

    def to_dict(self) -> Dict[str, Any]:
        """
        Serialize law metadata for persistence or blockchain recording.
        """
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "author": self.author,
            "version": self.version,
            "metadata": self.metadata,
        }

__all__ = ["Law"]
