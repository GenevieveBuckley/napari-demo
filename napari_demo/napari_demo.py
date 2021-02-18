import enum
import numpy as np


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
def napari_experimental_provide_function():
    return image_arithmetic


def image_arithmetic(
    layerA: 'napari.types.ImageData',
    operation: Operation,
    layerB: 'napari.types.ImageData',
) -> 'napari.types.ImageData':
    """Adds, subtracts, multiplies, or divides two same-shaped image layers."""
    return operation.value(layerA, layerB)
