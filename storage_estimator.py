# Storage Estimator
# Estimates storage required for a given number of devices.

device_count = int(input("Enter number of devices: "))
storage_per_device = float(input("Enter storage per device in GB: "))

if device_count < 0 or storage_per_device < 0:
    print("Error: values cannot be negative.")
else:
    total_storage = device_count * storage_per_device
    print("Total storage required:", total_storage, "GB")
    print("Total storage required:", total_storage / 1024, "TB")
    print("Total storage required:", total_storage * 1024, "MB")
