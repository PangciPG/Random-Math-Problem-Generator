import random

def generate_math_problems(num_problems=1000):
    problems = []
    last_problem = None
    for i in range(num_problems):
        while True:
            # 第一次运算
            if random.choice([True, False]):
                # 加法
                a = random.randint(1, 9)
                b = random.randint(1, 10 - a)
                first_part = f"{a} + {b}"
            else:
                # 减法
                a = random.randint(2, 10)
                b = random.randint(1, a - 1)
                first_part = f"{a} - {b}"

            # 计算第一次运算的结果
            first_result = eval(first_part)

            # 确保第一次运算的结果大于等于1，以便进行第二次运算
            if first_result < 1 or first_result >= 10:
                continue

            # 第二次运算
            if random.choice([True, False]):
                # 加法
                c = random.randint(1, 10 - first_result)
                second_part = f" + {c}"
            else:
                # 减法
                c = random.randint(1, first_result)
                second_part = f" - {c}"

            # 构建完整问题
            problem = f"{first_part}{second_part} = "

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

def save_problems_to_file(problems, filename="math_10x2.txt"):
    with open(filename, "w", encoding="utf-8") as file:
        for problem in problems:
            file.write(problem + "\n")

if __name__ == "__main__":
    math_problems = generate_math_problems()
    save_problems_to_file(math_problems)
    print(f"{len(math_problems)}道数学题已生成并保存到文件 'math_10x2.txt'。")
