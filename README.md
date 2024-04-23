# Log Analysis and Monitoring Script

This script monitors a specified log file for new entries and performs basic analysis on log entries, such as counting occurrences of specific keywords or patterns (e.g., error messages, HTTP status codes) and generating summary reports.

## Prerequisites

- Python 3.x

## Usage

1. Clone this repository.
2. Update the `log_file` variable in `log-monitor.py` with the path to your log file.
3. Run the script using Python: python3 log-monitor.py
4. The script will start monitoring the log file for new entries and perform real-time analysis.
5. To stop the monitoring, press `Ctrl+C`.

## Features

- Continuous monitoring of a specified log file.
- Real-time analysis of log entries for specific keywords or patterns.
- Summary reports on error counts and HTTP error counts.
- Error handling and logging for script execution feedback.

## Contributing

Feel free to fork this repository and submit pull requests for improvements or additional features.
