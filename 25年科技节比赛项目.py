import random


class Robot:
    def __init__(self):
        self.resources = 0
        self.position = [0, 0]

    def collect_resources(self, resource_amount):
        self.resources += resource_amount
        print(f"成功收集 {resource_amount} 个资源，当前资源总量: {self.resources}")

    def move(self, direction):
        if direction == 'up':
            self.position[1] += 1
        elif direction == 'down':
            self.position[1] -= 1
        elif direction == 'left':
            self.position[0] -= 1
        elif direction == 'right':
            self.position[0] += 1
        print(f"机器人移动到位置: {self.position}")

    def cross_obstacle(self):
        success = random.choice([True, False])
        if success:
            print("成功跨越障碍！")
        else:
            print("跨越障碍失败，尝试重新规划路径。")
        return success


def path_planning():
    directions = ['up', 'down', 'left', 'right']
    return random.choice(directions)


if __name__ == "__main__":
    robot = Robot()
    for _ in range(5):
        # 路径规划
        direction = path_planning()
        robot.move(direction)

        # 检查是否有资源可收集
        if random.random() < 0.5:
            resource_amount = random.randint(1, 10)
            robot.collect_resources(resource_amount)

        # 检查是否遇到障碍
        if random.random() < 0.3:
            robot.cross_obstacle()
    