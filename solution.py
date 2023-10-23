import tkinter as tk
from fuzzywuzzy import fuzz


def show_solution():
    problem_query = entry.get()
    with open(r'q&a.txt', 'r', encoding='utf-8') as file:
        lines = file.readlines()

    best_match_ratio = 0  # 最佳匹配比例
    best_match_solution = None  # 最佳匹配的解决办法

    for line in lines:
        problem_solution = line.strip().split('：')
        if len(problem_solution) != 2:
            continue

        problem = problem_solution[0]
        solution = problem_solution[1].strip()

        match_ratio = fuzz.partial_ratio(problem, problem_query)

        if match_ratio > best_match_ratio:
            best_match_ratio = match_ratio
            best_match_solution = solution

    if best_match_solution:
        result_text = best_match_solution
    else:
        result_text = '未找到解决办法'

    result.delete(1.0, tk.END)  # 清空结果文本框
    result.insert(tk.END, result_text)


root = tk.Tk()
problem_label = tk.Label(root, text='请输入问题:')
problem_label.pack()

entry = tk.Entry(root)
entry.pack()

button = tk.Button(root, text='解决', command=show_solution)
button.pack()

result_label = tk.Label(root, text='回答:')
result_label.pack()

result = tk.Text(root)
result.pack()


# 在用户输入问题时自动获取答案
def get_answer(event):
    show_solution()


entry.bind('<Return>', get_answer)

root.mainloop()