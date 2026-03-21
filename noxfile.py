#!/usr/bin/env -S uv run --script

# /// script
# dependencies = ["nox"]
# ///

"""Nox configuration."""

from __future__ import annotations

import os

import nox

PYPROJECT = nox.project.load_toml("pyproject.toml")
PYTHON_VERSIONS = nox.project.python_versions(PYPROJECT)

nox.needs_version = ">=2026.02.09"
nox.options.default_venv_backend = "uv"
nox.options.reuse_venv = "yes"


@nox.session(python=PYTHON_VERSIONS)
def tests(session: nox.Session) -> None:
    """Execute pytest tests."""
    deps = ["pytest", "pytest-durations"]
    if "GITHUB_ACTIONS" in os.environ:
        deps.append("pytest-github-actions-annotate-failures")

    session.install(".")
    session.install(*deps)
    session.run("pytest", *session.posargs)


@nox.session
def typing(session: nox.Session) -> None:
    """Type checks."""
    session.install(".")
    session.install("mypy", "ty")
    session.run("mypy", "tap_geekbot", "tests")
    session.run("ty", "check", "tap_geekbot", "tests")


if __name__ == "__main__":
    nox.main()
