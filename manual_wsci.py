from pathlib import Path

# ========= MOCK模拟ollama.chat =========
class MockMessage:
    def __init__(self, content):
        self.message = type("obj",(),{"content":content})

def chat(model, messages):
    mock_json = '''
{
  "root_cause":"Windows cached old university password for eduroam Wi‑Fi",
  "troubleshooting_steps":["Open Windows Settings > Network & Internet > Wi‑Fi","Forget existing eduroam profile","Re‑connect eduroam with new password","Verify account is active"],
  "note":"eduroam service operational, issue local device credential cache"
}
'''
    return MockMessage(mock_json)
# ========================================================


question = """
I changed my university password this morning.
Now my Windows laptop won't connect to campus Wi‑Fi,
but my phone still works.
"""

knowledge_dir = Path("knowledge")
# 手动硬编码相关文件列表，不自动检测关键词
selected_files = [
    knowledge_dir / "wifi_setup.txt",
    knowledge_dir / "password_changes.txt",
    knowledge_dir / "service_status.txt"
]

context = ""
for f in selected_files:
    context += f.read_text(encoding="utf-8")
    context += "\n\n"

print(f"Context characters: {len(context)}")

prompt = f"""
Use the knowledge context to answer student IT‑support question.

Context:
{context}

Student question:
{question}

Return structured JSON with keys root_cause, troubleshooting_steps(list), note.
Only output JSON.
"""

response = chat(model="qwen", messages=[{"role":"user", "content": prompt}])
print(response.message.content)
