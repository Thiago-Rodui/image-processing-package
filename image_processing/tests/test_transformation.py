from image_processing.processing.transformation import resize_image, rotate_image, flip_image
import cv2

# Carregar uma imagem
image = cv2.imread('caminho/para/imagem.jpg')

# Redimensionar a imagem
resized_image = resize_image(image, (200, 200))

# Rotacionar a imagem
rotated_image = rotate_image(image, 45)

# Espelhar a imagem horizontalmente
flipped_image = flip_image(image, 1)

# Salvar as imagens resultantes
cv2.imwrite('caminho/para/imagem_redimensionada.jpg', resized_image)
cv2.imwrite('caminho/para/imagem_rotacionada.jpg', rotated_image)
cv2.imwrite('caminho/para/imagem_espelhada.jpg', flipped_image)