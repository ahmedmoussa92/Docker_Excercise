# test_auth.py
import os
import requests

api_address = 'api'  # will be the name of the API container in docker-compose
api_port = 8000

users = [
    ("alice", "wonderland", 200),
    ("bob", "builder", 200),
    ("clementine", "mandarine", 403)
]

output = "============================\n    Authentication test\n============================\n"

for username, password, expected_code in users:
    r = requests.get(
        url=f"http://{api_address}:{api_port}/permissions",
        params={"username": username, "password": password}
    )
    status_code = r.status_code
    test_status = "SUCCESS" if status_code == expected_code else "FAILURE"

    result = f"""
request done at "/permissions"
| username="{username}"
| password="{password}"
expected result = {expected_code}
actual result = {status_code}
==> {test_status}
"""
    print(result)
    output += result

# Save logs if LOG=1
if os.environ.get("LOG") == "1":
    with open("api_test.log", "a") as file:
        file.write(output)
