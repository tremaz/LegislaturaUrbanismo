""" import base64

def encode_image(path):
    with open(path, "rb") as f:
        return base64.b64encode(f.read()).decode("utf-8")

caminho = input("caminho da imagem - ")
pergunta = input("o que quer saber sobre a imagem - ")
b64 = encode_image(caminho)

resp = client.chat.completions.create(
    model="meta-llama/llama-4-scout-17b-16e-instruct",
    messages=[
        {
            "role": "user",
            "content": [
                {"type": "text", "text": pergunta},
                {
                    "type": "image_url",
                    "image_url": {"url": f"data:image/jpeg;base64,{b64}"},
                },
            ],
        }
    ],
)

print(resp.choices[0].message.content) """