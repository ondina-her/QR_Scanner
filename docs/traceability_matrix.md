
## Traceability matrix

| Requirement ID | Requirement Description | Test Case ID | Test Type | Tool / Method | Status | Evidence |
|---|---|---|---|---|---|---|
| R1 | App decodes valid QR code | STQC-6 | Functional/UI | Selenium | Failed | Bug 001 |
| R2 | Scanner UI must allow user to start scanning| STQC‑9 | UI | Selenium | Passed | ../Test/test_qr_code.py |
| R3 | APP must reject invalid QR codes | STQC-7 | Functional/UI | Selenium | Passed | ../Test/test_qr_code.py |
| R4 | App handles empty input | STQC-8 | Negative/UI | Selenium | Passed | ../Test/test_qr_code.py |
| R5 | API creates an item correctly | API-1 | API | Postman | Passed | ../Test/postman/qr_code_scann.postman_collection.json |
| R6 | API creates a Linked scan | API-2 | API | Postman | Passed | ../Test/postman/qr_code_scann.postman_collection.json |
| R7 | API rejectS invalid input | API-3/API-4 | Negative/API | Postman | Passed | ../Test/postman/qr_code_scann.postman_collection.json |
| R8 | API must handle multiple users concurrently | PERF-1 | Performance | JMeter | Passed | JMeter report |
| R9 | The UI displays a QR detection bounding box | STQC‑10 | UI | Selenium | Passed | ../Test/test_qr_code.py |
| R10 | An item can be updated | API-5 | API | Postman | Passed | ../Test/postman/qr_code_scann.postman_collection.json |
| R11 | An item can be deleted with its scans | API-6 | API | Postman | Passed | ../Test/postman/qr_code_scann.postman_collection.json |
| R12 | A scan can be deleted | API-7 | API | Postman | Passed | ../Test/postman/qr_code_scann.postman_collection.json |
