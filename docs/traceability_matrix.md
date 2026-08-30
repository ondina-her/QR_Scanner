
## Traceability matrix

| Requirement ID | Requirement description | Test case ID | Tool / Method |
|---|---|---|---|
| R1| App must decode valid the QR code | STQC-6 | Postman(Happy path) |
| R2| Scanner UI must allow user to start scanning| STQC‑9  | Selenium (UI validation)|
| R3| The system must handle multiple users concurrently |  | JMeter(Load test with 20 threads) |
| R4| System must reject invalid QR codes | STQC-7/STQC-8 | Postman(Negative test with malformed QR) |
