🖥️ System Health Checker

A simple Python script that continuously monitors your CPU, Memory, and Disk usage, saving hourly reports to a JSON file. It helps detect high system resource usage by marking alerts when usage exceeds 80%.

📋 Features

✅ Monitors CPU, Memory, and Disk utilization

✅ Marks “Alert” when usage > 80%

✅ Saves all reports (up to 24 entries) to system_report.json

✅ Prints readable status messages to the console

✅ Automatically runs health checks hourly

⚙️ Requirements

Make sure you have Python 3.7+ installed.

Then, install the required dependency:

	pip install psutil

🚀 How to Run

1️⃣Clone or download this script to your system.

2️⃣ Open a terminal or command prompt in the script’s directory.

3️⃣ Run the script:

	python system_health_checker.py

The program will begin monitoring and display updates every hour.

Press CTRL + C anytime to stop the program safely.

🧠 Example Output
	
	[2025-10-29 10:00:00] System Health Check:
	
	CPU_STATUS: 25.6%
	
	MEMORY_STATUS: 65.3%
	
	DISK_STATUS: 81.2% High Usage Detected🆘🆘

🗂️ Output File

Reports are stored in a file called:

	"system_report.json"

Each record contains:
	
	{
	    "timestamp": "2025-10-29 10:00:00",
	    "cpu_status": {
	        "status": "Healthy",
	        "Usage": "25.6%"
	    },
	    "memory_status": {
	        "status": "Healthy",
	        "Usage": "65.3%"
	    },
	    "disk_status": {
	        "status": "Alert",
	        "Usage": "81.2%"
	    }
	}

⚠️ Notes

1️⃣ Default monitoring interval: 1 hour

2️⃣ Maximum stored reports: 24 (oldest report auto-deleted)

3️⃣ Disk path automatically adapts to your operating system

4️⃣ Stop anytime using CTRL + C

🧩 Future Enhancements (optional ideas)

1️⃣ Add logging for long-term data retention

2️⃣ Add email or Telegram alerts when status = “Alert”
