import requests
import os

DISCORD_WEBHOOK = "https://discord.com/api/webhooks/1482305834288681021/qNiGE19jn9lXWe0VsR5ysP5BIKm3EwqKM86e8fLYXYXWn4Ixt2uFRmKEwMZsKkjhYEAC"
API_URL = "https://coupon-manager.deno.dev/api/v1/coupons"
CACHE_FILE = "last_code.txt"

def run_bot():
    try:
        response = requests.get(API_URL)
        json_data = response.json()
        coupons = json_data.get('data', [])

        if not coupons:
            return

        # Lấy mã ở CUỐI danh sách để làm mốc so sánh
        current_latest_code = coupons[-1].get('couponCode')

        last_saved_code = ""
        if os.path.exists(CACHE_FILE):
            with open(CACHE_FILE, "r") as f:
                last_saved_code = f.read().strip()

        if current_latest_code != last_saved_code:
            msg = "🆕 **CẬP NHẬT TẤT CẢ COUPON MỚI:**\n"
            for item in coupons:
                msg += f"🎫 `{item.get('couponCode')}`\n"
            
            requests.post(DISCORD_WEBHOOK, json={"content": msg})

            with open(CACHE_FILE, "w") as f:
                f.write(current_latest_code)
            print(f"Đã gửi và lưu mã cuối: {current_latest_code}")
        else:
            print("Không có mã mới ở cuối danh sách.")

    except Exception as e:
        print(f"Lỗi: {e}")

if __name__ == "__main__":
    run_bot()
