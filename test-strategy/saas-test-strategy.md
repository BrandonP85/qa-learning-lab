# QA Portfolio Test Strategy

**Author:** Brandon P.  
**Version:** 1.0  
**Last Updated:** 2026  
**Status:** Active

---

## 1. Overview

This document outlines the test strategy applied across the manual QA portfolio contained in this repository. It defines the scope, objectives, methodology, tooling, and defect classification framework used throughout the testing effort.

Testing was conducted against two publicly accessible web applications selected for their complexity, real-world relevance, and suitability for demonstrating core QA competencies.

---

## 2. Applications Under Test

| Application | URL | Purpose |
|---|---|---|
| OpenCart Demo | https://demo.opencart.com | Full-featured e-commerce platform; realistic SaaS environment |
| The Internet | https://the-internet.herokuapp.com | Purpose-built QA practice application with intentional and unintentional defects |

OpenCart was selected as the primary target due to its realistic e-commerce feature set — authentication, navigation, product management, cart, and checkout flows — closely mirroring production SaaS environments. The Internet was selected to complement OpenCart with a broader range of UI patterns and edge case scenarios.

---

## 3. Objectives

- Demonstrate structured manual test case authoring across happy path, negative, and edge case scenarios
- Identify and document defects using industry-standard bug report format
- Apply consistent severity and priority classification to all findings
- Surface UX and validation deficiencies beyond strict functional failures
- Build a reproducible, well-documented testing artifact suitable for professional review

---

## 4. Scope

### In Scope

**OpenCart Demo**
- User authentication: registration, login, logout
- Form validation: required fields, email format, password requirements
- Navigation: menu structure, internal linking, page routing
- UI consistency: element visibility, labeling, interactive feedback

**The Internet**
- Navigation and link integrity
- Page load behavior and resource handling
- Interactive UI elements: hovers, disappearing elements
- Form functionality: password recovery flow
- Dynamic content behavior

### Out of Scope

- Payment processing and transaction flows (demo environment limitation)
- Backend/API testing
- Performance and load testing
- Accessibility (WCAG) compliance testing
- Mobile native application testing
- Automated regression testing (in progress — see repository roadmap)

---

## 5. Test Types Applied

| Test Type | Description |
|---|---|
| **Happy Path** | Validates core user flows under ideal conditions with valid inputs |
| **Negative Testing** | Validates system behavior under invalid, missing, or malformed inputs |
| **Edge Case Testing** | Probes boundary conditions and non-obvious failure points |
| **Exploratory Testing** | Unscripted investigation of application behavior with logged observations |

---

## 6. Entry and Exit Criteria

### Entry Criteria
- Target application is accessible and responsive
- Test environment (browser, OS) is documented
- Test cases are written and reviewed prior to execution

### Exit Criteria
- All planned test cases executed with documented results
- All identified defects logged with full reproduction steps and evidence
- No Critical or High severity defects left unresolved without documentation

---

## 7. Risk Areas and Prioritization

Testing effort was prioritized based on user impact and defect likelihood:

| Risk Area | Rationale |
|---|---|
| Authentication flows | High user impact; security and data integrity implications |
| Form validation | Common source of UX failure; affects conversion and user trust |
| Navigation and routing | Broken links and 404 errors directly degrade user experience |
| Dynamic content behavior | Non-deterministic features require careful observation |
| Infrastructure stability | Demo environments introduce server-level failure risk |

---

## 8. Defect Classification

### Severity
Measures the technical impact of the defect on the application.

| Level | Definition |
|---|---|
| **Critical** | Application is unusable; core functionality completely broken |
| **High** | Major feature broken; significant user impact; no workaround |
| **Medium** | Feature partially broken or behaving incorrectly; workaround exists |
| **Low** | Minor issue; cosmetic defect or UX inconsistency; minimal user impact |

### Priority
Measures the urgency of resolution from a business perspective.

| Level | Definition |
|---|---|
| **High** | Must be fixed immediately; blocking users or revenue |
| **Medium** | Should be fixed in current or next release cycle |
| **Low** | Can be scheduled for a future release without significant impact |

> Note: Severity and Priority are assessed independently. A low-severity cosmetic defect on a high-traffic page may carry Medium or High priority due to business impact.

---

## 9. Tools and Environment

| Tool | Purpose |
|---|---|
| Chrome (v148) | Primary test browser |
| Chrome DevTools | Console error capture, network monitoring, element inspection |
| GitHub | Test artifact documentation and version control |
| Markdown | Test case and bug report authoring format |

---

## 10. Defect Summary

| ID | Title | Application | Severity | Priority | Status |
|---|---|---|---|---|---|
| BUG-OC-001 | Empty field submission generates generic auth error | OpenCart | Medium | Low | New |
| BUG-OC-002 | No inline validation on password field during registration | OpenCart | Low | Low | New |
| BUG-OC-003 | Unresponsive navigation buttons on Manufacturer page | OpenCart | Medium | Medium | New |
| BUG-OC-004 | Subcategory item counts do not match parent category total | OpenCart | Medium | Low | New |
| BUG-OC-005 | 522 Connection Timeout — demo site fully unresponsive | OpenCart | Critical | High | New |
| BUG-TI-001 | 404 error on Contact Us page | The Internet | Medium | Medium | New |
| BUG-TI-002 | Typos page not randomizing on reload | The Internet | Medium | Low | New |
| BUG-TI-003 | Slow Resources page returns 503 — element never loads | The Internet | Low | Low | New |
| BUG-TI-004 | 404 error on View Profile links in Hovers page | The Internet | Low | Low | New |
| BUG-TI-005 | Internal Server Error on Forgot Password flow | The Internet | Medium | Low | New |

---

## 11. Out of Scope — Future Testing Roadmap

- Automated test suite using Playwright and Python
- API testing with Postman
- LLM exploratory testing documentation
- Expanded checkout and cart flow coverage
- Cross-browser compatibility testing

