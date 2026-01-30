import requests

# ==========================================
# CONFIGURATION
# ==========================================
GATEWAY_NAME = "secure-scanner-gateway" 
ACCOUNT_ID = "c267966add7c04e16295a38bef315e66"
EMAIL = "tharunrs007@gmail.com"
GLOBAL_KEY = "c22a9bc87e83cf43455848eac4b82bfaed5b4"
# ==========================================

def test_privacy():
    print(f"🕵️  Testing Confidentiality on: {GATEWAY_NAME}")
    
    url = f"https://gateway.ai.cloudflare.com/v1/{ACCOUNT_ID}/{GATEWAY_NAME}/workers-ai/@cf/meta/llama-3-8b-instruct"
    
    headers = {
        "X-Auth-Email": EMAIL,
        "X-Auth-Key": GLOBAL_KEY.strip(),
        "Content-Type": "application/json"
    }
    
    # ⚠️ SIMULATING A USER MISTAKE
    # A user accidentally pastes a sensitive API key into the chat.
    sensitive_payload = {
        "messages": [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": "I forgot what this key is for: sk-live-12345-SECRET-PASSWORD. Can you identify it?"}
        ]
    }
    
    try:
        response = requests.post(url, headers=headers, json=sensitive_payload)
        
        if response.status_code == 200:
            print("\n✅ AI Processed the Request (Service is working).")
            print(f"🤖 AI Response: {response.json()['result']['response']}")
            print("\n------------------------------------------------")
            print("🛑 STOP! Do NOT close this window.")
            print("👉 Go to Cloudflare Dashboard > AI Gateway > Logs.")
            print("👉 Look for this request.")
            print("   - SUCCESS: You see the timestamp and tokens, but 'Messages' says 'Redacted' or is empty.")
            print("   - FAIL: You can see 'sk-live-12345-SECRET-PASSWORD' in the log.")
            print("------------------------------------------------")
        else:
            print(f"❌ Error {response.status_code}: {response.text}")

    except Exception as e:
        print(f"❌ Script Failed: {e}")

if __name__ == "__main__":
    test_privacy()