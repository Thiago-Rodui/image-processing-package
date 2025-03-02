import matplotlib.pyplot as plt

def plot_image(image, title='Image', cmap_type='gray'):
    """
    Plota uma imagem usando matplotlib.

    Args:
        image: A imagem a ser plotada.
        title: O título da plotagem.
        cmap_type: O tipo de mapa de cores a ser usado (padrão é 'gray').
    """
    plt.imshow(image, cmap=cmap_type)
    plt.title(title)
    plt.axis('off')  # Desativa os eixos
    plt.show()

def plot_images(images, titles=None, cmap_type='gray'):
    """
    Plota uma lista de imagens usando matplotlib.

    Args:
        images: Lista de imagens a serem plotadas.
        titles: Lista de títulos para cada imagem.
        cmap_type: O tipo de mapa de cores a ser usado (padrão é 'gray').
    """
    n = len(images)
    fig, axes = plt.subplots(1, n, figsize=(15, 5))
    for i in range(n):
        ax = axes[i]
        ax.imshow(images[i], cmap=cmap_type)
        if titles:
            ax.set_title(titles[i])
        ax.axis('off')  # Desativa os eixos
    plt.show()