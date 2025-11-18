# Release Readiness Checklist

A practical checklist to make sure a release is truly ready for production.  
Use this for Go/No-Go meetings with Delivery, QE, DevOps, and Business stakeholders.

---

## 1. Release Information

- **Release name / version:** `<e.g., v2.5.0 – Customer Dashboard>`
- **Environment:** `<UAT / Pre-Prod / Production>`
- **Target deployment date:** `<DD-MMM-YYYY>`
- **Deployment window:** `<e.g., Friday 10 PM – Saturday 2 AM>`
- **Release owner:** `<Program / Delivery Manager>`
- **Rollback plan:** `<Yes/No – link or location>`

---

## 2. Functional Readiness ✅

| Item                                     | Status (✅/⚠️/❌) | Owner           | Notes |
|------------------------------------------|-------------------|-----------------|-------|
| All committed user stories completed     |                   |                 |       |
| Business acceptance criteria met         |                   |                 |       |
| Integration flows tested end-to-end      |                   |                 |       |
| UAT sign-off received                    |                   |                 |       |
| Non-functional requirements validated    |                   |                 |       |

> **Rule of thumb:** No **Critical** or **High** functional gaps allowed for Go.

---

## 3. Quality Gates ✅

| Item                                       | Status (✅/⚠️/❌) | Owner        | Notes |
|--------------------------------------------|-------------------|--------------|-------|
| **P1/P2 defects in UAT:** 0                |                   | QE Lead      |       |
| All Sev-3/4 defects have workarounds       |                   | QE Lead      |       |
| Regression suite executed                  |                   | QE Team      |       |
| Automation coverage above agreed target    |                   | QE Lead      |       |
| Performance / load tests passed            |                   | Perf Eng     |       |
| Security / vulnerability scan completed    |                   | Security     |       |

> **Critical rule:** If any **P1/P2** defect is open → **NO-GO**.

---

## 4. Deployment Readiness ✅

| Item                                        | Status (✅/⚠️/❌) | Owner   | Notes |
|---------------------------------------------|-------------------|---------|-------|
| Deployment runbook updated & reviewed       |                   | DevOps |       |
| Deployment steps dry-run in lower env       |                   | DevOps |       |
| Rollback steps documented and tested        |                   | DevOps |       |
| DB migrations / scripts tested in UAT       |                   | DBA    |       |
| Monitoring & alerts configured              |                   | DevOps |       |
| Logging / dashboards validated              |                   | DevOps |       |

---

## 5. Documentation & Training ✅

| Item                                   | Status (✅/⚠️/❌) | Owner         | Notes |
|----------------------------------------|-------------------|---------------|-------|
| User guides / help docs updated        |                   | Tech Writer   |       |
| Runbook / on-call handbook updated     |                   | DevOps / QE   |       |
| Known issues list created & shared     |                   | Program Mgr   |       |
| Support / L1 / L2 teams trained        |                   | Support Lead  |       |

---

## 6. Compliance & Risk ✅

| Item                                               | Status (✅/⚠️/❌) | Owner            | Notes |
|----------------------------------------------------|-------------------|------------------|-------|
| Regulatory / security checks completed             |                   | Compliance / Sec |       |
| Data privacy / PII handling validated              |                   | Security         |       |
| High-risk items have mitigation plans in place     |                   | Program / Risk   |       |

> Link this section with your **Risk Register** (Template 2.3).

---

## 7. Business Readiness ✅

| Item                                      | Status (✅/⚠️/❌) | Owner              | Notes |
|-------------------------------------------|-------------------|--------------------|-------|
| Key stakeholders informed of release      |                   | Program Manager    |       |
| Customer-facing communication prepared    |                   | Marketing / CSM    |       |
| Go-Live support window agreed             |                   | Program / Support  |       |
| Success criteria defined (KPIs / OKRs)    |                   | Product / Business |       |

---

## 8. Go / No-Go Decision Matrix 🚦

Fill this table right before the Go/No-Go call.

| Criteria                  | Weight      | Pass Threshold               | Status (Pass/Fail) | Comments |
|---------------------------|------------|------------------------------|--------------------|----------|
| Zero open P1/P2 defects   | **CRITICAL** | 100% met                     |                    |          |
| Performance benchmarks    | HIGH       | e.g., p95 < 3s               |                    |          |
| Regulatory/compliance OK  | **CRITICAL** | All checks green             |                    |          |
| UAT / Business sign-off   | **CRITICAL** | Formal approval received     |                    |          |
| Support readiness         | MEDIUM     | Training completed           |                    |          |

**Decision: `GO` / `NO-GO`**

- **If any CRITICAL criterion fails → NO-GO**  
- Document who made the decision and why.

**Sign-off:**

- Program / Delivery Manager: __________________  Date: ________  
- QE / Quality Lead: ___________________________  Date: ________  
- Product / Business Owner: ____________________  Date: ________  
- CTO / CIO / CXO (if applicable): _____________  Date: ________
