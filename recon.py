#!/usr/bin/env python3
# ==============================
# Name: recon
# Author: Brendon Hutchins
# Date: 02/02/23
# Version: 1.0
# ==============================

# ==============================
# Comments:
#
#
#
#
# ==============================

# Imports
from tabulate import tabulate
from argparse import ArgumentParser
import subprocess
import os
import sys
import time

# Globals

parser = ArgumentParser(description='*** Recon ***')

def example():
    result = subprocess.run([sys.executable, "-c", "print('hello world')"])
    result = subprocess.run([sys.executable, "-c", "import time; time.sleep(2)"], capture_output=True, text=True, timeout=3)
    data = subprocess.run(["powershell", "get-process"], shell=False)
    print("stdout: ", result.stdout)
    print("stderr: ", result.stderr)
    print(result.check_returncode())

def getNetwork():
    print("========================================   NETWORK INFO   ============================================")
    networkInfo = subprocess.run(["powershell", "Get-NetNeighbor | Sort-Object -Property State"], capture_output=True, text=True, timeout=10)
    print(networkInfo.stdout)
    print("----------------------------------------   ROUTE INFO   -----------------------------------------------")
    routeInfo = subprocess.run(["powershell", "Get-NetRoute | Sort-Object -Property State"], capture_output=True, text=True, timeout=10)
    print(routeInfo.stdout)
    print("----------------------------------------   HOST FILE   -----------------------------------------------")
    hostFile = subprocess.run(["powershell", "Get-content C:\Windows\System32\Drivers\etc\hosts"], capture_output=True, text=True, timeout=10)
    print(hostFile.stdout)
    print("----------------------------------------   TCP Connections   -----------------------------------------------")
    tcpConnections = subprocess.run(["powershell", "Get-NetTCPConnection | Sort-Object -Property State"], capture_output=True, text=True, timeout=10)
    print(tcpConnections.stdout)
    print("----------------------------------------   UDP Connections   -----------------------------------------------")
    tcpConnections = subprocess.run(["powershell", "Get-NetUDPEndpoint"], capture_output=True, text=True, timeout=10)
    print(tcpConnections.stdout)
    print("----------------------------------------   DNS Cache   -----------------------------------------------")
    tcpConnections = subprocess.run(["powershell", "Get-DnsClientCache"], capture_output=True, text=True, timeout=10)
    print(tcpConnections.stdout)

def getSystem():
    print("========================================   SYSTEM INFO   ============================================")
    winVersion = subprocess.run(["powershell", "wmic os get version"], capture_output=True, text=True, timeout=10)
    print(winVersion.stdout)
    print("----------------------------------------   Current User  --------------------------------------------")
    whoami = subprocess.run(["powershell", "whoami /all"], capture_output=True, text=True, timeout=10)
    print(whoami.stdout)
    print("----------------------------------------   System Users All  --------------------------------------------")
    systemUsers = subprocess.run(["powershell", "net user"], capture_output=True, text=True, timeout=10)
    print(systemUsers.stdout)
    print("----------------------------------------   Windows Updates  --------------------------------------------")
    systemUpdates = subprocess.run(["powershell", "wmic qfe list"], capture_output=True, text=True, timeout=10)
    print(systemUpdates.stdout)
    print("----------------------------------------   Running Processes  --------------------------------------------")
    systemUpdates = subprocess.run(["powershell", "Get-Process -FileVersion"], capture_output=True, text=True, timeout=10)
    print(systemUpdates.stdout)
    print("----------------------------------------   Interesting Files  --------------------------------------------")
    existPython = subprocess.run(["powershell", "Test-Path -Path 'INSERT-TESTPATH-HERE' "], capture_output=True, text=True, timeout=10)
    print("Exists Python: ", existPython.stdout)
    existPerl = subprocess.run(["powershell", "Test-Path -Path 'INSERT-TESTPATH-HERE' "], capture_output=True, text=True, timeout=10)
    print("Exists Perl: ", existPerl.stdout)

# RUN
#example()
getNetwork()
getSystem()

