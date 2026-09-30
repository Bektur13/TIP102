'''
On your platform, comments on posts are displayed in the order they are received. However, for a special feature, you need to reverse the order of comments before displaying them. Given a queue of comments represented as a list of strings, reverse the order using a stack.

def reverse_comments_queue(comments):
  pass
Example Usage:

print(reverse_comments_queue(["Great post!", "Love it!", "Thanks for sharing."]))

print(reverse_comments_queue(["First!", "Interesting read.", "Well written."]))

Input: 
Ouput: 
Edge: 
Plan: 


'''
# prob3

def is_symmetrical_title(title):
  l = 0
  r = len(title) - 1 

  while l <= r:
    # check l char and r char are equal
    if title[l] == ' ':
      l += 1
      continue
    elif title[r] == ' ':
      r -= 1
      continue
    
    if title[l].lower() != title[r].lower():
      print(f'idx{l} {title[l]} and idx{r} {title[r]}')
      return False

    l += 1
    r -= 1
    
  
  return True



print(is_symmetrical_title("A Santa at NASA"))
print(is_symmetrical_title("Social Media")) 




'''
You track your daily engagement rates as a list of integers, sorted in non-decreasing order. To analyze the impact of certain strategies, you decide to square each engagement rate and then sort the results in non-decreasing order.

Given an integer array engagements sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.

Your Task:

Read through the existing solution and add comments so that everyone in your pod understands how it works.
Modify the solution below to use the two-pointer technique.
'''

def engagement_boost(engagements):
    # Create new array full of 0s
    result = [0] * len(engagements)
    # Right pointer
    position = len(engagements) - 1

    l = 0
    r = len(engagements) - 1

    while l <= r:
      left_sq = engagements[l] ** 2
      right_sq = engagements[r] ** 2
      if left_sq >= right_sq:   
        result[position] = left_sq
        l += 1
      else:
        result[position] = right_sq 
        r -= 1

      position -= 1
    return result


# Time complexity: O(N), Space complexity: O(N)

print(engagement_boost([-4, -1, 0, 3, 10]))
print(engagement_boost([-7, -3, 2, 3, 11]))