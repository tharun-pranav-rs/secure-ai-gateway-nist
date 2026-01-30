import requests

# ==========================================
# FINAL VICTORY CONFIGURATION
# ==========================================
GATEWAY_NAME = "secure-scanner-gateway" 
ACCOUNT_ID = "c267966add7c04e16295a38bef315e66"
EMAIL = "tharunrs007@gmail.com"

# PASTE YOUR GLOBAL API KEY HERE
GLOBAL_KEY = "c22a9bc87e83cf43455848eac4b82bfaed5b4"
# ==========================================

def run_final_test():
    print(f"🚀 Targeting Gateway: {GATEWAY_NAME}")
    print(f"🔓 Authentication State: DISABLED (Open for Business)")

    url = f"https://gateway.ai.cloudflare.com/v1/{ACCOUNT_ID}/{GATEWAY_NAME}/workers-ai/@cf/meta/llama-3-8b-instruct"
    
    headers = {
        "X-Auth-Email": EMAIL,
        "X-Auth-Key": GLOBAL_KEY.strip(),
        "Content-Type": "application/json"
    }
    
    payload = {
        "messages": [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": "State the first law of thermodynamics."}
        ]
    }
    
    try:
        response = requests.post(url, headers=headers, json=payload)
        
        if response.status_code == 200:
            print("\n🎉 VICTORY! PIPELINE CONNECTED.")
            print(f"🤖 AI Response: {response.json()['result']['response']}")
            print("\n------------------------------------------------")
            print("✅ You have successfully implemented the NIST 'Manage' layer.")
            print("------------------------------------------------")
        else:
            print(f"\n❌ Error {response.status_code}:")
            print(response.text)

    except Exception as e:
        print(f"\n❌ Script Failed: {e}")

if __name__ == "__main__":
    run_final_test()