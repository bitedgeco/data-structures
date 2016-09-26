def merge_sort(lst):
    """Preform merge sorting on a list."""
    if len(lst) > 1:
        mid = len(lst) // 2
        left = lst[:mid]
        right = lst[mid:]

        merge_sort(left)
        merge_sort(right)

        left_idx = 0
        right_idx = 0
        lst_idx = 0

        while left_idx < len(left) and right_idx < len(right):
            if left[left_idx] < right[right_idx]:
                lst[lst_idx] = left[left_idx]
                left_idx += 1
            else:
                lst[lst_idx] = right[right_idx]
                right_idx += 1
            lst_idx += 1

        while left_idx < len(left):
            lst[lst_idx] = left[left_idx]
            left_idx += 1
            lst_idx += 1
        
        while right_idx < len(right):
            lst[lst_idx] = right[right_idx]
            right_idx += 1
            lst_idx += 1
        

