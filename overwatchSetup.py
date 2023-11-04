import bluetooth

device_index = 0
device_dict = {}
device_chosen_index_num = 0


def is_valid_input(input):
    global device_chosen_index_num
    try:
        device_chosen_index_num = int(input)
    except ValueError:
        raise ValueError(f'What you entered was not a number: "{input}"')
    # implment a way to check if the index is not part of the index of the device_list
    return True


def list_devices():
    global device_dict

    nearby_devices = bluetooth.discover_devices(lookup_names=True)
    print("Available Bluetooth Devices:")
    device_index = 0

    for addr, name in nearby_devices:
        print(f"index: {device_index} | {name} ({addr})")
        device_dict[device_index] = addr

        device_index += 1

    user_input = input("Enter the device index you want to connect to: ")

    is_valid_input(user_input)


'''
def connect_to_device(device_addr):
    socket = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
    socket.connect((device_addr, 1))
    print(f"Connected to {device_addr}")'''


print("loading devices...")
list_devices()
print(device_dict)
mac_address = device_dict[device_chosen_index_num]

# connect_to_device(mac_address)
