# GitHub Secrets Setup Guide

This document explains how to configure GitHub secrets for the CI/CD pipeline.

## Required Secrets

To set up the GitHub Actions CI/CD pipeline, you'll need to configure the following secrets in your GitHub repository:

### 1. Database Secrets
- `POSTGRES_PASSWORD`: The PostgreSQL password for testing environment
  - Value: A secure password for your test database (can be different from production)

### 2. Docker Hub Secrets (for image publishing)
- `DOCKER_USERNAME`: Your Docker Hub username
- `DOCKER_PASSWORD`: Your Docker Hub password or access token

## How to Add GitHub Secrets

1. Go to your GitHub repository
2. Click on **Settings** tab
3. In the left sidebar, click **Secrets and variables** → **Actions**
4. Click **New repository secret**
5. Add each secret with the name and value specified above

## Example Secret Values

```bash
# For testing - you can use a simple password
POSTGRES_PASSWORD=test_password_123

# Docker Hub credentials
DOCKER_USERNAME=your_dockerhub_username
DOCKER_PASSWORD=your_dockerhub_password_or_token
```

## Notes

- **POSTGRES_PASSWORD**: This is used for the test database in GitHub Actions. It doesn't need to match your local development password.
- **Docker Secrets**: Only required if you want to push images to Docker Hub. You can remove the docker job from the workflow if not needed.
- **Security**: Never commit actual passwords to your repository. Always use GitHub secrets for sensitive information.

## Optional: Skip Docker Push

If you don't want to publish Docker images, you can remove or comment out the entire `docker` job in `.github/workflows/ci-cd.yml`.

## Testing the Pipeline

After setting up the secrets:

1. Push your code to the `main` or `develop` branch
2. Check the **Actions** tab in your GitHub repository
3. Monitor the pipeline execution

The pipeline will:
- Run code quality checks (pre-commit hooks)
- Execute unit tests with coverage
- Run integration tests with Docker
- Perform security scans
- Build and push Docker images (if on main branch)
