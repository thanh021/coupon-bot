import requests
import os

# Webhook mới của bạn
DISCORD_WEBHOOK = "https://discord.com/api/webhooks/1482319676108308560/wfLvLJaZbWpvCZ0nrrNs-tvOrgVhYOTSSuwDBIbuDPOY6sb-DDpp6WwSW4qln3kChTPk"
API_URL = "https://coupon-manager.deno.dev/api/v1/coupons"


def run_bot():
    print("--- ĐANG KIỂM TRA MÃ MỚI ---")
    try:
        response = requests.get(API_URL)
        json_data = response.json()
        coupons = json_data.get('data', [])

        if not coupons:
            print("Không tìm thấy dữ liệu trên Web.")
            return

        # Lấy mã ở CUỐI danh sách để làm mốc so sánh (mã mới nhất theo ý bạn)
        current_latest_code = coupons[-1].get('couponCode')

        # Đọc mã cũ đã lưu từ file last_code.txt để so sánh
        last_saved_code = ""
        if os.path.exists(CACHE_FILE):
            with open(CACHE_FILE, "r") as f:
                last_saved_code = f.read().strip()

        # So sánh: Nếu mã cuối khác mã đã lưu thì mới gửi toàn bộ danh sách
        if current_latest_code != last_saved_code:
            print(f"Phát hiện mã mới ở cuối: {current_latest_code}. Đang gửi danh sách...")
            
            msg = "🆕 **CẬP NHẬT TẤT CẢ COUPON MỚI:**\n"
            for item in coupons:
                c_code = item.get('couponCode')
                msg += f"🎫 `{c_code}`\n"
            
            # Gửi lên Discord
            requests.post(DISCORD_WEBHOOK, json={"content": msg})

            # Lưu mã cuối này vào file để lần sau không gửi trùng
            with open(CACHE_FILE, "w") as f:
                f.write(current_latest_code)
            
            print(f"✅ Đã cập nhật mã mới lên Discord (Webhook mới).")
        else:
            print("😴 Mã cuối vẫn như cũ, không gửi tin nhắn.")

    except Exception as e:
        print(f"❌ Lỗi: {e}")

if __name__ == "__main__":
    run_bot()
