- output array -> levels = []
- first, if the root is none: return ​levels
- create a recursive function -> helper(node, level)
- when the len(levels) == level -> its time to append a new [] in the levels array
- and then append the node.val to the [] newly added array in the levels array
- then for the left first (since we are traversing left to right) - > if node.left:
                                                                        helper(node.left, level+1)
- same for the right of the node
- finally outside of the recursive function, call helper(root, 0)
- return levels
