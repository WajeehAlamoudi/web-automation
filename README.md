
# Automated Video Playback using Selenium

## Overview
This script automates video playback on Khan Academy using an existing Chrome session with **remote debugging** enabled. It navigates to specific video URLs, plays them, and waits for pre-defined durations.

---

## Prerequisites

1. **Google Chrome** must be installed.
2. **Python** (ensure it is added to your system PATH).
3. **Selenium** library. Install using:
   ```bash
   pip install selenium

## Setup Instructions
- Ensure prot you write in cmd matches the port in your python code.
- Make an outside directory for each port to save logs and other things there.
1. Open Command Prompt (as Administrator if needed).
2. Navigate to the Chrome application folder:
```cmd
cd C:\Program Files\Google\Chrome\Application\
```
Run Chrome with remote debugging enabled with specific folder key:
```cmd
"C:\Program Files\Google\Chrome\Application\chrome.exe" --remote-debugging-port=1980 --user-data-dir="C:\Users\wajee\chrome-automationKEYS\chromeKEY1980"

```
- Explanation:
```--remote-debugging-port=1980```: Enables Chrome debugging on port 1980.

```--user-data-dir```: Specifies the Chrome user data directory.

You can modify the 1980 port and chromeKEY1980 directory path if needed.
## Run the Script
1. Save the Python code.
2. adjust the urls and it's min durations (round up if needed).
- like 3min and 17sec = 180sec + 20sec = 200 sec.

## How It Works
Connects to an existing Chrome session using remote debugging.

Navigates to Khan Academy videos.

Waits for the play button and clicks it.

Plays each video for a specified duration:

- Video 1: 240 seconds
- Video 2: 420 seconds

# Note:
if your google account is not logged in, login to your google accout to not face khan Academy log in errors.
- if you logged in your google account the url navigator will directly opens khan Academy with your entered account.
- not recommended to use it fro skipping lectures unless you understand the subject.
