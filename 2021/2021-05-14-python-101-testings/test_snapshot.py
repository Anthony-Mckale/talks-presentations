def test_snapshot (snapshot):
    snapshot.assert_match("helloworld", "helloworld.txt")