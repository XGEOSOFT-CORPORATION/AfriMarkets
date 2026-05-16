# ==============================================================================
# AfriMarkets — setup.py
#
# Legacy setup script kept for backward compatibility with older pip versions
# and editable installs (pip install -e .).
#
# All canonical metadata and configuration live in pyproject.toml.
# This file should remain minimal.
# ==============================================================================

from __future__ import annotations

import sys
from pathlib import Path

from setuptools import find_packages, setup

# ------------------------------------------------------------------------------
# Python version guard
# ------------------------------------------------------------------------------
if sys.version_info < (3, 9):
    raise SystemExit(
        "AfriMarkets requires Python 3.9 or higher. "
        f"You are running Python {sys.version_info.major}.{sys.version_info.minor}."
    )

# ------------------------------------------------------------------------------
# Read long description from README
# ------------------------------------------------------------------------------
HERE = Path(__file__).parent
long_description = (HERE / "README.md").read_text(encoding="utf-8")

# ------------------------------------------------------------------------------
# Read runtime dependencies from requirements.txt
# (kept in sync with pyproject.toml [project.dependencies])
# ------------------------------------------------------------------------------
def _parse_requirements(path: str) -> list[str]:
    """Parse a requirements.txt, skipping comments and blank lines."""
    reqs = []
    for line in Path(path).read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if line and not line.startswith("#"):
            reqs.append(line)
    return reqs


install_requires = _parse_requirements("requirements.txt")

# ------------------------------------------------------------------------------
# setup()
# ------------------------------------------------------------------------------
setup(
    # ------------------------------------------------------------------
    # Identity
    # ------------------------------------------------------------------
    name             = "afrimarkets",
    version          = "0.1.0",
    description      = (
        "Unified access to historical and real-time data "
        "from African stock exchanges"
    ),
    long_description          = long_description,
    long_description_content_type = "text/markdown",

    # FIX 1 : licence déclarée comme string SPDX (plus de table TOML dépréciée)
    license          = "MIT",

    # ------------------------------------------------------------------
    # Authors
    # ------------------------------------------------------------------
    author       = (
        "Olabiyi Aurel Géoffroy Odjo, "
        "Koffi Frederic Sessie, "
        "Abdoul Oudouss Diakité, "
        "Steven P. Sanderson II"
    ),
    author_email = (
        "odjoaurel@gmail.com, "
        "koffisessie@gmail.com, "
        "abdouloudoussdiakite@gmail.com, "
        "spsanderson@gmail.com"
    ),
    maintainer       = "Olabiyi Aurel Géoffroy Odjo",
    maintainer_email = "odjoaurel@gmail.com",

    # ------------------------------------------------------------------
    # URLs
    # ------------------------------------------------------------------
    url          = "https://github.com/Koffi-Fredysessie/AfriMarkets-python",
    project_urls = {
        "Homepage"    : "https://github.com/Koffi-Fredysessie/AfriMarkets-python",
        "Bug Tracker" : "https://github.com/Koffi-Fredysessie/AfriMarkets-python/issues",
        "Repository"  : "https://github.com/Koffi-Fredysessie/AfriMarkets-python",
        "Changelog"   : "https://github.com/Koffi-Fredysessie/AfriMarkets-python/releases",
    },

    # ------------------------------------------------------------------
    # Package discovery
    # ------------------------------------------------------------------
    packages         = find_packages(
        exclude=["tests", "tests.*", "examples", "examples.*", "docs"]
    ),
    package_data     = {
        "afrimarkets": [
            "datasets/*.csv",
            "datasets/*.json",
            "py.typed",
        ]
    },
    include_package_data = True,

    # ------------------------------------------------------------------
    # Python & runtime requirements
    # ------------------------------------------------------------------
    python_requires  = ">=3.9",
    install_requires = install_requires,

    extras_require   = {
        "tensorflow": ["tensorflow>=2.12.0"],
        "torch"     : ["torch>=2.0.0"],

        "dev": [
            "pytest>=7.4.0",
            "pytest-cov>=4.1.0",
            "pytest-mock>=3.11.0",
            "black>=23.0.0",
            "flake8>=6.0.0",
            "flake8-bugbear>=23.0.0",
            "isort>=5.12.0",
            "mypy>=1.4.0",
            "pre-commit>=3.3.0",
            "sphinx>=7.0.0",
            "sphinx-rtd-theme>=1.3.0",
            "myst-parser>=2.0.0",
        ],

        "ci": [
            "pytest>=7.4.0",
            "pytest-cov>=4.1.0",
            "black>=23.0.0",
            "flake8>=6.0.0",
        ],
    },

    # ------------------------------------------------------------------
    # PyPI classifiers
    # FIX 2 : classifier "License :: OSI Approved :: MIT License" retiré
    #          (déprécié depuis setuptools >= 77 — la licence est déjà
    #           déclarée via license = "MIT" ci-dessus)
    # ------------------------------------------------------------------
    classifiers = [
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Intended Audience :: Financial and Insurance Industry",
        "Intended Audience :: Science/Research",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Topic :: Office/Business :: Financial",
        "Topic :: Office/Business :: Financial :: Investment",
        "Topic :: Scientific/Engineering :: Information Analysis",
        "Typing :: Typed",
    ],

    keywords = (
        "africa stock market finance BRVM NGX JSE GSE "
        "financial-data OHLCV trading portfolio time-series"
    ),

    zip_safe = False,
)