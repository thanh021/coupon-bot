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
            
            # Đọc mã cũ đã lưu trong file (nếu có)
            try:
                with open("last_code.txt", "r") as f:
                    last_code = f.read().strip()
            except FileNotFoundError:
                last_code = ""

            # Chỉ gửi nếu mã mới khác mã cũ
            if code != last_code:
                payload = {
                    "username": "Săn Coupon",
                    "content": f"🔥 **CÓ MÃ COUPON MỚI!**\n➡️ Mã: `{code}`\n🎁 Phần thưởng: {reward}"
                }
                requests.post(DISCORD_WEBHOOK, json=payload)
                
                # Lưu mã mới vào file để lần sau không gửi trùng
                with open("last_code.txt", "w") as f:
                    f.write(code)
                print(f"Đã gửi mã mới: {code}")
            else:
                print("Không có mã mới, không gửi Discord.")
                
    except Exception as e:
        print(f"Lỗi: {e}")

if __name__ == "__main__":
    run_bot()
