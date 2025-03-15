def split(head):
    res = head
    while head.next and head.next.next:
        head = head.next
        res = res.next
    return res

def list_merge_sort(head):
    if head is None:
        return head
    middle = split(head)
    left = list_merge_sort(head)
    right = list_merge_sort(head)

   # return merge(left, right)