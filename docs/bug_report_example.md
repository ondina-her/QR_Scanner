# Bug Report

# QR scanner fails to decode QR code smaller than 5 cm
## Bug Summary
- **Title:** Scanner app fails to decode small size QR code 
- **Date:** 5 August 2026
- **Reporter:** Ondina Hernandez

## Environment:
- **OS:** Microsoft Windows 11 LAPTOP
- **Hardware/Camera:** Integrated camera USB\VID_174F&PID_2469&REV_0007&MI_00
- **Lightning:** Testing was conducted under average daylight/regulated LED light source 
- **Target media:** Printed paper(3 cm) 

## Severity and Priority
- **Severity:** High
- **Priority:** High

## Description
- QR scanner fails to decode a QR code that are less than 5 cm. 

## Steps to Reproduce
1. Open the application.
2. Click button Start scanner 
3. Allow camera permissions.
4. Align camera with any printers QR code less than 5 cm.

## Expected Result
- The application should successfully parse the payload and display the url or text or other on placeholder.

## Actual Result
- The frame doesn't capture the code and display nothing. 

## Evidence
- ![app_imageBR1](report_Images/app_imageBR1.png)
- ![terminal_imageBR1](report_Images/terminal_imageBR1.png)

## Impact
- Users cannot visually confirm that a QR code has been detected.

## Status
- **Open**


# QR scanner fails to decode blurry QR codes 
## Bug Summary
- **Title:** Scanner app fail to decode blurry QR code 
- **Date:** 5 August 2026
- **Reporter:** Ondina Hernandez

## Environment:
- **OS:** Microsoft Windows 11 LAPTOP
- **Hardware/Camera:** Integrated camera USB\VID_174F&PID_2469&REV_0007&MI_00
- **Lightning:** Testing was conducted under average daylight/regulated LED light source 
- **Target media:** Printed QR code 

## Severity and Priority
- **Severity:** High
- **Priority:** High

## Description
- QR scanner fails to decode a QR code that seem blurry at first sight. 

## Steps to Reproduce
1. Open the application.
2. Click button Start scanner 
3. Allow camera permissions.
4. Align camera with any printed QR code that seem blurry at first sight.

## Expected Result
- The application should successfully parse the payload and display the url or text or other on placeholder.

## Actual Result
- The frame doesn't capture the code and display nothing. 

## Evidence
- ![app-imageBR2](report_Images/app_imageBR2.png)
- ![terminal-imageBR2](report_Images/terminal_imageBR2.png)

## Impact
- User cannot visually confirm that a QR code has been detected.

## Status
- **Open**

# QR detection bounding box is not displayed on the camera overlay
## Bug Summary
- **Title:** Scanner app fail to show bounding box on camera overlay
- **Date:** 8 August 2026
- **Reporter:** Ondina Hernandez

# Environment:
- **OS:** Microsoft Windows 11 LAPTOP
- **Hardware/Camera:** Integrated camera USB\VID_174F&PID_2469&REV_0007&MI_00
- **Lightning:** Testing was conducted under average daylight/regulated LED light source 
- **Target media:** Printed paper(~10 cm) 

## Severity and Priority
- **Severity:** Minor
- **Priority:** Medium

## Description
-  Missing QR code detection bounding box on camera overlay.

## Steps to Reproduce
1. Open the application.
2. Click button Start scanner 
3. Allow camera permissions.
4. Align camera with any printers QR code.

## Expected Result
- The green or white box around QR code in real time.

## Actual Result
- The stream shows no visual marker when a QR code is in view.

## Evidence
- ![app-imageBR3](report_Images/app_imageBR3.png)
- ![terminal-imageBR3](report_Images/terminal_imageBR3.png)

## Impact
- Users can't visually confirm that a bounding box on the camera overlay.

## Status
- **Open**
