from image_processing.filters.blur import apply_gaussian_blur, apply_median_blur, apply_bilateral_filter
import cv2

# Carregar uma imagem
image = cv2.imread('caminho/para/imagem.jpg')

# Aplicar desfoque gaussiano
gaussian_blur_image = apply_gaussian_blur(image, kernel_size=(5, 5), sigma=1)

# Aplicar desfoque mediano
median_blur_image = apply_median_blur(image, kernel_size=5)

# Aplicar filtro bilateral
bilateral_filter_image = apply_bilateral_filter(image, diameter=9, sigma_color=75, sigma_space=75)

# Salvar as imagens resultantes
cv2.imwrite('caminho/para/imagem_gaussian_blur.jpg', gaussian_blur_image)
cv2.imwrite('caminho/para/imagem_median_blur.jpg', median_blur_image)
cv2.imwrite('caminho/para/imagem_bilateral_filter.jpg', bilateral_filter_image)