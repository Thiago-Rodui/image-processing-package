from image_processing.processing.combination import blend_images, concatenate_images
import cv2

# Carregar duas imagens
image1 = cv2.imread('caminho/para/imagem1.jpg')
image2 = cv2.imread('caminho/para/imagem2.jpg')

# Combinar as imagens usando blending
blended_image = blend_images(image1, image2, alpha=0.7)

# Concatenar as imagens horizontalmente
concatenated_image = concatenate_images(image1, image2, axis=1)

# Salvar as imagens resultantes
cv2.imwrite('caminho/para/imagem_blended.jpg', blended_image)
cv2.imwrite('caminho/para/imagem_concatenated.jpg', concatenated_image)