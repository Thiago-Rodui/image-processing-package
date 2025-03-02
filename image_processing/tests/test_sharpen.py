from image_processing.filters.sharpen import apply_sharpen, apply_unsharp_mask
import cv2

# Carregar uma imagem
image = cv2.imread('caminho/para/imagem.jpg')

# Aplicar filtro de nitidez
sharpened_image = apply_sharpen(image)

# Aplicar filtro de máscara de nitidez
unsharp_mask_image = apply_unsharp_mask(image, kernel_size=(5, 5), sigma=1.0, amount=1.5, threshold=0)

# Salvar as imagens resultantes
cv2.imwrite('caminho/para/imagem_sharpened.jpg', sharpened_image)
cv2.imwrite('caminho/para/imagem_unsharp_mask.jpg', unsharp_mask_image)