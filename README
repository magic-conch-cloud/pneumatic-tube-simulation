Pneumatic Tube Simulation

Overview:
This project simulates the motion of gas molecules in a 2D container using PyQt5, inspired by pneumatic tube systems. The simulation demonstrates basic physics principles such as momentum transfer and collision detection. A dynamic solid object (like a piston) moves when struck by gas molecules within a static container, serving as a simplified model of pneumatic transport and pressure-driven systems.

Features:
- Static Square Cylinder: A fixed, larger rectangle that acts as the simulation boundary. Gas molecules and the dynamic solid cannot pass through its walls.
- Dynamic Solid Object: A smaller rectangle (the "piston") that fits inside the static cylinder and moves when hit by gas molecules.
- Gas Molecules: Multiple molecules are randomly placed inside the static cylinder (avoiding overlap with the solid object) and move with random velocities, bouncing off walls and the solid object.
- Physics Engine: Handles elastic collisions, momentum transfer, and friction for realistic motion.
- Visualization: Uses PyQt5’s QGraphicsView to render the simulation in real time.
- Logging: Key simulation events (object creation, simulation start) are logged with timestamps in update.txt.

How It Works:
1. Initialization:
   - The static cylinder is created as a large rectangle.
   - The dynamic solid object is centered inside the static cylinder.
   - Gas molecules are randomly placed inside the cylinder, avoiding overlap with the solid object.

2. Simulation Loop:
   - Gas molecules move and bounce off the static cylinder walls and the dynamic solid object.
   - When a molecule collides with the solid object, it transfers momentum, causing the solid to move.
   - The solid object slows down over time due to friction and bounces off the static cylinder walls.

3. Visualization:
   - The static cylinder is drawn as a black rectangle.
   - The dynamic solid object is drawn as a red rectangle.
   - Gas molecules are drawn as small circles.

4. Logging:
   - Events such as object creation and simulation start are recorded in update.txt.

How the Physics Engine Works:
- **Gas Molecule Motion:** Each gas molecule has a position and velocity. On each update, its position is incremented by its velocity.
- **Wall Collisions:** If a molecule reaches the boundary of the static cylinder, its velocity component perpendicular to the wall is reversed, simulating an elastic bounce.
- **Solid Object Collisions:** When a molecule collides with the dynamic solid object, both its x and y velocity components are reversed (elastic collision). At the same time, a force proportional to the molecule’s velocity is applied to the solid object, causing it to move in the opposite direction (momentum transfer).
- **Solid Object Motion:** The solid object has its own velocity, which is updated whenever it is hit by a gas molecule. The solid object also bounces off the static cylinder walls, losing some energy (velocity is reduced) to simulate imperfect collisions.
- **Friction:** After each update, the solid object’s velocity is slightly reduced to simulate friction, causing it to eventually slow down if not continuously pushed by gas molecules.

Getting Started:
- Requires Python 3.8+ and PyQt5 (pip install PyQt5).
- Run the simulation with: python main.py

Expected Output:
- A window (800x600) showing a black-outlined static cylinder, a red dynamic solid object, and 50 moving gas molecules.
- The dynamic object moves when hit by molecules and slows down due to friction.

For more details, see the code comments in main.py.
