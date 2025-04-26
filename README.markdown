## Overview

A Python script (`sched.py`) that writes the current timestamp to `current_time.txt` every 5 minutes. It runs as a Windows service using WinSW and logs activity to `service.log`.

**Location**: `D:\College\Semester 6 (Magang)\Iseng\SERVICE SCHEDULER\`

## Requirements

- Windows OS
- Python 3.6+ (in system PATH)
- WinSW (`PythonSchedService.exe`)
- Python library: `schedule`
- Virtual environment: `venv`

## Files

- `sched.py`: Main script
- `schedule.bat`: Runs the script
- `PythonSchedService.xml`: WinSW config
- `PythonSchedService.exe`: WinSW executable
- `current_time.txt`: Timestamp output
- `service.log`: Script logs
- `logs\`: WinSW logs (`PythonSchedService.out.log`, `PythonSchedService.err.log`)

## Setup

1. **Install Python and Virtual Environment**:

   ```bash
   python -m venv venv
   venv\Scripts\activate.bat
   pip install schedule
   ```

2. **Get WinSW**:

   - Download `WinSW-x64.exe` from GitHub.
   - Rename to `PythonSchedService.exe` and place in parent project directory.

3. **Set Permissions**:

   ```bash
   icacls "D:\College\Semester 6 (Magang)\Iseng\SERVICE SCHEDULER" /grant "SYSTEM:(F)" /T
   ```

4. **Create Logs Folder**:

   ```bash
   mkdir D:\College\Semester 6 (Magang)\Iseng\SERVICE SCHEDULER\logs
   ```

5. **Install Service**:

   ```bash
   cd D:\College\Semester 6 (Magang)\Iseng\SERVICE SCHEDULER
   PythonSchedService.exe install
   ```

## Usage

- **Start**:

  ```bash
  PythonSchedService.exe start
  ```

  Or use Services (`services.msc`).

- **Check Output**:

  - Timestamps: `current_time.txt`
  - Logs: `service.log`, `logs\PythonSchedService.err.log`

- **Stop**:

  ```bash
  PythonSchedService.exe stop
  ```

- **Uninstall**:

  ```bash
  PythonSchedService.exe uninstall
  ```

## Troubleshooting

- **Service Stops**:

  - Check `logs\PythonSchedService.err.log` and `service.log`.
  - Test `run.bat`:

    ```bash
    D:\College\Semester 6 (Magang)\Iseng\SERVICE SCHEDULER\run.bat
    ```

  - Verify permissions.

- **No Timestamps**:

  - Ensure service is running (`PythonSchedService.exe status`).
  - Check `sched.py` paths.
