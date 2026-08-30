# Test Execution Report

## Project
QR Code Scanner - QA Testing Portfolio Project

## Date
- 2026-08-09

## Tested By
- Ondina Hernández

## Scope
This report summarizes the test execution performed for the QR scanner application, including functional, UI, API, and performance testing activities.

## Test Environment
- Application: FastAPI QR scanner web app
- Browser: Chrome
- Tools: Selenium, pytest, Postman, JMeter
- Database: SQLite

## Test Cases Executed

| Test Case | Type | Status | Evidence / Notes |
|---|---|---|---|
| Valid QR scan | Functional / UI | Fail |See Test/postman/bug report example |
| Invalid QR scan | Functional / UI | Pass |See Test/test_qr_code.py |
| Empty input scan | Functional / UI | Pass |See Test/test_qr_code.py |
| UI validation | UI | Pass | See Test/test_qr_code.py |
| QR detection bounding box  | UI | Fail | See Test/test_qr_code.py |
| Create item via API | API | Pass |See Test/postman/qr_code_scann.postman_collection.json|
| Create scan via API | API | Pass |See Test/postman/qr_code_scann.postman_collection.json|
| Negative API case | API | Pass |See Test/postman/qr_code_scann.postman_collection.json|
| Performance Testing | API | Pass |See JMeter Performance Report|

## Bugs Found

| ID | Title | Severity | Status | Notes |
|---|---|---|---|---|
| BUG-001 | Scanner app fail to decode small size QR code | High | Open |See docs/bug_report_example.md |
| BUG-002 | Scanner app fail to decode blurry QR code | High | Open |See docs/bug_report_example.md |
| BUG-003 | Scanner app fail to show bounding box on camera overlay| Minor |Open |See docs/bug_report_example.md |

## Observations
- Web application need further fixes, regression testings, and retestings. 
- Not ready until the failed UI and QR decoding are investigated and retested.

## Overall Result
- Total test activities: 9 
- Test passed:  7 
- Test fail: 2
- Pass rate: 77.7%


