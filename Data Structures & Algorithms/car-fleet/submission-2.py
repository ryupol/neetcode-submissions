class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        cars = [(p, s) for p, s in zip(position, speed)]
        cars.sort(reverse=True)

        fleets = 1
        prevTime = (target - cars[0][0]) / cars[0][1]
        for i in range(1, len(cars)):
            currCar = cars[i]
            currTime = (target - currCar[0]) / currCar[1]

            if currTime > prevTime:
                fleets += 1
                prevTime = currTime
        return fleets

