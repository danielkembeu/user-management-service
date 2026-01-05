from typing import Any, Dict
from fastapi import status


def generate_response_message(
    status_code: int = status.HTTP_404_NOT_FOUND,
    msg: str | None = None,
) -> Dict[int | str, Dict[str, Any]] | None:
    """
    Generates a FastAPI response model documentation mapping for error responses.

    Args:
        status_code (int): HTTP status code (default: 404).
        msg (str | None): Custom error message.

    Returns:
        dict[int | str, dict[str, Any]] | None: Response documentation for FastAPI route decorators.
    """
    return {
        status_code: {
            "description": msg if msg else "Aucune information enregistrée",
            "content": {
                "application/json": {
                    "example": {"detail": {"message": msg if msg else "Aucune information enregistrée"}}
                }
            },
        }
    }


def generate_multiple_response_messages(
    messages: Dict[int, str | None]
) -> Dict[int, Dict[str, Any]]:
    """
    Generate response documentation supporting multiple status codes and messages
    for use in FastAPI route decorators.

    Args:
        messages (dict[int, str | None]): A dictionary mapping status codes to messages.

    Returns:
        dict[int, dict[str, Any]]: Response documentation with multiple status codes/messages.

    Example:
        responses=generate_multiple_response_messages({
            404: "Not found",
            400: "Bad request",
            401: None
        })
    """
    result = {}

    for status_code, msg in messages.items():
        description = msg if msg else "Aucune information enregistrée"
        result[status_code] = {
            "description": description,
            "content": {
                "application/json": {
                    "example": {"detail": {"message": description}}
                }
            }
        }
    return result
