# This program simulates the motion of gas molecules in a 2D container using PyQt5.
# It includes a solid object that moves when hit by gas molecules, demonstrating
# basic physics principles like momentum transfer and collision detection.

# Import necessary PyQt5 modules for GUI and graphics
import sys
import random
from PyQt5.QtWidgets import QApplication, QGraphicsView, QGraphicsScene, QGraphicsEllipseItem, QGraphicsRectItem
from PyQt5.QtCore import QTimer, QRectF
from PyQt5.QtGui import QPainter
from datetime import datetime

# Function to log updates to a file
def log_update(message):
    with open("c:\\Users\\int\\Documents\\pneumatic_tube\\update.txt", "a") as log_file:
        log_file.write(f"{datetime.now()}: {message}\n")

# Class representing a single gas molecule
class GasMolecule(QGraphicsEllipseItem):
    def __init__(self, x, y, radius, dx, dy):
        """
        Initialize a gas molecule with position, size, and velocity.
        :param x: Initial x-coordinate of the molecule
        :param y: Initial y-coordinate of the molecule
        :param radius: Radius of the molecule
        :param dx: Velocity in the x-direction
        :param dy: Velocity in the y-direction
        """
        super().__init__(0, 0, radius * 2, radius * 2)  # Create a circular molecule
        self.setPos(x, y)  # Set initial position
        self.dx = dx  # Velocity in x-direction
        self.dy = dy  # Velocity in y-direction

    def move(self, bounds, solid_object, static_cylinder):
        """
        Move the molecule and handle collisions with walls, the solid object, and the static cylinder.
        :param bounds: The rectangular bounds of the simulation
        :param solid_object: The solid object in the simulation
        :param static_cylinder: The static cylinder in the simulation
        """
        # Calculate the new position
        new_x = self.x() + self.dx
        new_y = self.y() + self.dy

        # Check for collisions with the walls of the static cylinder
        if new_x <= static_cylinder.left() or new_x + self.rect().width() >= static_cylinder.right():
            self.dx = -self.dx
        if new_y <= static_cylinder.top() or new_y + self.rect().height() >= static_cylinder.bottom():
            self.dy = -self.dy

        # Check for collisions with the dynamic solid object
        if self.collidesWithItem(solid_object):
            self.dx = -self.dx
            self.dy = -self.dy
            solid_object.apply_force(-self.dx, -self.dy)

        # Update the molecule's position
        self.setPos(self.x() + self.dx, self.y() + self.dy)

# Class representing the solid object
class SolidObject(QGraphicsRectItem):
    def __init__(self, x, y, width, height):
        """
        Initialize a solid object with position, size, and velocity.
        :param x: Initial x-coordinate of the object
        :param y: Initial y-coordinate of the object
        :param width: Width of the object
        :param height: Height of the object
        """
        super().__init__(0, 0, width, height)  # Create a rectangular object
        self.setPos(x, y)  # Set initial position
        self.vx = 0  # Velocity in x-direction
        self.vy = 0  # Velocity in y-direction

    def apply_force(self, fx, fy):
        """
        Apply a force to the solid object, changing its velocity.
        :param fx: Force in the x-direction
        :param fy: Force in the y-direction
        """
        self.vx += fx * 0.1  # Adjust velocity based on force (scaled by 0.1)
        self.vy += fy * 0.1

    def move(self, bounds):
        """
        Move the solid object and handle collisions with the walls of the static cylinder.
        :param bounds: The rectangular bounds of the simulation
        """
        # Calculate the new position
        new_x = self.x() + self.vx
        new_y = self.y() + self.vy

        # Check for collisions with the walls of the static cylinder
        if new_x <= bounds.left() or new_x + self.rect().width() >= bounds.right():
            self.vx = -self.vx * 0.5  # Reverse and reduce velocity on x-axis collision
        if new_y <= bounds.top() or new_y + self.rect().height() >= bounds.bottom():
            self.vy = -self.vy * 0.5  # Reverse and reduce velocity on y-axis collision

        # Apply friction to gradually slow down the object
        self.vx *= 0.98
        self.vy *= 0.98

        # Update the object's position
        self.setPos(self.x() + self.vx, self.y() + self.vy)

# Main simulation class
class GasSimulation(QGraphicsView):
    def __init__(self):
        """
        Initialize the gas simulation, including the scene, molecules, and solid object.
        """
        super().__init__()
        self.scene = QGraphicsScene(self)  # Create a graphics scene
        self.setScene(self.scene)  # Set the scene for the view
        self.setRenderHint(QPainter.Antialiasing)  # Enable antialiasing for smoother rendering

        # Define the simulation bounds (static square cylinder)
        solid_width = 200
        solid_height = 100
        cylinder_width = solid_width + 400  # Add extra width for gas molecules
        cylinder_height = solid_height + 10  # Height is 10px higher than the solid object
        self.static_cylinder = QRectF(
            100,  # Left
            250 - (cylinder_height / 2),  # Center the cylinder vertically around the solid object
            cylinder_width,
            cylinder_height
        )
        self.scene.addRect(self.static_cylinder)  # Visualize the static cylinder
        log_update("Static cylinder created")

        # Define the dynamic solid object
        solid_x = self.static_cylinder.left() + (self.static_cylinder.width() - solid_width) / 2
        solid_y = self.static_cylinder.top() + (self.static_cylinder.height() - solid_height) / 2
        self.solid_object = SolidObject(solid_x, solid_y, solid_width, solid_height)  # Centered dynamic rectangle
        self.scene.addItem(self.solid_object)
        log_update(f"Dynamic solid object created at ({solid_x}, {solid_y})")

        # Add gas molecules inside the static cylinder
        self.molecules = []
        for _ in range(50):  # Create 50 molecules
            while True:
                x = random.uniform(self.static_cylinder.left() + 10, self.static_cylinder.right() - 20)
                y = random.uniform(self.static_cylinder.top() + 10, self.static_cylinder.bottom() - 20)
                radius = 5
                molecule_rect = QRectF(x, y, radius * 2, radius * 2)
                if not self.solid_object.sceneBoundingRect().intersects(molecule_rect):
                    break
            dx = random.uniform(-2, 2)
            dy = random.uniform(-2, 2)
            molecule = GasMolecule(x, y, radius, dx, dy)
            self.molecules.append(molecule)
            self.scene.addItem(molecule)
        log_update("Gas molecules created and positioned")

        # Set up a timer to update the simulation
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_simulation)  # Call update_simulation periodically
        self.timer.start(16)  # Update every 16 ms (~60 FPS)

    def update_simulation(self):
        """
        Update the positions of all molecules and the solid object.
        """
        for molecule in self.molecules:
            molecule.move(self.static_cylinder, self.solid_object, self.static_cylinder)  # Pass solid_object and static_cylinder to handle collisions
        self.solid_object.move(self.static_cylinder)  # Move the solid object

if __name__ == '__main__':
    app = QApplication(sys.argv)  # Create the application
    simulation = GasSimulation()  # Create the simulation
    simulation.setWindowTitle("2D Gas Molecule Simulation with Static Cylinder")  # Set window title
    simulation.resize(800, 600)  # Set window size
    simulation.show()  # Show the simulation window
    log_update("Simulation started")
    sys.exit(app.exec_())  # Run the application event loop