curl -Is https://7134d86238462086.247ctf.com/flag | grep -i "Set-Cookie" | cut -d '=' -f2 | cut -d ';' -f1 | base64 -d 2>/dev/null | jq -r '.flag[" b"]' | base64 -d
