import logging

import jwt
from fastapi import HTTPException, status

from config import token_algo, secret_key

logger = logging.getLogger(__name__)


def generate_token(user_details) -> str:
    """Generates token for user information based jwt library.
    :param user_details: user information provided by the user
    :return: str
    """
    try:
        # Generates the token with user information
        token = jwt.encode(user_details, secret_key, algorithm=token_algo)
        return token
    except Exception as err:
        logger.error(f"Error while generating the token and Error - {str(err)}")
        raise HTTPException(
            detail=f"Error while generating the token and Error - {str(err)}",
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )
