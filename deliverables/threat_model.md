
# Threat Model – Securing Containerized Microservices

## STRIDE Analysis

| Threat     | Example in App                         | Mitigation                                                                 |
|------------|----------------------------------------|----------------------------------------------------------------------------|
| **Spoofing** | No auth on endpoints                   | Limit network exposure, use `.env` for secrets                            |
| **Tampering** | User input used in command/eval       | Replaced `eval()` with `ast.literal_eval()` / `numexpr`; input validation |
| **Repudiation** | No logging of failed requests         | Could be improved with audit logs and structured logging                  |
| **Information Disclosure** | Errors return internal messages      | Exception handling improved; could add generic error messages             |
| **Denial of Service** | Unbounded input + no resource limits | `mem_limit`, `pids_limit`, input validation added                         |
| **Elevation of Privilege** | App ran as root                | Now runs as non-root user in Docker                                       |

## MITRE ATT&CK Mapping (Containers)

| ATT&CK Tactic       | Technique                          | Relevance                                            |
|---------------------|-------------------------------------|------------------------------------------------------|
| Initial Access      | T1190: Exploit Public-Facing App    | Unvalidated inputs on `/ping` and `/calculate`       |
| Execution           | T1203: Command & Scripting Interpreter | `eval()` and `subprocess` used insecurely           |
| Privilege Escalation | T1611: Escape to Host              | Mitigated by `USER`, `read_only`, `no-new-privs`     |
| Defense Evasion     | T1610: Deploy Container with Defaults | Fixed by restricting ports, using `.env`, etc.      |

## Vulnerability to Control Mapping (NIST 800-53)

| Vulnerability               | Mitigation Strategy                     | NIST 800-53 Control |
|----------------------------|------------------------------------------|---------------------|
| Hardcoded credentials      | Used `.env` files                        | AC-6, IA-5          |
| Command injection          | Removed `shell=True`, validated input    | SI-10, SI-3         |
| Use of `eval()`            | Replaced with `numexpr`                 | SI-10               |
| Run as root                | Changed to non-root Docker user          | CM-6, AC-6          |
| No input validation        | Added regex checks and error handling    | SI-10               |
