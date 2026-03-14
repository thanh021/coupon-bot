import requests

DISCORD_WEBHOOK = "https://discord.com/api/webhooks/1482305834288681021/qNiGE19jn9lXWe0VsR5ysP5BIKm3EwqKM86e8fLYXYXWn4Ixt2uFRmKEwMZsKkjhYEAC"
API_URL = "https://coupon-manager.deno.dev/api/v1/coupons"

def run_bot():
    print("--- ĐANG QUÉT MÃ COUPON ---")
    try:
        response = requests.get(API_URL)
        json_data = response.json()
        
        # Theo ảnh bạn gửi, mã nằm trong json_data['data']
        coupons = json_data.get('data', [])

        if coupons:
            # Lấy 3 mã mới nhất để gửi một lần cho gọn
            top_coupons = coupons[:3] 
            msg = "🔔 **DANH SÁCH COUPON MỚI NHẤT:**\n"
            
            for item in top_coupons:
                c_code = item.get('couponCode')
                c_note = item.get('statusInfo', 'Hoạt động')
                msg += f"🎫 Mã: `{c_code}` ({c_note})\n"
            
            # Gửi lên Discord
            requests.post(DISCORD_WEBHOOK, json={"content": msg})
            print("✅ Đã gửi danh sách mã lên Discord!")
        else:
            print("Không tìm thấy mục data hoặc danh sách trống.")
            
    except Exception as e:
        print(f"Lỗi: {e}")

if __name__ == "__main__":
    run_bot()
