# 1.Two Sum - Memomizaion

- Recognize how output can be saved so don't brute force. Since there are two numbers, we can store the difference in a hashmap.


# 167. Two Sum II
- Recognize how sorted -> use double pointers with left right movements

# 15. Three sum
- Check conditions. When asked for non duplicates, check it as base case.
- Unerstand the return type and not exit loop too early.
- Understand that three sum reduces to two sum and you can reuse understanding. Use two sum II becuase it is Sorted. Sort is nlogn
O(nlogn) + O(n^2) -> Reduces to O(nlogn)

# 121. Best time to buy stock.
- Know how to reduce sliding window problem down to finding the smallest and highest index that is valid from left right chronologically. 
