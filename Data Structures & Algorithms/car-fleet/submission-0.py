class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = list(zip(position, speed))
        cars.sort(reverse=True)

        fleet = 0
        last_fleet_time = 0

        for pos, spd in cars:
            time = (target - pos) / spd

            if time > last_fleet_time:
                fleet += 1
                last_fleet_time = time
        return fleet