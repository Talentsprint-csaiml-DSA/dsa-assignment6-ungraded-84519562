def can_pack(box1,box2):
    return box1[0] < box2[0] and box1[1] < box2[1] and box1[2] < box2[2]
def longest_box_sequence(boxes):
    #ToDo 
    #Write your code here.
    boxes=[sorted(box) for box in boxes]
    boxes.sort()
    noOfBoxes=len(boxes)
    dp=[1]*noOfBoxes
    for i in range (1,noOfBoxes):
        for j in range(i):
            if can_pack(boxes[j],boxes[i]):
                dp[i]=max(dp[i],dp[j] +1)
    return max(dp)

# print(longest_box_sequence([ (1, 5, 6), (3, 4, 5), (1, 2, 3), (6, 2, 8), (5, 5,1), (2, 3,1) ]))


    
