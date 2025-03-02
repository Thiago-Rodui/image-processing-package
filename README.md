## Image Processing Package

Este pacote fornece várias ferramentas para processamento de imagens, incluindo filtros, transformações e análises.

## Instalação

Use o gerenciador de pacotes pip para instalar o pacote:

```bash
pip install image-processing-package
```

### Como usar

```python
from image_processing.utils.io import load_image, save_image
from image_processing.filters.blur import apply_gaussian_blur
from image_processing.filters.sharpen import apply_sharpen

# Carregar uma imagem
image = load_image('caminho/para/imagem.jpg')

# Aplicar um filtro de desfoque gaussiano
blurred_image = apply_gaussian_blur(image, kernel_size=(5, 5), sigma=1)

# Aplicar um filtro de nitidez
sharpened_image = apply_sharpen(image)

# Salvar a imagem filtrada
save_image(blurred_image, 'caminho/para/imagem_desfocada.jpg')
save_image(sharpened_image, 'caminho/para/imagem_nitida.jpg')