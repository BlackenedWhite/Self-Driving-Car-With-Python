import numpy as np
import cv2
import time

W = [1, 0, 0]
A = [0, 1, 0]
D = [0, 0, 1]
NM = [0, 0, 0]

for file_num in range(1, 302):
	print(file_num)
	data = np.load('newData/fixed/collected_data-{}.npy'.format(file_num))
	imgs = np.array(data[0])
	outs = np.array(data[1])
	data = []
	print("data loaded...")

	# shuffle data
	s = np.arange(imgs.shape[0])
	np.random.shuffle(s)
	imgs = imgs[s]
	outs = outs[s]
	print("data shuffled...")

	# balancing data
	forwards = np.array([[0, 0, 0]], dtype=int)
	forwards = np.delete(forwards, 0, 0)
	lefts = np.array([[0, 0, 0]], dtype=int)
	lefts = np.delete(lefts, 0, 0)
	rights = np.array([[0, 0, 0]], dtype=int)
	rights = np.delete(rights, 0, 0)
	# print("1")

	forwards_imgs = np.array([[]], dtype=(np.uint8))
	forwards_imgs.shape = (0, 100, 100, 4)
	lefts_imgs = np.array([[]], dtype=(np.uint8))
	lefts_imgs.shape = (0, 100, 100, 4)
	rights_imgs = np.array([[]], dtype=(np.uint8))
	rights_imgs.shape = (0, 100, 100, 4)
	# print("2")

	for i in range(imgs.shape[0]):
		# print("sample number: " + str(i))
		if list(outs[i]) == W:
			forwards = np.append(forwards, [outs[i]], axis=0)
			forwards_imgs = np.append(forwards_imgs, [imgs[i]], axis=0)
		elif list(outs[i]) == A:
			lefts = np.append(lefts, [outs[i]], axis=0)
			lefts_imgs = np.append(lefts_imgs, [imgs[i]], axis=0)
		elif list(outs[i]) == D:
			rights = np.append(rights, [outs[i]], axis=0)
			rights_imgs = np.append(rights_imgs, [imgs[i]], axis=0)
		else:
			print("****ERRRRROR NO MATCHES****")

	# Clear
	# data = []
	# imgs = []
	# outs = []

	# Under Sampling
	forwards = forwards[:len(lefts)][:len(rights)]
	lefts = lefts[:len(forwards)]
	rights = rights[:len(forwards)]

	forwards_imgs = forwards_imgs[:len(lefts_imgs)][:len(rights_imgs)]
	lefts_imgs = lefts_imgs[:len(forwards_imgs)]
	rights_imgs = rights_imgs[:len(forwards_imgs)]

	n_imgs = forwards_imgs
	n_imgs = np.append(n_imgs, rights_imgs, axis=0)
	n_imgs = np.append(n_imgs, lefts_imgs, axis=0)
	n_outs = forwards
	n_outs = np.append(n_outs, rights, axis=0)
	n_outs = np.append(n_outs, lefts, axis=0)

	# shuffle data
	s = np.arange(imgs.shape[0])
	np.random.shuffle(s)
	imgs = list(imgs[s])
	outs = list(outs[s])
	print("data shuffled...")

	print("Saving Data...")
	n_data = [list(n_imgs), list(n_outs)]
	# imgs = []
	# outs = []
	np.save("newData/balanced/data_balanced-{}.npy".format(file_num), n_data)
