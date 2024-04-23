import logging
import time
import re
import sys

# Configure logging
logging.basicConfig(level=logging.INFO,format='%(asctime)s - %(levelname)s - %(message)s')

def monitor_log(log_file):
    try:
        with open(log_file, 'r') as file:
            file.seek(0, 2) # Go to the end of the file
            while True:
                line = file.readline()
                if not line:
                    time.sleep(0.1) # Sleep briefly
                    continue
                yield line
    except KeyboardInterrupt:
        logging.info("Monitoring stopped by user.")
        sys.exit(0)

def analyze_log(log_file):
    error_pattern = re.compile(r'ERROR')
    http_status_pattern = re.compile(r'\bHTTP\s+[45]\d{2}\b')
    error_count = 0
    http_error_count = 0

    for line in monitor_log(log_file):
        if error_pattern.search(line):
            error_count += 1
        if http_status_pattern.search(line):
            http_error_count += 1

        # Display real-time analysis
        print(f"Error count: {error_count}, HTTP error count: {http_error_count}")

def main():
    log_file = 'your_log_file.log' # Specify your log file path here
    logging.info(f"Starting log monitoring for {log_file}")
    analyze_log(log_file)

if __name__ == "__main__":
    main()
