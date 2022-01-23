# LC 973
import heapq

from typing import List


def k_closest_points_to_origin(points: List[List[int]], k: int) -> List[List[int]]:
    heap = []
    squared_distances_to_points = {}

    for point in points:
        squared_point_distance = point[0] ** 2 + point[1] ** 2
        heap.append(squared_point_distance)

        if squared_point_distance not in squared_distances_to_points:
            squared_distances_to_points[squared_point_distance] = []
        squared_distances_to_points[squared_point_distance].append(point)

    heapq.heapify(heap)

    min_squared_distances = []
    for _ in range(k):
        min_squared_distances.append(heapq.heappop(heap))

    min_squared_distances = list(set(min_squared_distances))

    min_distance_points = []

    for x in min_squared_distances:
        min_distance_points.extend(squared_distances_to_points[x])

    return min_distance_points


################################################################################
# Test cases.

tst = [[1, 2], [2, 1]]
expected = [[1, 2], [2, 1]]

assert k_closest_points_to_origin(tst, 2) == expected

tst = [[10, 1], [1, 2], [1, 3], [2, 4]]
expected = [[1, 2]]

assert k_closest_points_to_origin(tst, 1) == expected
