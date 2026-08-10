class Solution:
    def getBiggestThree(self, grid: List[List[int]]) -> List[int]:
        max1,max2,max3 = 0,0,0
        rows = len(grid)
        columns = len(grid[0])
        for i in range(rows):
            for j in range(columns):
                sum_rhombus = 0
                min_length_to_border = min( #полудиаметр ромба
                    abs(0-i), abs(rows-1-i), abs(0-j), abs(columns-1-j)
                    )
                if min_length_to_border == 0:
                    sum_rhombus = grid[i][j]
                    if max1<sum_rhombus:
                        max3, max2, max1 = max2, max1, sum_rhombus
                    elif max2 < sum_rhombus and sum_rhombus != max1:
                        max3, max2 = max2, sum_rhombus
                    elif max3 < sum_rhombus and sum_rhombus != max2 and sum_rhombus != max1:
                        max3 = sum_rhombus

                else:
                    for n in range(0,min_length_to_border+1):
                        sum_rhombus = 0
                        for k in range(i-n,i+n+1):
                            for m in range(j-n,j+n+1):
                                if abs(k-i) + abs(m-j) == n:
                                    sum_rhombus += grid[k][m]
                        if max1<sum_rhombus:
                            max3, max2, max1 = max2, max1, sum_rhombus
                        elif max2 < sum_rhombus and sum_rhombus != max1:
                            max3, max2 = max2, sum_rhombus
                        elif max3 < sum_rhombus and sum_rhombus != max2 and sum_rhombus != max1:
                            max3 = sum_rhombus
                
        

        max_arr = []        
        if max1 > 0: 
            max_arr.append(max1)
        if max2 > 0: 
            max_arr.append(max2)
        if max3 > 0:
            max_arr.append(max3)

        return sorted(list(set(max_arr)), reverse = True)
