#!/usr/bin/env python3
"""
Release management script for XGBoost API project.
"""

import argparse
import re
import subprocess
from pathlib import Path
from typing import Tuple

ROOT = Path(__file__).parent.parent

def get_current_version() -> str:
    """Read current version from VERSION file."""
    with open(ROOT / "VERSION", "r") as f:
        return f.read().strip()

def parse_version(version: str) -> Tuple[int, int, int]:
    """Parse version string into major, minor, patch components."""
    match = re.match(r"(\d+)\.(\d+)\.(\d+)", version)
    if not match:
        raise ValueError(f"Invalid version format: {version}")
    return tuple(map(int, match.groups()))

def update_version(new_version: str) -> None:
    """Update version in all necessary files."""
    try:
        # Update VERSION file
        with open(ROOT / "VERSION", "w") as f:
            f.write(new_version + "\n")
        
        # Update Dockerfile
        dockerfile_path = ROOT / "Dockerfile"
        with open(dockerfile_path, "r") as f:
            content = f.read()
        with open(dockerfile_path, "w") as f:
            f.write(content)
        
        # Update kubernetes deployments
        deployment_path = ROOT / "kubernetes" / "deployment.yaml"
        with open(deployment_path, "r") as f:
            content = f.read()
        content = re.sub(
            r"bniladridas/flask-xgboost-api:.*",
            f"bniladridas/flask-xgboost-api:{new_version}",
            content
        )
        with open(deployment_path, "w") as f:
            f.write(content)
    except Exception as e:
        print(f"Error updating version: {e}")
        raise

def create_release_branch(version: str) -> None:
    """Create and checkout a release branch."""
    branch_name = f"release-{version}"
    try:
        subprocess.run(["git", "checkout", "-b", branch_name], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error creating release branch: {e}")
        raise

def create_release_commit(version: str) -> None:
    """Create a release commit."""
    try:
        subprocess.run(["git", "add", "."], check=True)
        subprocess.run(["git", "commit", "-m", f"Release version {version}"], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error creating release commit: {e}")
        raise

def create_release_tag(version: str) -> None:
    """Create and push a release tag."""
    tag_name = f"v{version}"
    try:
        subprocess.run(["git", "tag", "-a", tag_name, "-m", f"Release {tag_name}"], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error creating release tag: {e}")
        raise

def build_and_push_docker(version: str) -> None:
    """Build and push Docker image."""
    image_name = f"bniladridas/flask-xgboost-api:{version}"
    try:
        subprocess.run(["docker", "build", "-t", image_name, "."], check=True)
        subprocess.run(["docker", "push", image_name], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error building and pushing Docker image: {e}")
        raise

def main() -> None:
    parser = argparse.ArgumentParser(description="Release management script")
    parser.add_argument(
        "--version",
        type=str,
        required=True,
        help="New version number (e.g., 1.0.1)"
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Perform a dry run without making changes"
    )
    args = parser.parse_args()

    current_version = get_current_version()
    new_version = args.version

    print(f"Current version: {current_version}")
    print(f"New version: {new_version}")

    if args.dry_run:
        print("Dry run - no changes will be made")
        return

    # Perform release steps
    update_version(new_version)
    create_release_branch(new_version)
    create_release_commit(new_version)
    create_release_tag(new_version)
    build_and_push_docker(new_version)

    print(f"""
Release {new_version} prepared successfully!

Next steps:
1. Push the release branch:
   git push origin release-{new_version}

2. Push the release tag:
   git push origin v{new_version}

3. Create a pull request from release-{new_version} to main

4. Deploy to Kubernetes:
   kubectl apply -f kubernetes/deployment.yaml
   kubectl apply -f kubernetes/service.yaml
""")

if __name__ == "__main__":
    main()
