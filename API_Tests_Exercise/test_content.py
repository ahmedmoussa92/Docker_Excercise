import requests
import os

api_address = 'api'
api_port = 8000

sentences = [
    ("life is beautiful", +1),
    ("that sucks", -1)
]

results = []
for version in ['v1', 'v2']:
    for sentence, expected in sentences:
        r = requests.get(f"http://{api_address}:{api_port}/{version}/sentiment",
                         params={'username': 'alice', 'password': 'wonderland', 'sentence': sentence})
        score = r.json().get('score')
        status = 'SUCCESS' if (score > 0 and expected > 0) or (score < 0 and expected < 0) else 'FAILURE'
        results.append((version, sentence, score, status))

output = "\n".join([f"{v} | {s} -> {sc} ({st})" for v, s, sc, st in results])
print("\n=== Content Test ===\n" + output)

if os.environ.get('LOG') == '1':
    with open('/logs/api_test.log', 'a') as f:
        f.write(output + "\n")
