@echo off
:: Verify python.exe exists
IF NOT EXIST "D:\College\Semester 6 (Magang)\Iseng\SERVICE SCHEDULER\venv\Scripts\python.exe" (
echo Error: python.exe not found in venv\Scripts
exit /b 1
)

:: Activate the virtual environment
CALL "D:\College\Semester 6 (Magang)\Iseng\SERVICE SCHEDULER\venv\Scripts\activate.bat"

:: Execute the Python script
"D:\College\Semester 6 (Magang)\Iseng\SERVICE SCHEDULER\venv\Scripts\python.exe" "D:\College\Semester 6 (Magang)\Iseng\SERVICE SCHEDULER\sched.py"