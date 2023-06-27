- Do post-order traversal
- Start from the bottom of the node
- Initialize max_path = -inf
- create a recursive function -> gain_from_subtree(node)
- in this function, keep calculating the gain_from_left and gain_from_right sums and make them 0 if they are negative
- then calculate the max_path = max( max_path, gain_from_left + gain_from_right + node.val)
- and then return in the recursive function - > max(gain_from_left + node.val, gain_from_right + node.val)
- out the recursive function call the gain_from_subtree recursive function by passing the root(this is where the code actually starts
- finally outside the recursive function, return max_path

​
