# AC-Remote-Control---Python-Project


## Description:
This project simulates an air conditioner control system using software. The user can control various aspects of the air conditioner, such as cooling, heating, automatic mode, fan speed, temperature, and eco mode. The system uses a circular linked list structure to manage the dynamic states of the air conditioner.

## Classes:

### 1. `AcAbstract`:
- An abstract class that defines the basic methods for controlling the air conditioner, including `Temperatura`, `Mode`, `Fan`, `Eco`, `Power`, `Time`, and `DisplyScreen`.

### 2. `ACRemoteControl`:
- A class that implements the methods defined in `AcAbstract` and performs the actual control functions, such as changing the temperature, mode, fan speed, and turning the power on/off.
- It uses a linked list to manage the air conditioner's modes (such as Cool, Heat, Auto).

### 3. `LinkedList`:
- Implements a circular linked list where each node represents a state (mode) of the air conditioner. It supports searching for a specific node, printing the entire list, and keeping track of the list's size.

### 4. `Node`:
- Represents a node in the linked list, storing a value (mode) and the reference to the next node.

## Requirements:
- Python 3.x

## Installation:
1. Download all the files.
2. Run the `MAIN.py` file to start using the system.

## Usage Example:
Here is a code example to demonstrate how to use the system to control the air conditioner:

```python
from ACRemoteControl import ACRemoteControl

# Create an instance of the RemoteControl
RemoteControl = ACRemoteControl()

# Turn the air conditioner ON
RemoteControl.Power('ON')

# Activate Eco Mode
RemoteControl.Eco('ON')

# Set the air conditioner's mode to the 4th mode (could be Cool, Heat, etc.)
RemoteControl.Mode(4)

# Change the fan speed
RemoteControl.Fan('FAN')

# Increase the temperature
RemoteControl.Temperatura('+')
RemoteControl.Temperatura('+')

# Display the current settings
RemoteControl.DisplyScreen()
