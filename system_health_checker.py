import psutil
import json
import time
from datetime import datetime

# To get the CPU status
def get_cpu_status():

  cpu = psutil.cpu_percent()
  usage = cpu
  
  return {"status": "Alert" if usage > 80 else "Healthy", "Usage": f"{usage}%"}

# To get the Memory status
def get_memory_status():
  memory = psutil.virtual_memory()
  usage = memory.percent

  return {"status": "Alert" if usage > 80 else "Healthy", "Usage": f"{usage}%"}

# To get the Disk status
def get_disk_status():

  disk = psutil.disk_usage('/')
  usage = disk.percent

  return {"status": "Alert" if usage > 80 else "Healthy", "Usage": f"{usage}%"}

def system_health():

  all_reports = []
  max_reports = 24

  while True:

    cpu_status = get_cpu_status()
    memory_status = get_memory_status()
    disk_status = get_disk_status()

    combine_data = {
    "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    "cpu_status": cpu_status,
    "memory_status": memory_status,
    "disk_status": disk_status
    }

    all_reports.append(combine_data)

    # checks and remove if log is more than 24
    if len(all_reports) > max_reports:
      all_reports.pop(0)

    # Writes the cpu, memory & disk usage into a json file 
    with open("system_report.json", 'w') as file:
      json.dump(all_reports, file, indent=4)

   
    print(f"\n[{combine_data['timestamp']}] System Health Check:")
    for key, value in combine_data.items():
      if key != "timestamp":  # Skip timestamp
        if value["status"] == "Alert":
          print(f"{key.upper()}: {value['Usage']} High Usage Detected🆘🆘")
        else:
          print(f"{key.upper()}: {value['Usage']}")

    time.sleep(3600)

# Ensures the function only runs when the script is executed directly, not when it's imported as a module by another script
if __name__ == "__main__":
  try:
    print('Starting System Health Checker.......... CTRL + C to stop')
    system_health()
  except KeyboardInterrupt:
    print("\n\nSystem Health Checker stopped by user. Final report saved.")
  except Exception as e:
    print(f"\nAn unexpexted error occured: {e}")