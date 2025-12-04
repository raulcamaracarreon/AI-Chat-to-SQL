import os
from typing import Optional
from openai import OpenAI

class NLtoSQL:
    """
    Traductor NL→SQL. Por defecto usa OpenAI (modelo pequeño/rápido).
    Puedes cambiar a tu preferencia: 'openai:gpt-4o-mini', 'openai:gpt-4.1-mini', etc.
    También puedes adaptar a un endpoint local (Llama, etc.).
    """
    def __init__(self, system_prompt: str, model_choice: str = "openai:gpt-4o-mini"):
        self.system_prompt = system_prompt
        self.model_choice = model_choice

        if self.model_choice.startswith("openai:"):
            self.provider = "openai"
            self.model = self.model_choice.split(":", 1)[1]
            self.client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))
        else:
            raise ValueError("Solo 'openai:*' implementado en este starter.")

    def nl_to_sql(self, user_query: str) -> str:
        if self.provider == "openai":
            rsp = self.client.chat.completions.create(
                model=self.model,
                temperature=0,
                messages=[
                    {"role": "system", "content": self.system_prompt},
                    {"role": "user", "content": user_query},
                ]
            )
            sql = rsp.choices[0].message.content.strip()
            # Asegura que sea una sola línea SQL sin backticks
            sql = sql.replace("```sql", "").replace("```", "").strip()
            return sql

        raise RuntimeError("Proveedor no soportado.")
