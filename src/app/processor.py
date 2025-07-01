"""Processor module for stock-backtest-correlation backtest signal.

This module validates incoming messages and computes a derived signal
based on the input data. All operations are logged for observability.
"""

from typing import Any

from app.utils.setup_logger import setup_logger
from app.utils.types import ValidatedMessage
from app.utils.validate_data import validate_message_schema

logger = setup_logger(__name__)


def validate_input_message(message: dict[str, Any]) -> ValidatedMessage:
    """Validate the incoming raw message against the expected schema.

    Parameters:
        message (dict[str, Any]): The raw message payload.

    Returns:
        ValidatedMessage: A validated message object.
    """
    logger.debug("🔍 Validating message schema...")
    if not validate_message_schema(message):
        logger.error("❌ Message schema invalid: %s", message)
        raise ValueError("Invalid message format")
    return message  # type: ignore[return-value]


def compute_signal(message: ValidatedMessage) -> dict[str, Any]:
    """Compute a backtest signal from the validated input message.

    This function is a placeholder. Replace with strategy-specific logic.

    Parameters:
        message (ValidatedMessage): The validated input data.

    Returns:
        dict[str, Any]: The enriched output data.
    """
    logger.info("⚙️ Computing backtest signal...")
    signal = {"signal": "HOLD", "confidence": 0.5}  # placeholder logic
    logger.debug("✅ Computed signal: %s", signal)
    return {**message, **signal}
