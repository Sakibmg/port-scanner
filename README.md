# Simple TCP Port Scanner

A small Python scanner built with sockets. It tries a TCP connection to each port in a range and reports the open ones.

## How it works
- socket.connect_ex returns 0 when a connection succeeds, which means the port is open
- A 1-second timeout stops closed ports from hanging the scan

## Usage
Set `target` in scanner.py, then run: python3 scanner.py

## Tested on
My own lab VM (Metasploitable2), and results matched `nmap -p 1-100`.

## Legal note
Only scan machines you own or have written permission to test.

## Next steps
Threading for speed, banner grabbing, a command-line argument for the target.
