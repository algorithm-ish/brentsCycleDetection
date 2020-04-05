import random

#generate random unique list of sampleSize nums from posNums range
def genSet(posNums, sampleSize):
    answer = []
    answerSize = 0
    while answerSize < sampleSize:
        r = random.randint(0, posNums)
        if r not in answer:
            answerSize += 1
            answer.append(r)
    return answer

#assumes nums is a set of unique values, returns mapped function
def mapper(nums):           
    fn = {}
    for key in nums:
        fn[key] = nums[random.randint(0,len(nums)-1)]
    return fn 
