# Starting at the top of the triangle below and moving to adjacent numbers on the
# row below, the maximum total from top to bottom is 23.

# 3
# 7 4
# 2 4 6
# 8 5 9 3

# That is, 3 + 7 + 4 + 9 = 23. Find the maximum total from top to bottom of the 
# triangle below:


f = open("triangle.txt")
triangle_str = f.read()
tri_data = triangle_str.strip().split("\n")
tri_data.reverse()
tri_data = [[int(x) for x in row.split()] for row in tri_data]


def main():
    for row in range(len(tri_data)):
        for col in range(len(tri_data[row])-1):
            tri_data[row+1][col] += max(tri_data[row][col],tri_data[row][col+1])

    print ("Maximum sum is %d" % tri_data[-1][0])


if __name__ == "__main__":
    main()
    
    

