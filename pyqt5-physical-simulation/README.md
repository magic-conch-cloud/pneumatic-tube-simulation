# pyqt5-physical-simulation

## Project Overview
This project is a graphical user interface application developed using PyQt5 for simulating physical phenomena. The application allows users to interact with various simulation parameters and visualize the results in real-time.

## Project Structure 
Most of what's written here doesn't work yet. Everything still works in main.py, which is outside the current folder.
```
pyqt5-physical-simulation
├── src
│   ├── main.py                # Entry point of the application 
│   ├── ui
│   │   ├── main_window.py     # Main user interface definition
│   │   └── resources.qrc      # Qt resource file for images and icons
│   ├── simulation
│   │   ├── __init__.py        # Marks the simulation directory as a package
│   │   └── physics_engine.py   # Core logic for the physical simulation
│   └── utils
│       └── helpers.py         # Utility functions for the application
├── requirements.txt           # Project dependencies
└── README.md                  # Documentation for the project
```

## Setup Instructions
1. **Clone the repository**:
   ```
   git clone <repository-url>
   cd pyqt5-physical-simulation
   ```

2. **Install dependencies**:
   It is recommended to use a virtual environment. You can create one using:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```
   Then install the required packages:
   ```
   pip install -r requirements.txt
   ```

3. **Compile the Qt resource file**:
   Use the `pyrcc5` tool to compile the `resources.qrc` file into a Python module:
   ```
   pyrcc5 -o src/ui/resources.py src/ui/resources.qrc
   ```

## Usage
To run the application, execute the following command:
```
python src/main.py
```

## Features
- Interactive user interface for setting simulation parameters.
- Real-time visualization of simulation results.
- Modular design with separate components for UI, simulation logic, and utility functions.

## Contributing
Contributions are welcome! Please submit a pull request or open an issue for any suggestions or improvements.

## License
This project is licensed under the MIT License. See the LICENSE file for details.
