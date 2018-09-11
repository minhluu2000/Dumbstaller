powershell -ExecutionPolicy ByPass -Command Install-Module PSWindowsUpdate
powershell -ExecutionPolicy ByPass -Command Get-WUInstall -MicrosoftUpdate -AcceptAll -AutoReboot
cmd /k