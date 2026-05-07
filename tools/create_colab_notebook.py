import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "notebooks" / "ipp_runnable_companion.ipynb"


def md(source):
    return {
        "cell_type": "markdown",
        "metadata": {},
        "source": source.strip().splitlines(True),
    }


def code(source):
    return {
        "cell_type": "code",
        "execution_count": None,
        "metadata": {},
        "outputs": [],
        "source": source.strip().splitlines(True),
    }


chapters = [
    ("1-0. Colaboratory (Colab) の使い方", "https://utokyo-ipp.github.io/1/1-0.html", [
        code("""
# セルを順番に実行すると、変数の状態が次の処理に引き継がれます。
x = 1
x = x + 2
x
"""),
        code("""
# Notebookでは最後の式の値が表示されます。printとの違いを見てみましょう。
message = "Colabで実行中"
print(message)
message.upper()
"""),
    ]),
    ("1-1. 数値演算", "https://utokyo-ipp.github.io/1/1-1.html", [
        code("""
print("割り算:", 7 / 2)
print("整数除算:", 7 // 2)
print("余り:", 7 % 2)
print("べき乗:", 2 ** 3 ** 2)
"""),
        code("""
import math

print(math.sqrt(2))
print(0.1 + 0.2)
print((0.1 + 0.2) == 0.3)
print(math.isclose(0.1 + 0.2, 0.3))
"""),
    ]),
    ("1-2. 変数と関数の基礎", "https://utokyo-ipp.github.io/1/1-2.html", [
        code("""
def ft_to_cm(feet, inch):
    return (feet * 12 + inch) * 2.54

height = ft_to_cm(5, 7)
print(height)
"""),
        code("""
def square_print(x):
    print(x * x)

def square_return(x):
    return x * x

a = square_print(3)
b = square_return(3)
print("printする関数の返値:", a)
print("returnする関数の返値:", b)
"""),
    ]),
    ("1-3. 論理・比較演算と条件分岐の基礎", "https://utokyo-ipp.github.io/1/1-3.html", [
        code("""
def sign(x):
    if x > 0:
        return "plus"
    if x < 0:
        return "minus"
    return "zero"

for value in [3, 0, -2]:
    print(value, sign(value))
"""),
        code("""
def is_even(n):
    return n % 2 == 0

print(is_even(4))
print(is_even(5))
print(not (3 < 2 or 4 == 4))
"""),
    ]),
    ("1-4. テストとデバッグ", "https://utokyo-ipp.github.io/1/1-4.html", [
        code("""
def half(x):
    return x / 2

assert half(4) == 2
assert half(3) == 1.5
print("テスト通過")
"""),
        code("""
def safe_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "0では割れません"

print(safe_divide(10, 2))
print(safe_divide(10, 0))
"""),
    ]),
    ("2-1. 文字列 (string)", "https://utokyo-ipp.github.io/2/2-1.html", [
        code("""
s = "Python"
print(s[0], s[1], s[-1])
print(s[1:4])
print(s[::-1])
"""),
        code("""
text = "  banana\\n"
print(text.strip())
print(text.count("a"))
print(text.replace("banana", "orange"))
print("na" in text)
"""),
    ]),
    ("2-2. リスト (list)", "https://utokyo-ipp.github.io/2/2-2.html", [
        code("""
xs = [3, 1, 2]
print("sorted:", sorted(xs))
print("元のxs:", xs)
xs.sort()
print("sort後のxs:", xs)
"""),
        code("""
xs = [1, 2, 3]
same = xs
copy = xs[:]
same.append(4)
copy.append(5)
print("xs:", xs)
print("same:", same)
print("copy:", copy)
"""),
    ]),
    ("2-3. 条件分岐", "https://utokyo-ipp.github.io/2/2-3.html", [
        code("""
def grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    else:
        return "D"

for score in [95, 82, 71, 60]:
    print(score, grade(score))
"""),
        code("""
x = 0
if x != 0 and 10 / x > 1:
    print("割りました")
else:
    print("短絡評価で安全にスキップ")
"""),
    ]),
    ("3-1. 辞書 (dictionary)", "https://utokyo-ipp.github.io/3/3-1.html", [
        code("""
scores = {"A": 80, "B": 90}
scores["C"] = 75
print(scores)
print(scores.get("D", 0))
"""),
        code("""
text = "banana"
counts = {}
for ch in text:
    counts[ch] = counts.get(ch, 0) + 1

for ch, count in counts.items():
    print(ch, count)
"""),
    ]),
    ("3-2. 繰り返し", "https://utokyo-ipp.github.io/3/3-2.html", [
        code("""
for i, ch in enumerate("abc", start=1):
    print(i, ch)

print(list(range(2, 9, 2)))
"""),
        code("""
total = 0
for n in [1, 2, 3, 4, 5]:
    if n == 2:
        continue
    if n == 5:
        break
    total += n
print(total)
"""),
    ]),
    ("3-3. 関数", "https://utokyo-ipp.github.io/3/3-3.html", [
        code("""
def area(width, height=1):
    return width * height

print(area(5))
print(area(height=2, width=5))
"""),
        code("""
def total(*nums):
    return sum(nums)

def apply_twice(f, x):
    return f(f(x))

print(total(1, 2, 3))
print(apply_twice(lambda x: x + 10, 5))
"""),
    ]),
    ("4-1. ファイル入出力の基本", "https://utokyo-ipp.github.io/4/4-1.html", [
        code("""
from pathlib import Path

path = Path("sample.txt")
path.write_text("alpha\\nbeta\\ngamma\\n", encoding="utf-8")

with path.open(encoding="utf-8") as f:
    print(f.readline().strip())
    print(f.read())
"""),
        code("""
from pathlib import Path

out = Path("output.txt")
with out.open("w", encoding="utf-8") as f:
    f.write("first\\n")
    f.write("second\\n")

print(out.read_text(encoding="utf-8"))
"""),
    ]),
    ("4-2. イテラブルとイテレータ", "https://utokyo-ipp.github.io/4/4-2.html", [
        code("""
it = iter([10, 20])
print(next(it))
print(next(it))

try:
    print(next(it))
except StopIteration:
    print("要素を使い切りました")
"""),
        code("""
it = enumerate(["a", "b"])
print(list(it))
print(list(it))
"""),
    ]),
    ("4-3. ディレクトリと木構造", "https://utokyo-ipp.github.io/4/4-3.html", [
        code("""
from pathlib import Path

root = Path("project")
(root / "data").mkdir(parents=True, exist_ok=True)
(root / "data" / "numbers.txt").write_text("1\\n2\\n3\\n", encoding="utf-8")

for path in sorted(root.rglob("*")):
    print(path)
"""),
        code("""
from pathlib import Path

path = Path("project") / "data" / "numbers.txt"
print(path)
print(path.parent)
print(path.name)
"""),
    ]),
    ("5-1. モジュールの使い方", "https://utokyo-ipp.github.io/5/5-1.html", [
        code("""
import math
from math import pi
import random as rd

print(math.sqrt(9))
print(pi)
print(rd.choice(["A", "B", "C"]))
"""),
    ]),
    ("5-2. モジュールの作り方", "https://utokyo-ipp.github.io/5/5-2.html", [
        code("""
from pathlib import Path
import importlib

Path("mycalc.py").write_text('''
def twice(x):
    return x * 2

def add(a, b):
    return a + b
'''.strip(), encoding="utf-8")

mycalc = importlib.import_module("mycalc")
print(mycalc.twice(5))
print(mycalc.add(2, 3))
"""),
        code("""
from pathlib import Path

Path("script_example.py").write_text('''
def main():
    print("直接実行されたときだけmainを呼びます")

if __name__ == "__main__":
    main()
'''.strip(), encoding="utf-8")

%run script_example.py
"""),
    ]),
    ("5-3. NumPyライブラリ", "https://utokyo-ipp.github.io/5/5-3.html", [
        code("""
import numpy as np

a = np.array([1, 2, 3])
b = np.array([10, 20, 30])
print(a + b)
print(a * 2)
print(a.dtype)
"""),
        code("""
import numpy as np

x = np.array([[1, 2, 3], [4, 5, 6]])
print(x.shape)
print(x[:, 1])
print(x[x > 3])
"""),
    ]),
    ("6-1. 内包表記", "https://utokyo-ipp.github.io/6/6-1.html", [
        code("""
print([x * x for x in range(6)])
print([x for x in range(10) if x % 2 == 0])
"""),
        code("""
rows = [[1, 2], [3, 4]]
print([x for row in rows for x in row])
print({x: x * x for x in range(4)})
"""),
    ]),
    ("6-2. 高階関数", "https://utokyo-ipp.github.io/6/6-2.html", [
        code("""
words = ["bbb", "a", "cc"]
print(sorted(words, key=len))
print(max(words, key=len))
"""),
        code("""
nums = [0, 1, 2, 3, 4]
print(list(map(lambda x: x + 1, nums)))
print(list(filter(lambda x: x % 2 == 1, nums)))
"""),
    ]),
    ("6-3. クラス", "https://utokyo-ipp.github.io/6/6-3.html", [
        code("""
class Counter:
    def __init__(self, value=0):
        self.value = value

    def up(self):
        self.value += 1

c = Counter()
c.up()
c.up()
print(c.value)
"""),
        code("""
class Animal:
    def speak(self):
        return "..."

class Dog(Animal):
    def speak(self):
        return "wan"

print(Animal().speak())
print(Dog().speak())
"""),
    ]),
    ("7-1. pandasライブラリ", "https://utokyo-ipp.github.io/7/7-1.html", [
        code("""
import pandas as pd

df = pd.DataFrame({
    "name": ["A", "B", "C"],
    "score": [70, 90, 80],
})
display(df)
display(df[df["score"] >= 80])
"""),
        code("""
import pandas as pd

df = pd.DataFrame({"score": [80, 90]}, index=["r1", "r2"])
print(df.loc["r2", "score"])
print(df.iloc[1, 0])
display(df.assign(pass_flag=df["score"] >= 85).sort_values("score"))
"""),
    ]),
    ("7-2. scikit-learnライブラリ", "https://utokyo-ipp.github.io/7/7-2.html", [
        code("""
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

iris = load_iris()
X_train, X_test, y_train, y_test = train_test_split(
    iris.data, iris.target, random_state=0
)
model = LogisticRegression(max_iter=200)
model.fit(X_train, y_train)
print(model.score(X_test, y_test))
print(model.predict(X_test[:5]))
"""),
        code("""
from sklearn.datasets import load_iris
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA

iris = load_iris()
clusters = KMeans(n_clusters=3, random_state=0, n_init=10).fit_predict(iris.data)
points = PCA(n_components=2).fit_transform(iris.data)
print(clusters[:10])
print(points[:3])
"""),
    ]),
    ("▲Jupyter Notebook の使い方", "https://utokyo-ipp.github.io/appendix/1-jupyter-notebook.html", [
        code("""
from IPython.display import Markdown, display

display(Markdown("**Markdown表示**もNotebook内で確認できます。"))
"""),
    ]),
    ("▲セット (set)", "https://utokyo-ipp.github.io/appendix/2-set.html", [
        code("""
a = {1, 2, 3}
b = {2, 3, 4}
print(a | b)
print(a & b)
print(a - b)
"""),
        code("""
s = set([1, 1, 2, 3])
s.add(4)
s.discard(99)
print(s)
"""),
    ]),
    ("▲再帰", "https://utokyo-ipp.github.io/appendix/3-recursion.html", [
        code("""
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

print(factorial(5))
"""),
        code("""
def total(xs):
    if xs == []:
        return 0
    return xs[0] + total(xs[1:])

print(total([1, 2, 3, 4]))
"""),
    ]),
    ("▲簡単なデータの可視化", "https://utokyo-ipp.github.io/appendix/3-visualization.html", [
        code("""
import matplotlib.pyplot as plt

x = [1, 2, 3]
y = [2, 4, 9]
plt.plot(x, y, marker="o")
plt.title("line plot")
plt.show()
"""),
        code("""
import matplotlib.pyplot as plt

plt.scatter([1, 2, 3, 4], [2, 1, 4, 3])
plt.title("scatter plot")
plt.show()
"""),
    ]),
    ("▲CSVファイルの入出力", "https://utokyo-ipp.github.io/appendix/4-csv.html", [
        code("""
import csv
from pathlib import Path

path = Path("scores.csv")
with path.open("w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["name", "score"])
    writer.writerow(["A", 80])
    writer.writerow(["B", 90])

with path.open(encoding="utf-8") as f:
    for row in csv.reader(f):
        print(row)
"""),
    ]),
    ("▲Bokehライブラリ", "https://utokyo-ipp.github.io/appendix/5-bokeh.html", [
        code("""
try:
    from bokeh.plotting import figure, output_notebook, show
    output_notebook()
    p = figure(title="Bokeh line")
    p.line([1, 2, 3], [2, 4, 3], line_width=2)
    show(p)
except Exception as e:
    print("Bokehの表示をスキップしました:", e)
"""),
    ]),
    ("▲Pythonスクリプトとコマンドライン実行", "https://utokyo-ipp.github.io/appendix/5-command.html", [
        code("""
import sys

fake_argv = ["script.py", "input.txt", "output.txt"]
print(fake_argv[0])
print(fake_argv[1:])
"""),
        code("""
from pathlib import Path

Path("hello_cli.py").write_text('''
import sys
print("args:", sys.argv[1:])
'''.strip(), encoding="utf-8")

!python hello_cli.py apple banana
"""),
    ]),
    ("▲Matplotlibライブラリ", "https://utokyo-ipp.github.io/appendix/5-matplotlib.html", [
        code("""
import matplotlib.pyplot as plt

fig, ax = plt.subplots()
ax.hist([1, 1, 2, 3, 3, 3])
ax.set_title("histogram")
plt.show()
"""),
        code("""
import matplotlib.pyplot as plt

plt.imshow([[1, 2], [3, 4]])
plt.colorbar()
plt.title("heatmap")
plt.savefig("heatmap.png")
plt.show()
"""),
    ]),
    ("▲正規表現", "https://utokyo-ipp.github.io/appendix/5-re.html", [
        code("""
import re

s = "id=123, code=45"
print(re.findall(r"\\d+", s))
print(re.sub(r"\\d+", "X", s))
"""),
        code("""
import re

text = "Python programming"
print(bool(re.search(r"^Python", text)))
print(re.split(r"\\s+", text))
"""),
    ]),
]


cells = [
    md("""
# IPP 実行用コンパニオンNotebook

東京大学「Pythonプログラミング入門」の章構成に合わせて、コードの動きをぽちぽち実行しながら確認するためのNotebookです。

教材本文やコードを丸ごと転載するのではなく、各章の概念を確認できる実行用セルとして作っています。各章タイトルの下に元教材へのリンクを付けています。
"""),
    code("""
import sys
print(sys.version)
"""),
]

for title, url, chapter_cells in chapters:
    cells.append(md(f"## {title}\\n\\n教材: {url}"))
    cells.extend(chapter_cells)


notebook = {
    "cells": cells,
    "metadata": {
        "colab": {
            "provenance": [],
            "toc_visible": True,
        },
        "kernelspec": {
            "display_name": "Python 3",
            "language": "python",
            "name": "python3",
        },
        "language_info": {
            "name": "python",
            "pygments_lexer": "ipython3",
        },
    },
    "nbformat": 4,
    "nbformat_minor": 5,
}

OUT.parent.mkdir(parents=True, exist_ok=True)
OUT.write_text(json.dumps(notebook, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(OUT)
print(f"{len(cells)} cells")
