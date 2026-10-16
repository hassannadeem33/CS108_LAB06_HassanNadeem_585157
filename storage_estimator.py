# Storage Estimator
# Estimates storage required for a given number of devices.

device_count = int(input("Enter number of devices: "))
storage_per_device = float(input("Enter storage per device in GB: "))

total_storage = device_count * storage_per_device

print("Total storage required:", total_storage, "GB")