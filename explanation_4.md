------ Overview -------------

To give context, an Active Directory is a term developed by Microsoft used in server systems to be able to quickly find users within groups of groups, etc., along with other properties or "directory-based identity-related services" (cite # 1). 

In this problem, utilizing the helper functions provided first iterate over the group passed in to the `is_user_in_group` function and with a conditional statement determine if that group is equal to a particular category. If so, then iterate over user that was passed in and confirm whether that user is in the group. 

1. for loop = O(N) * 2
2. if statement = O(1) * 4
3. result = O(N^2) 

Citation:
1. https://en.wikipedia.org/wiki/Active_Directory