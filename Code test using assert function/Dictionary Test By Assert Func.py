def test_average():
    test_cases = [
        { "name" : "simple case 1",
          "input" : [1,2,3],
          "expected_result" : 2.0
        },
        {
          "name" : "simple case 2",
          "input" : [1,2,3,4],
          "expected_result" : 2.5
        },
        {
          "name" : "list with one item",
          "input" : [100],
          "expected_result" : 100.0
        },
        {
          "name" : "emty list",
          "input" : [],
          "expected_result" : None
        }
        ]
    for test_case in test_cases:
        def average():
            av = sum(test_case["input"])/len(test_case["input"])
            return av
        assert test_case["expected_result"] == average(),test_case["name"]
