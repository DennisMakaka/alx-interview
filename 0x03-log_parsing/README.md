# 0x03. Log Parsing

## Project Overview

This project involves creating a Python script to parse and analyze server logs in real-time. The script reads data from `stdin`, processes logs line by line, and computes aggregated metrics.

## Requirements

- **Python Version**: Interpreted on Ubuntu 20.04 LTS using Python 3.4.3
- **Style**: Follows PEP 8 guidelines
- **Execution**: Script files must be executable and should start with `#!/usr/bin/python3`

## Usage

Run the log parsing script by piping log data into it via standard input, either through real log data or the generator script (`0-generator.py`).

## Input Format

Log entries must follow this format:

<IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size>


- **IP Address**: IPv4 address of the client
- **Status Code**: HTTP status code (e.g., 200, 301, 400)
- **File Size**: Size of the served file in bytes

Lines not matching this format will be skipped.

## Output

The script outputs these metrics:
- **Total File Size**: Cumulative sum of all file sizes.
- **Status Code Counts**: Counts each status code encountered, printed in ascending order.

Metrics are displayed every 10 lines or when interrupted by a keyboard signal (CTRL + C).

## Project Task

### Task 0: Log Parsing

- **Objective**: Implement a script (`0-stats.py`) that reads `stdin` line by line, parses the required fields, and computes metrics.
- **Steps**:
  - Parse log lines, extracting the IP, status code, and file size.
  - Display metrics every 10 lines or on keyboard interrupt.
- **Key Skills**:
  - File I/O (standard input)
  - Data aggregation and parsing
  - Signal handling for interruption
  - Dictionary usage for counting status codes
  - Exception handling for erroneous lines

## Repository

- **GitHub repository**: `alx-interview`
- **Directory**: `0x03-log_parsing`
- **File**: `0-stats.py`

