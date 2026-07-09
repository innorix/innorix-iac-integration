import os

from client import INNORIXClient

client = INNORIXClient()


files = [
    {
        "file_path": os.getenv("BOOTSTRAP_PATH"),
        "file_size": int(os.getenv("BOOTSTRAP_SIZE"))
    }
]


response = client.create_transfer(
    source_id=os.getenv("SOURCE_DEVICE_ID"),
    target_id=os.getenv("TARGET_DEVICE_ID"),
    target_path=os.getenv("TARGET_PATH"),
    files=files
)

print("Bootstrap transfer created.")
print(response)


automation_id = os.getenv("AUTOMATION_ID")

status = client.get_unified_transfer_list(
    automation_id=automation_id,
    limit=10,
    type_filter="history"
)

print(status)