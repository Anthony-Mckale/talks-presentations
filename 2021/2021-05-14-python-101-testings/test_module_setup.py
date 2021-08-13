def setup_module(module):
    print("setup any state specific to the execution of the given module.")


def teardown_module(module):
    print("teardown any state that was previously setup with a setup_module method.")

def test_sanity():
    assert 1 == 1


