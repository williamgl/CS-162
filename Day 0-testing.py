# Author: Gan Li
# Date: 8/22/21 7:52 下午
# Description: 随便测试的内容
def right_justify(s):
    """3.14 exercise 1"""
    length = len(s)
    return ' ' * (70 - length) + s


def main():
    string = input('Please type in a string less than 70 characters:')
    print(right_justify(string))


if __name__ == "__main__":
    main()
