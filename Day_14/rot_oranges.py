def rot(grid):
	if len(grid)==0:
		return -1
	row_len=len(grid)
	col_len=len(grid[0])
	s=[]
	total=0
	for i in range(row_len):
		for j in range(col_len):
			if grid[i][j]==2:
				s.append([i,j])
			if grid[i][j]!=0:
				total=total+1


	if total==0:
		return -1
	count_min=0
	cnt=0
	dx=[0,0,-1,1]
	dy=[-1,1,0,0]
	while len(s)!=0:
		size=len(s)
		print(size)
		print(s)
		cnt=cnt+size
		for i in range(size):
			point=s.pop(0)
			for j in range(4):
				x=point[0]+dx[j]
				y=point[1]+dy[j]
				if x<0 or x>=row_len or y<0 or y>=col_len or grid[x][y]==0 or grid[x][y]==2:
					continue
				grid[x][y]=2
				s.append([x,y])
		if len(s)!=0:
			count_min=count_min+1
	
	if total==cnt:
		return count_min
	else:
		return -1


v = [[2, 1, 0, 2, 1],
	 [1, 0, 1, 2, 1],
	 [1, 0, 0, 2, 1]]
res=rot(v)
print(res)
