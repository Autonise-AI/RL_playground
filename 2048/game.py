import numpy as np
import matplotlib.pyplot as plt
import tkinter as tk

class game_2048():

	def __init__(self):

		self.size = [4, 4]
		self.matrix = np.zeros(self.size)
		self.prob_4_2 = 0.001
		self.ax = plt.figure(num=1)
		self.color_map = {0: [255, 255, 255], 2:[0, 128, 128], 4:[0, 160, 160], 8:[0, 180, 180],
						 16:[0, 200, 200], 32: [0, 220, 220], 64:[0, 255, 255], 128:[120, 0, 0],
						 256:[150, 0, 0], 512:[180, 0, 0], 1024:[210, 0, 0], 2048:[255, 0, 0]}

	def random_add(self):

		np.random.seed()

		possible = np.where(self.matrix.ravel() == 0)[0]

		t = np.random.choice(possible, 1)

		n = True if np.random.randint(100000)/100000 < self.prob_4_2 else False

		if n:
			self.matrix[t//self.size[1],t%self.size[1]] = 4
		else:
			self.matrix[t//self.size[1],t%self.size[1]] = 2

		return self.check_game_over()

	def check_game_over(self):

		copy = self.matrix.copy()
		check = True
		operations = [self.move_up, self.move_down, self.move_left, self.move_right]

		for o in operations:
			o()
			if check and np.all(copy == self.matrix):
				check = True
			else:
				check = False
				break

		self.matrix = copy
		
		if check:
			return True

		return False

	def show(self, val):

		image = np.zeros([self.size[0], self.size[1], 3]).astype(np.uint8)
		for i in range(self.size[0]):
			for j in range(self.size[1]):
				image[i, j] = np.array(self.color_map[self.matrix[i, j]])


		# plt.matshow(self.matrix, 1)
		plt.imshow(image.astype(np.uint8))
		plt.pause(val)

	def move_up(self):

		copy = self.matrix.copy()

		new = np.zeros(self.size)

		for j in range(self.size[1]):
			filled = 0
			prev = 0
			for i in range(self.size[0]):
				if self.matrix[i, j] != 0:
					if self.matrix[i, j] == prev:
						new[filled - 1, j] = 2*self.matrix[i, j]
						prev = 0
					else:
						new[filled, j] = self.matrix[i, j]
						filled += 1
						prev = self.matrix[i, j]

		self.matrix = new

		return not np.all(copy == self.matrix)

	def move_down(self):

		copy = self.matrix.copy()

		self.matrix = np.flip(self.matrix, 0)
		self.move_up()
		self.matrix = np.flip(self.matrix, 0)

		return not np.all(copy == self.matrix)

	def move_right(self):

		copy = self.matrix.copy()

		self.matrix = np.transpose(self.matrix)

		self.move_down()

		self.matrix = np.transpose(self.matrix)

		return not np.all(copy == self.matrix)

	def move_left(self):

		copy_left = self.matrix.copy()

		self.matrix = np.transpose(self.matrix)

		self.move_up()

		self.matrix = np.transpose(self.matrix)

		return not np.all(copy_left == self.matrix)

	def refresh(self):
		self.__init__()
		self.random_add()
		self.show(0.1)

	def add(self, check):
		if check:
			game_over = self.random_add()
			self.show(0.1)
			if game_over:
				print('Game Over')
				return 0
			return 1
		else:
			print('Illegal Move')
			return 1

	def left(self):
		check = self.move_left()
		if not self.add(check):
			break

	def right(self):
		check = self.move_right()
		if not self.add(check):
			break

	def up(self):
		check = self.move_up()
		if not self.add(check):
			break

	def down(self):
		check = self.move_down()
		if not self.add(check):
			break
	
	def play(self):

		root = tk.Tk()
		frame = tk.Frame(root)
		frame.pack()

		button = tk.Button(frame, text="QUIT", fg="red",command=quit)
		button.pack(side=tk.LEFT)
		slogan = tk.Button(frame,text="UP",command=self.up)
		slogan.pack(side=tk.LEFT)
		slogan = tk.Button(frame,text="DOWN",command=self.down)
		slogan.pack(side=tk.LEFT)
		slogan = tk.Button(frame,text="RIGHT",command=self.right)
		slogan.pack(side=tk.LEFT)
		slogan = tk.Button(frame,text="LEFT",command=self.left)
		slogan.pack(side=tk.LEFT)
		slogan = tk.Button(frame,text="REFRESH",command=self.refresh)
		slogan.pack(side=tk.LEFT)

		root.mainloop()


if __name__ == "__main__":

	env = environment()
	env.play()

	# for i in range(1000):
	# 	if i!=0 and env.check_game_over():
	# 		env.show(1)
	# 		print('Game Over')
	# 		break
	# 	env.random_add()
	# 	if i % 100 == 0:
	# 		env.show(1)
	# 	if env.move_left():
	# 		continue
	# 	if env.move_down():
	# 		continue
	# 	if env.move_right():
	# 		continue
	# 	if env.move_up():
	# 		continue

		

		

