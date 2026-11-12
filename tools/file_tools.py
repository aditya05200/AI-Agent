"""
File-related tools available to the agent.
"""

import os

from config.logger import logger


def list_files() -> str:
    """
    List all files and directories in the current folder.

    Returns:
        Directory contents as a formatted string.
    """
    logger.info(
        "Listing files from current directory"
    )

    files = os.listdir(".")

    return "\n".join(files)


def read_file(filename: str) -> str:
    """
    Read a file from disk.

    Args:
        filename: Name of the file to read.

    Returns:
        File contents or an error message.
    """
    logger.info(
        "Reading file: %s",
        filename
    )

    try:
        with open(
            filename,
            mode="r",
            encoding="utf-8"
        ) as file:
            return file.read()

    except FileNotFoundError:

        logger.warning(
            "File not found: %s",
            filename
        )

        return (
            f"File not found: {filename}"
        )

    except Exception as error:

        logger.error(
            "Unexpected file read error: %s",
            error
        )

        return (
            f"Unexpected error while reading "
            f"{filename}"
        )