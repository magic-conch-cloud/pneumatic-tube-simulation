# Pneumatic Tube Simulation
# This program simulates the motion of gas molecules in a 2D container using PyQt5.
# It demonstrates momentum transfer and collision detection between gas molecules and a movable solid object (piston).
# The simulation is visualized in real time, and key events are logged to a file for tracking.

import sys
import random
from PyQt5.QtWidgets import QApplication, QGraphicsView, QGraphicsScene, QGraphicsEllipseItem, QGraphicsRectItem
from PyQt5.QtCore import QTimer, QRectF
from PyQt5.QtGui import QPainter
from datetime import datetime

# Function to log simulation events with timestamps to update.txt
def log_update(message):
    with open("c:\\Users\\int\\Documents\\pneumatic_tube\\update.txt", "a") as log_file:
        log_file.write(f"{datetime.now()}: {message}\n")

# -----------------------------
# Gas Molecule Class Definition
# -----------------------------
class GasMolecule(QGraphicsEllipseItem):
    """
    Represents a single gas molecule as a circle in the simulation.
    Each molecule has a position and a velocity (dx, dy).
    """
    def __init__(self, x, y, radius, dx, dy):
        """
        Initialize a gas molecule with position, size, and velocity.
        :param x: Initial x-coordinate
        :param y: Initial y-coordinate
        :param radius: Radius of the molecule
        :param dx: Initial velocity in x-direction
        :param dy: Initial velocity in y-direction
        """
        super().__init__(0, 0, radius * 2, radius * 2)  # Create a circle
        self.setPos(x, y)  # Set initial position
        self.dx = dx  # Velocity in x-direction
        self.dy = dy  # Velocity in y-direction

    def move(self, bounds, solid_object, static_cylinder):
        """
        Move the molecule and handle collisions with the static cylinder and the solid object.
        :param bounds: The rectangular bounds of the simulation (not used, kept for compatibility)
        :param solid_object: The dynamic solid object (piston)
        :param static_cylinder: The static container rectangle
        """
        # Calculate the new position based on current velocity
        new_x = self.x() + self.dx
        new_y = self.y() + self.dy

        # Bounce off the static cylinder walls (reverse velocity if hitting a wall)
        if new_x <= static_cylinder.left() or new_x + self.rect().width() >= static_cylinder.right():
            self.dx = -self.dx
        if new_y <= static_cylinder.top() or new_y + self.rect().height() >= static_cylinder.bottom():
            self.dy = -self.dy

        # Bounce off the dynamic solid object and transfer momentum
        if self.collidesWithItem(solid_object):
            # Reverse direction (elastic collision)
            self.dx = -self.dx
            self.dy = -self.dy
            # Apply force to the solid object in the opposite direction (momentum transfer)
            solid_object.apply_force(-self.dx, -self.dy)

        # Update the molecule's position
        self.setPos(self.x() + self.dx, self.y() + self.dy)

# --------------------------------------
# Dynamic Solid Object (Piston) Class
# --------------------------------------
class SolidObject(QGraphicsRectItem):
    """
    Represents the dynamic solid object (piston) that can move inside the static cylinder.
    The solid object has its own velocity and responds to collisions with gas molecules.
    """
    def __init__(self, x, y, width, height):
        """
        Initialize a solid object with position, size, and velocity.
        :param x: Initial x-coordinate
        :param y: Initial y-coordinate
        :param width: Width of the object
        :param height: Height of the object
        """
        super().__init__(0, 0, width, height)
        self.setPos(x, y)
        self.vx = 0  # Velocity in x-direction
        self.vy = 0  # Velocity in y-direction

    def apply_force(self, fx, fy):
        """
        Apply a force to the solid object, changing its velocity.
        Called when a gas molecule collides with the solid.
        :param fx: Force in x-direction (proportional to molecule's velocity)
        :param fy: Force in y-direction
        """
        self.vx += fx * 0.1  # The scaling factor controls responsiveness
        self.vy += fy * 0.1

    def move(self, bounds):
        """
        Move the solid object and handle collisions with the static cylinder walls.
        :param bounds: The static cylinder rectangle
        """
        # Calculate the new position based on current velocity
        new_x = self.x() + self.vx
        new_y = self.y() + self.vy

        # Bounce off the static cylinder walls and lose some energy (simulate imperfect collision)
        if new_x <= bounds.left() or new_x + self.rect().width() >= bounds.right():
            self.vx = -self.vx * 0.5  # Reverse and dampen velocity
        if new_y <= bounds.top() or new_y + self.rect().height() >= bounds.bottom():
            self.vy = -self.vy * 0.5

        # Apply friction to gradually slow down the object (simulate energy loss)
        self.vx *= 0.98
        self.vy *= 0.98

        # Update the object's position
        self.setPos(self.x() + self.vx, self.y() + self.vy)

