import requests
import time

# ==========================================
# CONFIGURATION
# ==========================================
GATEWAY_NAME = "secure-scanner-gateway" 
ACCOUNT_ID = "c267966add7c04e16295a38bef315e66"
EMAIL = "tharunrs007@gmail.com"
GLOBAL_KEY = "c22a9bc87e83cf43455848eac4b82bfaed5b4" # <--- Use your Master Key again
# ==========================================

def launch_attack():
    url = f"https://gateway.ai.cloudflare.com/v1/{ACCOUNT_ID}/{GATEWAY_NAME}/workers-ai/@cf/meta/llama-3-8b-instruct"
    
    headers = {
        "X-Auth-Email": EMAIL,
        "X-Auth-Key": GLOBAL_KEY.strip(),
        "Content-Type": "application/json"
    }
    
    payload = {
        "messages": [{"role": "user", "content": "Spam request!"}]
    }

    print(f"⚔️  LAUNCHING DoS SIMULATION against {GATEWAY_NAME}...")
    print(f"🛑  Limit is set to 3 requests/min. Expecting failure on request #4.")
    print("-" * 40)

    for i in range(1, 10): # We will try to send 9 requests rapidly
        try:
            print(f"🚀 Sending Request #{i}...", end=" ")
            response = requests.post(url, headers=headers, json=payload)
            
            if response.status_code == 200:
                print("✅ Success (200 OK)")
            elif response.status_code == 429:
                print("🛡️ BLOCKED! (429 Too Many Requests)")
                print("\n🎉 SUCCESS! The Rate Limiter is working.")
                print("   Your infrastructure successfully defended itself.")
                break # Stop the loop, we proved the point
            else:
                print(f"❌ Error {response.status_code}")
                
        except Exception as e:
            print(f"❌ Connection Failed: {e}")
        
        # No sleep time! We want to hit it fast.

if __name__ == "__main__":
    launch_attack()