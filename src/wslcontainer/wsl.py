"""WSL (Windows Subsystem for Linux) command utilities."""

import subprocess


def run_wsl_help() -> "subprocess.CompletedProcess[str]":
    """Run ``wsl --help`` and return the completed process result.

    Returns:
        subprocess.CompletedProcess: The result of the ``wsl --help`` command.

    Raises:
        FileNotFoundError: If the ``wsl`` executable is not found on the system.
    """
    return subprocess.run(
        ["wsl", "--version"],
        capture_output=True,
        text=True,
        check=False,
        encoding="locale",
        errors="replace",
    )


def is_wsl_available() -> bool:
    """Check whether WSL is available on the current system.

    Executes ``wsl --help`` and returns ``True`` if the command succeeds,
    ``False`` otherwise (e.g. WSL is not installed or the executable is not
    found in *PATH*).

    Returns:
        bool: ``True`` if WSL is available, ``False`` if not.
    """
    try:
        result = run_wsl_help()
        return result.returncode == 0
    except FileNotFoundError:
        return False
