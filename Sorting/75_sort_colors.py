def sortcolors(nums):
    l=0
    m=0
    r=len(nums)-1
    while m<=r:
        if nums[m]==0:
            nums[m],nums[l]=nums[l],nums[m]
            l+=1
            m+=1
        elif nums[m]==1:
            m+=1
        elif nums[m]==2:
            nums[m],nums[r]=nums[r],nums[m]
            r-=1
    return nums
print(sortcolors([2,2,1,0,2,1,1,0,0]))