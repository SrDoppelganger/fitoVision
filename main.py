import cv2 as cv

#analisa a imagem
imgPath = 'IMGs/pexels-cartist-3605370.jpg';
image = cv.imread(imgPath);

#configuração da janela
cv.namedWindow("girassol",cv.WINDOW_NORMAL)
cv.resizeWindow("girassol", 800, 800)


#mostra a imagem
cv.imshow('girassol',image)

cv.waitKey(0)
cv.destroyAllWindows()