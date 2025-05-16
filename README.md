# Pneumatic Tube Simulation

## Overview
This project simulates the motion of gas molecules in a 2D container using PyQt5, inspired by the concept of a pneumatic tube system. The original vision was to create a real-world pneumatic tube using actual pipes, motors, and pressure gradients to move objects from high-pressure to low-pressure areas. Due to practical challenges, this evolved into a Python-based simulation that demonstrates basic physics principles such as momentum transfer and collision detection. A dynamic solid object moves when struck by gas molecules within a static container, serving as a simplified model of a pneumatic transport system.

The simulation provides an educational tool for understanding gas dynamics and object motion, with potential as a stepping stone toward a physical implementation.

## Project Structure
The project is organized into two main directories: the root `PNEUMATIC_TUBE` directory and the `pyqt5-physical-simulation` subdirectory, which contains a more modular implementation.

### Root Directory (`PNEUMATIC_TUBE`)
- **main.py**: The core simulation script implementing a 2D gas molecule simulation using PyQt5. It includes:
  - `GasMolecule` class for molecule behavior (position, velocity, collision handling).
  - `SolidObject` class for the dynamic object (responds to collisions with molecules).
  - `GasSimulation` class for managing the PyQt5 scene, molecules, and updates.
- **GUI_def.py**: Preliminary GUI definitions (work in progress, not integrated).
- **my_think.png**: A diagram or sketch of the project concept.
- **README**: Basic project overview (this file supersedes it).
- **TODO**: List of tasks and planned improvements.
- **update.txt**: Log file for simulation events (e.g., object creation, simulation start).

### Subdirectory (`pyqt5-physical-simulation`) (not work yet, everything in main.py)
A more structured implementation with modular code:
- **src/main.py**: A refined version of the root `main.py` (may include updates or differences).
- **src/simulation/**:
  - `physics_engine.py`: Handles physics calculations (e.g., collisions, momentum transfer).
  - `__init__.py`: Marks the simulation directory as a Python package.
- **src/ui/**:
  - `main_window.py`: Defines the main application window (PyQt5-based).
  - `resources.qrc`: Resource file for GUI assets (e.g., icons, images).
- **src/utils/**:
  - `helpers.py`: Utility functions for the simulation (e.g., logging, calculations).
- **README.md**: Subdirectory-specific documentation.
- **requirements.txt**: Lists Python dependencies (e.g., PyQt5).

## How It Works
1. **Simulation Setup**:
   - A static square cylinder (larger container) defines the simulation bounds, preventing gas molecules from passing through.
   - A dynamic square cylinder (smaller, movable object) is centered inside, representing the object to be moved.
   - 50 gas molecules are randomly positioned within the container, avoiding overlap with the dynamic object.

2. **Physics Dynamics**:
   - Gas molecules move with random initial velocities and bounce off the static cylinder walls and the dynamic object.
   - Collisions with the dynamic object transfer momentum, causing it to move.
   - The dynamic object experiences friction and reduced velocity on wall collisions, simulating energy loss.

3. **Visualization**:
   - PyQt5 renders the simulation in a QGraphicsView, with molecules as circles, the static cylinder as a black outline, and the dynamic object as a red rectangle.
   - A QTimer updates the scene at ~60 FPS for smooth animation.

4. **Logging**:
   - Key events (e.g., object creation, simulation start) are logged to `update.txt` with timestamps.

## Getting Started
### Prerequisites
- Python 3.8+
- PyQt5 (`pip install PyQt5`)

### Running the Simulation
1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd PNEUMATIC_TUBE
   ```
2. Install dependencies:
   ```bash
   pip install -r pyqt5-physical-simulation/requirements.txt
   ```
3. Run the root simulation:
   ```bash
   python main.py
   ```
   Or run the modular version:
   ```bash
   cd pyqt5-physical-simulation/src
   python main.py
   ```

### Expected Output
A window (800x600 pixels) displays:
- A black-outlined static square cylinder.
- A red dynamic square cylinder centered inside.
- 50 gas molecules (small circles) moving and colliding.
- The dynamic object moves when hit by molecules, slowing down due to friction.

## Planned Improvements
- **Modular Integration**: Fully transition to the `pyqt5-physical-simulation` structure for better maintainability.
- **Enhanced Physics**: Add realistic gas pressure and temperature effects to better mimic a pneumatic system.
- **GUI Enhancements**: Integrate `GUI_def.py` and `main_window.py` for user controls (e.g., start/stop, pressure adjustment).
- **Real-World Transition**: Explore integrating hardware (e.g., motors, sensors) for a physical pneumatic tube prototype.
- **Performance Optimization**: Optimize collision detection for larger molecule counts.
- **Documentation**: Expand READMEs and add inline code comments.

## License
This project is licensed under the [MIT License](LICENSE), allowing anyone to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the software, subject to the conditions outlined in the license file.

## Contact
For questions or suggestions, open an issue or contact the project maintainer via GitHub.
