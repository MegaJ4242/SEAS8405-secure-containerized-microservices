
# Summary Report – Securing Containerized Microservices

## Steps Taken

The project began with the deployment of an intentionally vulnerable Flask-based microservice architecture using Docker Compose. The application was examined for common security flaws through manual code review and automated scanning. Following the discovery of multiple issues, the application and infrastructure were hardened to align with container security best practices.

The workflow included:
- Running and testing the vulnerable app locally using Docker Compose.
- Performing static code analysis using Bandit.
- Conducting a container image vulnerability scan using Trivy.
- Remediating insecure code patterns in `app.py`.
- Hardened the `Dockerfile` with a minimal base image, non-root user, and health checks.
- Enhanced the `docker-compose.yml` with security and resource limits.
- Documented threats using STRIDE, MITRE ATT&CK, and NIST control mappings.
- Created an architecture diagram to illustrate the improved deployment.

## Vulnerabilities Found and Fixed

### From Bandit:
- **Hardcoded password**: Moved to environment variable using `.env` file.
- **Command injection (`shell=True`)**: Replaced with `subprocess.run()` and IP validation.
- **Insecure `eval()` usage**: Replaced with `numexpr` for safe expression evaluation.
- **Flask binding to 0.0.0.0**: Restricted to appropriate interface per Docker context.

### From Trivy:
- Found 5 vulnerabilities in the container image:
  - High severity CVEs in `setuptools` and `sqlite-libs`
  - Medium severity CVE in `pip`
  - All addressed by updating `pip` and `setuptools` during the Docker build process.

## Architecture and How It Improves Security

The updated architecture implements:
- **Minimal base image (Alpine)** to reduce the attack surface.
- **Non-root user execution** to minimize privilege abuse.
- **`.env` configuration** to separate secrets from code.
- **Resource limits (`mem_limit`, `pids_limit`)** to prevent DoS attacks.
- **Security options** such as `read_only` and `no-new-privileges:true`.
- **Health checks** for container liveliness monitoring.

These changes collectively enhance confidentiality, integrity, and availability within the containerized environment.

## Reflection and Lessons Learned

This project demonstrated how even a simple microservice can harbor multiple critical security flaws if deployed without proper controls. By addressing both code-level and infrastructure-level risks, I gained hands-on experience implementing secure development and deployment practices. I also deepened my familiarity with threat modeling frameworks and container hardening techniques, which will inform future system architecture and DevSecOps initiatives.

Tools like Bandit, Trivy, and Docker security settings are now part of my secure coding checklist. A key takeaway was how interdependent application security and container security are—and how important it is to address both in tandem.
