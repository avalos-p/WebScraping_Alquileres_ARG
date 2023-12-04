import os
from config.cfg import ROOT

def create_folder(path):
    """Create folder if doesnt exist.
    """
    if not os.path.exists(path):
        os.makedirs(os.path.join(ROOT, 'alquileres', path))


