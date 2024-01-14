def main():
    nums = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    sort_numbers_imperative(nums)
    sorted_nums = sort_numbers_declarative(nums)
    print("Отсортированный список в императивном стиле:", nums)
    print("Отсортированный список в декларативном стиле:", sorted_nums)


def sort_numbers_imperative(nums):
    n = len(nums)
    for i in range(n):
        for j in range(0, n - i - 1):
            if nums[j] < nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]


def sort_numbers_declarative(nums):
    return sorted(nums, reverse=True)


if __name__ == "__main__":
    main()
