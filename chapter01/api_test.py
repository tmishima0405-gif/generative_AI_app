#%%
import tiktoken
#%%
# エンコーディングを取得（安全策としてcl100k_base）
enc = tiktoken.get_encoding("cl100k_base")

text = "こんにちは、今日はいい天気ですね。"

# トークン化
tokens = enc.encode(text)

print("トークン列:", tokens)
print("トークン数:", len(tokens))
# %%

# %%
1+1
# %%
