import random


def generate_calibration_tests(num_tests=5):
    test_id = 1
    sensor_types = ["Temperature", "Humidity", "Pressure"]
    for _ in range(num_tests):
        sensor_type = random.choice(sensor_types)
        expected_result = random.uniform(0, 100) if sensor_type != "Pressure" else random.uniform(900, 1100)
        tolerance = 0.5 if sensor_type != "Pressure" else 5

        test_case = {
            "test_id": test_id,
            "action": "Calibrate {} sensor".format(sensor_type),
            "input_data": {"sensor_type": sensor_type},
            "expected_result": {"value": expected_result, "tolerance": tolerance},
        }
        yield test_case
        test_id += 1


if __name__ == "__main__":
    for test in generate_calibration_tests(num_tests=10):
        print(f"Test {test['test_id']}: {test['action']}")
        print(f"Input: {test['input_data']}")
        print(f"Expected Result: {test['expected_result']}")
        print("-" * 30)
