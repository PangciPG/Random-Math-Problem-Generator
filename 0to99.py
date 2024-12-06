import random

def generate_math_problems(num_problems=1000):
    problems = []
    last_problem = None
    for i in range(num_problems):
        while True:
            # 随机选择加法或减法
            if random.choice([True, False]):
                # 加法
                a = random.randint(1, 99)  # 不出现0，最大为99
                b = random.randint(1, 100 - a)  # 保证和不超过100
                problem = f"{a} + {b} = "
            else:
                # 减法
                a = random.randint(10, 20)  # 确保减法的a不小于10
                b = random.randint(10, a - 10)  # 确保b不等于a
                problem = f"{a} - {b} = "
            
            # 确保相邻的两道题不重复
            if problem != last_problem:
                problems.append(problem)
                last_problem = problem
                break

        # 每10道题加分割线并注明范围
        if (i + 1) % 10 == 0:
            start = (i // 10) % 10 * 10 + 1
            end = start + 9
            problems.insert(-10, f"---{start}-{end}题---")
        
        # 每100道题加分页符并重置题目编号
        if (i + 1) % 100 == 0:
            problems.append("\f")  # Word兼容的分页符
            last_problem = None

    return problems

def save_problems_to_file(problems, filename="math_99.txt"):
    with open(filename, "w", encoding="utf-8") as file:
        for problem in problems:
            file.write(problem + "\n")

if __name__ == "__main__":
    math_problems = generate_math_problems()
    save_problems_to_file(math_problems)
    print(f"{len(math_problems)}道数学题已生成并保存到文件 'math_99.txt'。")
