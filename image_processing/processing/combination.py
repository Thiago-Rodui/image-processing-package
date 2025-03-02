import cv2
import numpy as np

def blend_images(image1, image2, alpha=0.5):
    """
    Combina duas imagens usando a técnica de blending.

    Args:
        image1: A primeira imagem.
        image2: A segunda imagem.
        alpha: O peso da primeira imagem (entre 0 e 1).

    Returns:
        A imagem resultante da combinação.
    """
    if image1.shape != image2.shape:
        raise ValueError("As imagens devem ter o mesmo tamanho e número de canais")
    
    blended_image = cv2.addWeighted(image1, alpha, image2, 1 - alpha, 0)
    return blended_image

def concatenate_images(image1, image2, axis=0):
    """
    Concatena duas imagens ao longo de um eixo especificado.

    Args:
        image1: A primeira imagem.
        image2: A segunda imagem.
        axis: O eixo ao longo do qual as imagens serão concatenadas (0 para vertical, 1 para horizontal).

    Returns:
        A imagem resultante da concatenação.
    """
    if axis not in [0, 1]:
        raise ValueError("O eixo deve ser 0 (vertical) ou 1 (horizontal)")
    
    concatenated_image = np.concatenate((image1, image2), axis=axis)
    return concatenated_image