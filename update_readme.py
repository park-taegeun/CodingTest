"""
README 자동 갱신 스크립트

easy/ medium/ hard/ 폴더를 스캔해서
진행 상황 표와 풀이 목록을 자동으로 다시 만든다.

사용법:
    python update_readme.py
"""

import os

# 난이도별 설정 (폴더명, 표시 이름, 이모지)
LEVELS = [
    ("easy", "Easy", "🟢"),
    ("medium", "Medium", "🟡"),
    ("hard", "Hard", "🔴"),
]


def parse_filename(filename):
    """
    '001_two_sum.py' -> (1, 'Two Sum')
    파일명 규칙에 안 맞으면 None 반환
    """
    if not filename.endswith(".py"):
        return None
    name = filename[:-3]  # .py 제거
    parts = name.split("_", 1)  # 첫 '_'로만 분리
    if len(parts) != 2:
        return None
    num_str, title_str = parts
    if not num_str.isdigit():
        return None
    number = int(num_str)
    # two_sum -> Two Sum
    title = " ".join(word.capitalize() for word in title_str.split("_"))
    return number, title


def collect_problems():
    """각 난이도 폴더에서 풀이 파일을 수집"""
    result = {}
    for folder, _, _ in LEVELS:
        problems = []
        if os.path.isdir(folder):
            for fname in sorted(os.listdir(folder)):
                parsed = parse_filename(fname)
                if parsed:
                    number, title = parsed
                    path = f"{folder}/{fname}"
                    problems.append((number, title, path))
        problems.sort(key=lambda x: x[0])  # 문제 번호순 정렬
        result[folder] = problems
    return result


def build_readme(problems):
    """수집한 데이터로 README 전체 문자열을 만든다"""
    counts = {folder: len(problems[folder]) for folder, _, _ in LEVELS}
    total = sum(counts.values())

    lines = []
    add = lines.append

    # 헤더
    add('<div align="center">')
    add("")
    add("# 🧩 CodingTest")
    add("")
    add("**파이썬으로 푸는 LeetCode 풀이 저장소**")
    add("")
    add("![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)")
    add("![LeetCode](https://img.shields.io/badge/LeetCode-FFA116?style=flat-square&logo=leetcode&logoColor=white)")
    add("![License](https://img.shields.io/badge/license-MIT-green?style=flat-square)")
    add("")
    add("꾸준히 한 문제씩 🌱")
    add("")
    add("</div>")
    add("")
    add("---")
    add("")

    # 진행 상황
    add("## 📊 진행 상황")
    add("")
    add("| 난이도 | 푼 문제 수 |")
    add("| :---: | :---: |")
    for folder, name, emoji in LEVELS:
        add(f"| {emoji} {name} | {counts[folder]} |")
    add(f"| **합계** | **{total}** |")
    add("")
    add("---")
    add("")

    # 폴더 구조
    add("## 📂 폴더 구조")
    add("")
    add("```")
    add("CodingTest/")
    add("├── easy/          # 🟢 Easy 난이도 풀이")
    add("├── medium/        # 🟡 Medium 난이도 풀이")
    add("├── hard/          # 🔴 Hard 난이도 풀이")
    add("└── template.py    # 풀이 시작용 템플릿")
    add("```")
    add("")
    add("---")
    add("")

    # 파일명 규칙
    add("## 📝 파일명 규칙")
    add("")
    add("```")
    add("문제번호_문제이름.py")
    add("```")
    add("")
    add("> 예시: `001_two_sum.py`, `020_valid_parentheses.py`")
    add("")
    add("---")
    add("")

    # 커밋 규칙
    add("## 💬 커밋 규칙")
    add("")
    add("```")
    add("type: 문제번호. 문제이름")
    add("```")
    add("")
    add("| type | 사용 시점 | 예시 |")
    add("| :---: | :--- | :--- |")
    add("| `solve` | 문제 풀이 추가 | `solve: 1. Two Sum` |")
    add("| `fix` | 기존 풀이 수정 | `fix: 1. Two Sum 예외처리` |")
    add("| `refactor` | 풀이 개선 (더 나은 방법) | `refactor: 1. Two Sum 해시맵 풀이로` |")
    add("| `docs` | README 등 문서 수정 | `docs: 진행 상황 업데이트` |")
    add("")
    add("> 처음엔 `solve`만 써도 충분해. 나머지는 필요할 때 골라 쓰면 돼.")
    add("")
    add("---")
    add("")

    # 풀이 목록
    add("## 🗂 풀이 목록")
    add("")
    for folder, name, emoji in LEVELS:
        add(f"### {emoji} {name}")
        add("")
        add("| # | 문제 | 풀이 |")
        add("| :---: | :--- | :---: |")
        if problems[folder]:
            for number, title, path in problems[folder]:
                add(f"| {number} | {title} | [🔗]({path}) |")
        else:
            add("| - | - | - |")
        add("")
    add("---")
    add("")
    add('<div align="center">')
    add("")
    add("**Keep going! 🚀**")
    add("")
    add("</div>")
    add("")

    return "\n".join(lines)


def main():
    problems = collect_problems()
    readme = build_readme(problems)
    with open("README.md", "w", encoding="utf-8") as f:
        f.write(readme)

    total = sum(len(v) for v in problems.values())
    print("✅ README.md 갱신 완료!")
    for folder, name, emoji in LEVELS:
        print(f"   {emoji} {name}: {len(problems[folder])}개")
    print(f"   합계: {total}개")


if __name__ == "__main__":
    main()
