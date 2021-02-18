import enum
import numpy as np

from napari_plugin_engine import napari_hook_implementation


# Enums are a convenient way to get a dropdown menu
class Operation(enum.Enum):
    """A set of valid arithmetic operations for image_arithmetic."""

    add = np.add
    subtract = np.subtract
    multiply = np.multiply
    divide = np.divide


# Define our image_arithmetic function.
# Note that we can use forward references for the napari type annotations.
# You can read more about them here:
# https://www.python.org/dev/peps/pep-0484/#forward-references
# In this example, because we have already imported napari anyway, it doesn't
# really matter. But this syntax would let you specify that a parameter is a
# napari object type without actually importing or depending on napari.
# Note: here we use `napari.types.ImageData` as our parameter annotations,
# which means our function will be passed layer.data instead of
# the full layer instance
@napari_hook_implementation
def napari_experimental_provide_function():
    return [add, subtract, multiply, multiply]


def add(
    layerA: 'napari.types.ImageData',
    layerB: 'napari.types.ImageData',
) -> 'napari.types.ImageData':
    return np.add(layerA, layerB)

def subtract(
    layerA: 'napari.types.ImageData',
    layerB: 'napari.types.ImageData',
) -> 'napari.types.ImageData':
    return np.subtract(layerA, layerB)

def multiply(
    layerA: 'napari.types.ImageData',
    layerB: 'napari.types.ImageData',
) -> 'napari.types.ImageData':
    return np.multiply(layerA, layerB)

def divide(
    layerA: 'napari.types.ImageData',
    layerB: 'napari.types.ImageData',
) -> 'napari.types.ImageData':
    return np.divide(layerA, layerB)
