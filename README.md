<div align="center">

# `tap-geekbot`

<div>
  <a href="https://results.pre-commit.ci/latest/github/reservoir-data/tap-betterstack/main">
    <img alt="pre-commit.ci status" src="https://results.pre-commit.ci/badge/github/reservoir-data/tap-betterstack/main.svg"/>
  </a>
  <a href="https://github.com/reservoir-data/tap-betterstack/blob/main/LICENSE">
    <img alt="License" src="https://img.shields.io/github/license/reservoir-data/tap-betterstack"/>
  </a>
  <a href="https://github.com/astral-sh/ruff">
    <img src="https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/charliermarsh/ruff/main/assets/badge/v2.json" alt="Ruff" style="max-width:100%;">
  </a>
  <a href="https://pypi.org/p/tap-geekbot/">
    <img alt="Python versions" src="https://img.shields.io/pypi/pyversions/tap-geekbot"/>
  </a>
</div>

Singer tap for [Geekbot](https://geekbot.com/).

Built with the [Meltano Tap SDK](https://sdk.meltano.com) for Singer Taps.

</div>

## Capabilities

* `catalog`
* `state`
* `discover`
* `about`
* `stream-maps`

## Settings

- [ ] `Developer TODO:` Declare tap settings here.

A full list of supported settings and capabilities is available by running: `tap-geekbot --about`

### Source Authentication and Authorization

- [ ] `Developer TODO:` If your tap requires special access on the source system, or any special authentication requirements, provide those here.

## Usage

You can easily run `tap-geekbot` by itself or in a pipeline using [Meltano](https://meltano.com/).

### Executing the Tap Directly

```bash
tap-geekbot --version
tap-geekbot --help
tap-geekbot --config CONFIG --discover > ./catalog.json
```

## Developer Resources

- [ ] `Developer TODO:` As a first step, scan the entire project for the text "`TODO:`" and complete any recommended steps, deleting the "TODO" references once completed.

### Initialize your Development Environment

```bash
pipx install poetry
poetry install
```

### Create and Run Tests

Create tests within the `tests` subfolder and then run:

```bash
poetry run pytest
```

You can also test the `tap-geekbot` CLI interface directly using `poetry run`:

```bash
poetry run tap-geekbot --help
```

### Testing with [Meltano](https://www.meltano.com)

_**Note:** This tap will work in any Singer environment and does not require Meltano.
Examples here are for convenience and to streamline end-to-end orchestration scenarios._

Your project comes with a custom `meltano.yml` project file already created. Open the `meltano.yml` and follow any _"TODO"_ items listed in
the file.

Next, install Meltano (if you haven't already) and any needed plugins:

```bash
# Install meltano
pipx install meltano
# Initialize meltano within this directory
cd tap-geekbot
meltano install
```

Now you can test and orchestrate using Meltano:

```bash
# Test invocation:
meltano invoke tap-geekbot --version
# OR run a test `elt` pipeline:
meltano elt tap-geekbot target-jsonl
```

### SDK Dev Guide

See the [dev guide](https://sdk.meltano.com/en/latest/dev_guide.html) for more instructions on how to use the SDK to
develop your own taps and targets.
