"""BMI 指标计算器

身高使用米（m），体重使用千克（kg）。
"""


def main():
    try:
        height = float(input("请输入您的身高（米）："))
        weight = float(input("请输入您的体重（千克）："))
    except ValueError:
        print("输入无效，请输入数字。")
        return

    if height <= 0 or weight <= 0:
        print("身高和体重必须大于 0。")
        return

    bmi = weight / (height ** 2)

    if bmi < 18.5:
        result = "偏瘦"
    elif bmi < 24:
        result = "正常"
    elif bmi < 28:
        result = "偏胖"
    else:
        result = "肥胖"

    print(f"您的 BMI 指标为：{bmi:.2f}")
    print(f"体重状态：{result}")
    print("提示：BMI 仅供参考，不能代替专业健康评估。")


if __name__ == "__main__":
    main()
