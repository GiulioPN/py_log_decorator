import math
import random

from decorators import log_execution_time
from logger import app_logger


@log_execution_time(operation_name="estimate_pi")
def estimate_pi(num_points: int = 1000) -> float:
    """Estimate the value of pi using Monte Carlo method.

    Parameters
    ----------
    num_points : int, optional
        The number of points to use in the simulation, by default 1000

    Returns
    -------
    float
        The estimated value of pi
    """
    points_inside_circle = 0

    for _ in range(num_points):
        # Generate random points between 0 and 1
        x = random.uniform(0, 1)
        y = random.uniform(0, 1)

        # Check if point lies inside quarter circle
        distance = math.sqrt(x**2 + y**2)
        if distance <= 1:
            points_inside_circle += 1

    # Calculate pi: (points inside circle / total points) * 4
    pi_estimate = 4 * points_inside_circle / num_points
    return pi_estimate


if __name__ == "__main__":
    # Run simulation with 100000 points
    estimated_pi = estimate_pi(100000)
    app_logger.info(f"Estimated value of π: {estimated_pi:.6f}")
    app_logger.info(f"Actual value of π: {math.pi:.6f}")
    app_logger.info(f"Difference: {abs(estimated_pi - math.pi):.6f}")
