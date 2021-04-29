with open("file1.txt") as file1:
    nums1 = [int(num) for num in file1.readlines() if num != "\n"]

with open("file2.txt") as file2:
    nums2 = [int(num) for num in file2.readlines() if num != "\n"]

print(nums1)
print(nums2)

result = [number for number in nums2 if number in nums1]

# Write your code above 👆

print(result)
