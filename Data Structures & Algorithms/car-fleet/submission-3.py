class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        cars = [(p, s) for p, s in zip(position, speed)]
        cars.sort(reverse=True)

        hour = (target - cars[0][0]) / cars[0][1]

        stack = [] #10 8 3
        for i in range(0, len(cars)):
            pos, spd = cars[i]
            dest = (target - pos) / spd

            if stack and stack[-1] >= dest:
                continue
            else:
                stack.append(dest)
        return len(stack)

