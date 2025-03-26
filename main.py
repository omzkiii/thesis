from controllers import main
from controllers import gui

# main.generate("Sampaloc, Manila", ["school", "college", "institute", "university"])
# main.generate("Sampaloc, Manila", ["station", "bus_station", "stop", "train_station"])
gui.gui(main.generate)
