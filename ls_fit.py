import numpy as np
import matplotlib.pyplot as plt
import transforms3d
import IPython

def plot_points(ps, marker='b+', label=''):
	plt.plot(ps[0, :], ps[1, :], marker, label=label)


def ls_fit(s, d):

	n = s.shape[1]

	sc = np.tile(np.array([np.mean(s, axis=1)]).T, (1, n))
	dc = np.tile(np.array([np.mean(d, axis=1)]).T, (1, n))
	s_ = s - sc
	d_ = d - dc

	H = np.zeros((2, 2), dtype=float)

	for i in range(n):
		H = H + np.matmul(np.array([s_[:, i]]).T, np.array([d_[:, i]]))

	U, S, VT = np.linalg.svd(H, full_matrices=True)

	R = np.matmul(VT.T, U.T)
	t = dc[:, 0] - np.matmul(R, sc[:, 0])

	return R, t

if __name__ == '__main__':
	
	# pure translation example
	# s = np.zeros((2, 3), dtype=float)
	# s[:, 0] = [-1, 0]
	# s[:, 1] = [0, 0]
	# s[:, 2] = [1, 0]
	# d = s + 5

	# 45 degree rotation, no translation example
	s = np.zeros((2, 3), dtype=float)
	s[:, 0] = [-1, 0]
	s[:, 1] = [0, 0]
	s[:, 2] = [1, 0]
	d = np.zeros((2, 3), dtype=float)
	d[:, 0] = [-1.0/np.sqrt(2), -1.0/np.sqrt(2)]
	d[:, 1] = [0, 0]
	d[:, 2] = [1.0/np.sqrt(2), 1.0/np.sqrt(2)]

	# 45 degree rotation with translation example
	# s = np.zeros((2, 3), dtype=float)
	# s[:, 0] = [-1, 0]
	# s[:, 1] = [0, 0]
	# s[:, 2] = [1, 0]
	# d = np.zeros((2, 3), dtype=float)
	# d[:, 0] = [2 - 1.0/np.sqrt(2), 2 - 1.0/np.sqrt(2)]
	# d[:, 1] = [2, 2]
	# d[:, 2] = [2 + 1.0/np.sqrt(2), 2 + 1.0/np.sqrt(2)]

	R, t = ls_fit(s, d)
	n = s.shape[1]
	de = np.matmul(R, s) + np.tile(np.array([t]).T, (1, n))

	plot_points(s, 'bo', 'orig')
	plot_points(d, 'go', 'dest')
	plot_points(de, 'r+', 'ls fit')
	plt.legend()
	plt.xlabel('x')
	plt.ylabel('y')
	plt.title('2D Least Squares Fit Example')

	IPython.embed()

