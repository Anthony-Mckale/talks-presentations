


class TestClassConverter:
    @classmethod
    def setup_class(cls):
        print("\nsetup_class: setup any state specific to the execution of the given class\n")


    @classmethod
    def teardown_class(cls):
        print("\nteardown_class: teardown any state that was previously setup with a call to setup_class.\n")

    def setup_method(self, method):
        print("\nsetup_method: setup_method is invoked for every test method of a class.\n")


    def teardown_method(self, method):
        print("\nteardown_method: teardown any state that was previously setup with a setup_method call.\n")

    def test_sanity(self):
        assert 1 == 1