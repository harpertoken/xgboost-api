# Release Process

This document describes the release process for the XGBoost API project.

## Version Numbering

We follow [Semantic Versioning](https://semver.org/):

- MAJOR version for incompatible API changes
- MINOR version for backwards-compatible functionality additions
- PATCH version for backwards-compatible bug fixes

## Release Steps

1. Ensure all tests pass and the main branch is stable.

2. Update CHANGELOG.md with the new version's changes.

3. Run the release script:
```bash
# First do a dry run
python scripts/release.py --version X.Y.Z --dry-run

# If everything looks good, run the actual release
python scripts/release.py --version X.Y.Z
```

4. Follow the instructions printed by the release script.

5. Create a GitHub release:
   - Go to GitHub Releases
   - Create a new release using the tag
   - Copy the relevant section from CHANGELOG.md
   - Attach any additional artifacts if needed

## Release Artifacts

Each release includes:

1. Git tag in the format `vX.Y.Z`
2. Docker image tagged as `bniladridas/flask-xgboost-api:X.Y.Z`
3. Updated Kubernetes deployment configurations
4. Updated documentation

## Post-Release

1. Verify the deployment works in a staging environment
2. Monitor the production deployment
3. Update any relevant documentation websites
4. Announce the release in appropriate channels

## Hotfix Process

For urgent fixes to a release:

1. Create a hotfix branch from the release tag
2. Make the necessary fixes
3. Follow the regular release process with a patch version increment

## Creating a New Release

To create a new release, follow these detailed steps:

1. **Prepare the Release:**
   - Ensure all changes are committed and pushed to the main branch.
   - Run all tests to ensure the codebase is stable.

2. **Update Version:**
   - Update the version number in the `VERSION` file.
   - Update the version number in the `Dockerfile` and Kubernetes deployment configurations.

3. **Update Documentation:**
   - Update `CHANGELOG.md` with the new version's changes.
   - Update any other relevant documentation files.

4. **Run Release Script:**
   - Perform a dry run of the release script:
     ```bash
     python scripts/release.py --version X.Y.Z --dry-run
     ```
   - If the dry run is successful, run the actual release script:
     ```bash
     python scripts/release.py --version X.Y.Z
     ```

5. **Create GitHub Release:**
   - Go to GitHub Releases.
   - Create a new release using the tag created by the release script.
   - Copy the relevant section from `CHANGELOG.md` into the release description.
   - Attach any additional artifacts if needed.

6. **Deploy to Kubernetes:**
   - Apply the updated Kubernetes deployment configurations:
     ```bash
     kubectl apply -f kubernetes/deployment.yaml
     kubectl apply -f kubernetes/service.yaml
     ```

7. **Post-Release Verification:**
   - Verify the deployment works in a staging environment.
   - Monitor the production deployment for any issues.
   - Update any relevant documentation websites.
   - Announce the release in appropriate channels.
