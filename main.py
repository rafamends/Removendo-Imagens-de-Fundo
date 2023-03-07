from rembg import remove
from PIL import Image

input_imagem = "cachorro.jpg"
out_imagem = "cachorro_rmbg.png"

input = Image.open(input_imagem)
out = remove(input)

out.save(out_imagem)