from src.checker import pi_distance


def test_pi_distance__zero_check():
    x1, y1 = (1, 1)
    x2, y2 = (1, 1)
    assert pi_distance(x1, y1, x2, y2) == 0


def test_pi_distance__Edinburgh_Dundee_check():
    x1, y1 = (55.953251, -3.188267) # Edinburgh
    x2, y2 = (56.462002, -2.970700) # Dundee
    assert pi_distance(x1, y1, x2, y2) == 0.5533199612249649

def test_pi_distance__Perth_Dundee_check():
    x1, y1 = (56.396999, -3.437000) # Perth
    x2, y2 = (56.462002, -2.970700) # Dundee
    assert pi_distance(x1, y1, x2, y2) == 0.47080896339067246

def test_pi_distance__Dundee_Perth_check():
    x2, y2 = (56.396999, -3.437000) # Perth
    x1, y1 = (56.462002, -2.970700) # Dundee
    assert pi_distance(x1, y1, x2, y2) == 0.47080896339067246