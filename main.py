import os
from dotenv import load_dotenv
from groq import Groq
from pathlib import Path

load_dotenv()
client = Groq(api_key=os.environ["GROQ_API_KEY"])

leis = Path("Leis.txt").read_text(encoding="utf-8")
prompt_base = Path("PromptBase.txt").read_text(encoding="utf-8")
problema = Path("AnaliseDaImagem.txt").read_text(encoding="utf-8")

resp1 = client.chat.completions.create(
    model="openai/gpt-oss-120b",
    messages=[{"role": "user", "content": f"{prompt_base} FONTES: {leis}. O problema que você deve explicar é {problema}"}]
              )

with open("Resposta.txt", "w", encoding="utf-8") as f:
    f.write(resp1.choices[0].message.content)