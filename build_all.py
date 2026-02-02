#!/usr/bin/env python3
"""
Build all placeholder packages.
"""

import subprocess
import sys
from pathlib import Path

PACKAGES = ["toy_package_a", "toy_package_b"]


def build_package(package_name):
    """Build a single package."""
    package_dir = Path(package_name)

    if not package_dir.exists():
        print(f"[ERROR] Package directory {package_name} does not exist!")
        return False

    print(f"\n[BUILD] Building {package_name}...")

    try:
        result = subprocess.run(
            [sys.executable, "-m", "build"],
            cwd=package_dir,
            capture_output=True,
            text=True,
        )

        if result.returncode == 0:
            print(f"[OK] Successfully built {package_name}")
            return True
        else:
            print(f"[ERROR] Failed to build {package_name}")
            print(result.stderr)
            return False

    except Exception as e:
        print(f"[ERROR] Exception while building {package_name}: {e}")
        return False


def main():
    """Build all packages."""
    print("=" * 60)
    print("Building all toy packages")
    print("=" * 60)

    # Check if build module is available
    try:
        import build
    except ImportError:
        print("\n[ERROR] 'build' module not found. Please install it:")
        print("  pip install build")
        sys.exit(1)

    success_count = 0
    failed_packages = []

    for package in PACKAGES:
        if build_package(package):
            success_count += 1
        else:
            failed_packages.append(package)

    print("\n" + "=" * 60)
    print(f"Build Summary: {success_count}/{len(PACKAGES)} successful")
    print("=" * 60)

    if failed_packages:
        print("\n[FAILED] The following packages failed to build:")
        for pkg in failed_packages:
            print(f"  - {pkg}")
        sys.exit(1)
    else:
        print("\n[OK] All packages built successfully!")
        print("\nNext steps:")
        print("  Review the packages and upload to PyPI using:")
        print("  python upload_all.py")


if __name__ == "__main__":
    main()
