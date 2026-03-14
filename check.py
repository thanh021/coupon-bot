# Bot version 1.1
import requests
import os

# Webhook mới bạn vừa đưa
DISCORD_WEBHOOK = "https://discord.com/api/webhooks/1482319676108308560/wfLvLJaZbWpvCZ0nrrNs-tvOrgVhYOTSSuwDBIbuDPOY6sb-DDpp6WwSW4qln3kChTPk"
API_URL = "https://coupon-manager.deno.dev/api/v1/coupons"
CACHE_FILE = "last_code.txt"

def run_bot():
    print("--- BOT ĐANG SĂN MÃ ---")
    try:
        response = requests.get(API_URL)
        json_data = response.json()
        # Lấy danh sách từ mục "data" theo ảnh bạn chụp
        coupons = json_data.get('data', [])

        if not coupons:
            print("Không tìm thấy dữ liệu trên Web.")
            return

        # Lấy mã ở CUỐI danh sách để làm mốc so sánh
        current_latest_code = coupons[-1].get('couponCode')

        # Đọc mã cũ đã lưu từ file last_code.txt
        last_saved_code = ""
        if os.path.exists(CACHE_FILE):
            with open(CACHE_FILE, "r") as f:
                last_saved_code = f.read().strip()

        # So sánh: Nếu mã cuối khác mã đã lưu mới gửi
        if current_latest_code != last_saved_code:
            print(f"Phát hiện mã mới: {current_latest_code}")
            
            # Tạo nội dung tin nhắn chỉ gồm các mã coupon
            msg = "🆕 **CẬP NHẬT TẤT CẢ COUPON MỚI:**\n"
            for item in coupons:
                c_code = item.get('couponCode')
                msg += f"🎫 `{c_code}`\n"
            
            # Gửi lên Discord
            requests.post(DISCORD_WEBHOOK, json={"content": msg})

            # Lưu lại mã cuối vào file để lần sau không gửi trùng
            with open(CACHE_FILE, "w") as f:
                f.write(current_latest_code)
            
            print("✅ Đã cập nhật mã mới lên Discord.")
        else:
            print("😴 Mã cuối vẫn như cũ, bot sẽ im lặng.")

    except Exception as e:
        print(f"❌ Lỗi: {e}")

if __name__ == "__main__":
    run_bot()
