ECHO off
Powershell.exe -executionpolicy RemoteSigned
Powershell.exe Import-Module PSWindowsUpdate
Powershell.exe Install-Module PSWindowsUpdate