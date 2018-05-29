# noinspection PyShadowingBuiltins,PyUnusedLocal
def sum(x, y):

    try:
        val_x = int(x)
        val_y = int(y)
    except ValueError:
        raise

    assert val_x >= 0 and val_x <= 100, "Value must be between 0 and 100"
    assert val_y >= 0 and val_y <= 100, "Value must be between 0 and 100"

    return (val_x + val_y)
