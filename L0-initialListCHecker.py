import pandas as pd

# Path to the CSV file
csv_file_path = r'C:\Users\User\Downloads\L0\initialList.csv'

# List of addresses to check
addresses_to_check = [
    "0x5eC8Cd4881eba87279f5F243Eb89EA9383E677c5",
    "0x5F4107FD9d987237A6dEC167E9a5EEa643F2c76e"
]

# Read the CSV file into a DataFrame
df = pd.read_csv(csv_file_path)

# Extract the 'ADDRESS' column as a set for faster lookup
addresses_in_csv = set(df['ADDRESS'])

# Check which addresses are present in the CSV
addresses_found = [address for address in addresses_to_check if address in addresses_in_csv]
addresses_not_found = [address for address in addresses_to_check if address not in addresses_in_csv]

# Print the results
print(f"Addresses found in CSV ({len(addresses_found)}):")
for address in addresses_found:
    print(address)

print(f"\nAddresses not found in CSV ({len(addresses_not_found)}):")
for address in addresses_not_found:
    print(address)
