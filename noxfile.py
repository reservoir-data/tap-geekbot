"""Nox configuration."""

from __future__ import annotations

import os
import sys
from textwrap import dedent

import nox

try:
    from nox_poetry import Session, session
except ImportError:
    message = f"""\
    Nox failed to import the 'nox-poetry' package.
    Please install it using the following command:
    {sys.executable} -m pip install nox-poetry"""
    raise SystemExit(dedent(message)) from None

PYPROJECT = nox.project.load_toml("pyproject.toml")
PYTHON_VERSIONS = nox.project.python_versions(PYPROJECT)

nox.options.sessions = ("tests",)
nox.needs_version = ">=2024.5.1"
nox.options.default_venv_backend = "uv|virtualenv"
nox.options.sessions = (
    f"tests-{PYTHON_VERSIONS[-1]}",
    "typing",
)


@session(python=PYTHON_VERSIONS)
def tests(session: Session) -> None:
    """Execute pytest tests."""
    deps = ["pytest", "pytest-durations"]
    if "GITHUB_ACTIONS" in os.environ:
        deps.append("pytest-github-actions-annotate-failures")

    session.install(".")
    session.install(*deps)
    session.run("pytest", *session.posargs)


@session
def typing(session: Session) -> None:
    """Type checks."""
    session.install(".")
    session.install("mypy", "ty")
    session.run("mypy", "tap_geekbot", "tests")
    session.run("ty", "check", "tap_geekbot", "tests")
