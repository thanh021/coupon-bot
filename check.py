import requests

API_URL = "https://coupon-manager.deno.dev/api/v1/coupons"
DISCORD_WEBHOOK = "https://discord.com/api/webhooks/1482305834288681021/qNiGE19jn9lXWe0VsR5ysP5BIKm3EwqKM86e8fLYXYXWn4Ixt2uFRmKEwMZsKkjhYEAC"

def run_bot():
    try:
        response = requests.get(API_URL)
        data = response.json()
        
        if isinstance(data, list) and len(data) > 0:
            latest = data[0]
            code = latest.get('code')
            reward = latest.get('reward', 'Không có mô tả')
            
            # Gửi tin nhắn lên Discord
            payload = {
                "content": f"🔥 **COUPON MỚI:** `{code}`\n🎁 Phần thưởng: {reward}"
            }
            requests.post(DISCORD_WEBHOOK, json=payload)
            print(f"Đã gửi mã: {code}")
    except Exception as e:
        print(f"Lỗi: {e}")

if __name__ == "__main__":
    run_bot()
