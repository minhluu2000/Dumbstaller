powershell -ExecutionPolicy ByPass -Command Install-Module PSWindowsUpdate
powershell -ExecutionPolicy ByPass -Command Get-WUInstall -MicrosoftUpdate -AcceptAll -AutoReboot
powershell -ExecutionPolicy ByPass -Command Get-WindowsUpdate -AcceptAll -Install -IgnoreReboot
cmd /k