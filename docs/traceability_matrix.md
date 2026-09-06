
## Traceability matrix

| Requirement ID | Requirement description | Evidence | Test case ID | Tool / Method | Status | Evidence |
|---|---|---|---|---|---|---|
| R1 | App decodes valid QR code | STQC-6 | Functional/UI | Selenium | Failed | Bug 001 |
| R2 | Scanner UI must allow user to start scanning| STQC‑9 | UI | Selenium | Passed | test_qr_code.py |
| R3 | APP must reject invalid QR codes | STQC-7 | Functional/UI | Selenium | Passed | test_qr_code.py |
| R4 | App handles empty input | STQC-8 | Negative/UI | Selenium | Passed | test_qr_code.py |
| R5 | API creates an item correctly | API-1 | API | Postman | Passed | Postman |
| R6 | API creates a Linked scan | API-2 | API | Postman | Passed | Postman |
| R7 | API rejectS invalid input | API-3/API-4 | Negative/API | Postman | Passed | Postman |
| R8 | API must handle multiple users concurrently | PERF-1 | Performance | JMeter | Passed | JMeter report |
