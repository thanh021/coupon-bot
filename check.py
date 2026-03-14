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
            
            # GỬI TEST NGAY LẬP TỨC
            payload = {
                "username": "Captain Hook",
                "content": f"✅ **BOT ĐANG HOẠT ĐỘNG!**\n🔥 Mã hiện tại trên web là: `{code}`\n🎁 Phần thưởng: {reward}"
            }
            r = requests.post(DISCORD_WEBHOOK, json=payload)
            print(f"Đã gửi lệnh tới Discord, mã phản hồi: {r.status_code}")
        else:
            print("API hiện đang trống.")
    except Exception as e:
        print(f"Lỗi: {e}")

if __name__ == "__main__":
    run_bot()
