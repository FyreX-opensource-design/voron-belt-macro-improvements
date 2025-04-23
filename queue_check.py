import requests

def queue_check():
  MOONRAKER_URL = "127.0.0.1:7125"  # or IP address
  response = requests.get(f"{MOONRAKER_URL}/server/files/queue")
  queue = response.json().get("queue", [])

  if not queue:
      return 0
  else:
      return 1