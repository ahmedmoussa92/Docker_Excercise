import requests
import os

api_address = 'api'
api_port = 8000

users = [
    ('bob', 'builder', 'v1', 200),
    ('bob', 'builder', 'v2', 403),
    ('alice', 'wonderland', 'v1', 200),
    ('alice', 'wonderland', 'v2', 200)
]

results = []
for user, pwd, version, expected in users:
    r = requests.get(f"http://{api_address}:{api_port}/{version}/sentiment",
                     params={'username': user, 'password': pwd, 'sentence': 'life is good'})
    status = 'SUCCESS' if r.status_code == expected else 'FAILURE'
    results.append((user, version, r.status_code, status))

output = "\n".join([f"{u} ({v}): {s} -> {st}" for u, v, s, st in results])
print("\n=== Authorization Test ===\n" + output)

if os.environ.get('LOG') == '1':
    with open('/logs/api_test.log', 'a') as f:
        f.write(output + "\n")
