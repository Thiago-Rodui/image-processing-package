from image_processing.utils.plot import plot_image, plot_images
import cv2

# Carregar uma imagem
image = cv2.imread('caminho/para/imagem.jpg', cv2.IMREAD_GRAYSCALE)

# Plotar uma única imagem
plot_image(image, title='Imagem Original')

# Carregar mais imagens
image_blur = cv2.GaussianBlur(image, (5, 5), 0)
image_sharpen = cv2.filter2D(image, -1, kernel)

# Plotar múltiplas imagens
plot_images([image, image_blur, image_sharpen], titles=['Original', 'Blur', 'Sharpen'])