import win32com.client
shell = win32com.client.Dispatch("WScript.Shell")
shell.Run('cmd /K (cd "C:\Users\Sanhe Hu\Desktop" && lisa.jpg)')