# --------------------------------------
# Main Simulation Class
# --------------------------------------
class GasSimulation(QGraphicsView):
    """
    Sets up the simulation scene, creates all objects, and runs the simulation loop.
    """
    def __init__(self):
        """
        Initialize the gas simulation, including the scene, molecules, and solid object.
        """
        super().__init__()
        self.scene = QGraphicsScene(self)
        self.setScene(self.scene)
        self.setRenderHint(QPainter.Antialiasing)

        # --- Simulation parameters ---
        solid_width = 200
        solid_height = 100
        cylinder_width = solid_width + 400  # Extra width for gas molecules to move
        cylinder_height = solid_height + 10  # Only 10px higher than the solid

        # Define the static square cylinder (container)
        # This is the fixed boundary for the simulation
        self.static_cylinder = QRectF(
            100,
            250 - (cylinder_height / 2),  # Vertically centered in the window
            cylinder_width,
            cylinder_height
        )
        self.scene.addRect(self.static_cylinder)  # Draw the static cylinder
        log_update("Static cylinder created")

        # Define and center the dynamic solid object inside the static cylinder
        solid_x = self.static_cylinder.left() + (self.static_cylinder.width() - solid_width) / 2
        solid_y = self.static_cylinder.top() + (self.static_cylinder.height() - solid_height) / 2
        self.solid_object = SolidObject(solid_x, solid_y, solid_width, solid_height)
        self.scene.addItem(self.solid_object)
        log_update(f"Dynamic solid object created at ({solid_x}, {solid_y})")

        # Create gas molecules inside the static cylinder, avoiding overlap with the solid object
        self.molecules = []
        for _ in range(50):
            while True:
                # Random position within the static cylinder, with a margin
                x = random.uniform(self.static_cylinder.left() + 10, self.static_cylinder.right() - 20)
                y = random.uniform(self.static_cylinder.top() + 10, self.static_cylinder.bottom() - 20)
                radius = 5
                molecule_rect = QRectF(x, y, radius * 2, radius * 2)
                # Ensure no overlap with the solid object
                if not self.solid_object.sceneBoundingRect().intersects(molecule_rect):
                    break
            dx = random.uniform(-2, 2)
            dy = random.uniform(-2, 2)
            molecule = GasMolecule(x, y, radius, dx, dy)
            self.molecules.append(molecule)
            self.scene.addItem(molecule)
        log_update("Gas molecules created and positioned")

        # Set up a timer to update the simulation at ~60 FPS (16 ms interval)
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_simulation)
        self.timer.start(16)

    def update_simulation(self):
        """
        Update the positions of all molecules and the solid object.
        Called automatically by the QTimer.
        """
        for molecule in self.molecules:
            # Move each molecule, handle collisions
            molecule.move(self.static_cylinder, self.solid_object, self.static_cylinder)
        # Move the solid object (piston)
        self.solid_object.move(self.static_cylinder)

# --------------------------------------
# Program Entry Point
# --------------------------------------
if __name__ == '__main__':
    # Create the Qt application
    app = QApplication(sys.argv)
    # Create and show the simulation window
    simulation = GasSimulation()
    simulation.setWindowTitle("2D Gas Molecule Simulation with Static Cylinder")
    simulation.resize(800, 600)
    simulation.show()
    log_update("Simulation started")
    # Start the Qt event loop
    sys.exit(app.exec_())
