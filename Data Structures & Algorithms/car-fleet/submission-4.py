class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        cars = [(p, s) for p, s in zip(position, speed)]
        cars.sort(reverse=True)

        times = [(target - cars[0][0]) / cars[0][1]]
        for i in range(1, len(cars)):
            pos, spd = cars[i]
            currTime = (target - pos) / spd

            if times[-1] < currTime:
                times.append(currTime)

        return len(times)

