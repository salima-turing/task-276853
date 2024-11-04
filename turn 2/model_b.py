import random


def generate_calibration_tests(num_tests=5, custom_tolerances=None):
    test_id = 1
    sensor_types = ["Temperature", "Humidity", "Pressure", "Light", "Battery"]
    default_tolerances = {
        "Temperature": 0.5,
        "Humidity": 0.5,
        "Pressure": 5,
        "Light": 20,
        "Battery": 0.1
    }

    if custom_tolerances is not None:
        default_tolerances.update(custom_tolerances)

    for _ in range(num_tests):
        sensor_type = random.choice(sensor_types)
        tolerance = default_tolerances[sensor_type]

        if sensor_type == "Battery":
            # Vary the tolerance for battery calibration based on voltage range
            battery_voltage = random.uniform(3.0, 4.2)
            if 3.0 <= battery_voltage < 3.6:
                tolerance = 0.2
            elif 3.6 <= battery_voltage < 4.0:
                tolerance = 0.15
            else:
                tolerance = 0.1

        expected_result = random.uniform(0, 100) if sensor_type != "Pressure" else random.uniform(900, 1100)

        # Additional sensor-specific calibration rules can be added here
        if sensor_type == "Light" and expected_result > 90:
            # Force tolerance to be high for high light levels
            tolerance = 10

        test_case = {
            "test_id": test_id,
            "action": f"Calibrate {sensor_type} sensor",
            "input_data": {"sensor_type": sensor_type},
            "expected_result": {"value": expected_result, "tolerance": tolerance}
        }
        yield test_case
        test_id += 1


if __name__ == "__main__":
    # Example usage with custom tolerances for Temperature and Pressure
    custom_tolerances = {
        "Temperature": 0.2,
        "Pressure": 3,
    }
    for test in generate_calibration_tests(num_tests=10, custom_tolerances=custom_tolerances):
        print(f"Test {test['test_id']}: {test['action']}")
        print(f"Input: {test['input_data']}")
        print(f"Expected Result: {test['expected_result']}")
        print("-" * 30)
