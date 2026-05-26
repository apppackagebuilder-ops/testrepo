import logging

# Configure logging
logging.basicConfig(
    filename='app.log',          # Log file name
    level=logging.INFO,          # Log level
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# Sample log messages
logging.info("Application started")
logging.warning("This is a warning message")
logging.error("This is an error message")

print("Logs written to app.log")
