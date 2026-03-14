import requests

DISCORD_WEBHOOK = "https://discord.com/api/webhooks/1482305834288681021/qNiGE19jn9lXWe0VsR5ysP5BIKm3EwqKM86e8fLYXYXWn4Ixt2uFRmKEwMZsKkjhYEAC"
API_URL = "https://coupon-manager.deno.dev/api/v1/coupons"

def run_bot():
    print("--- ĐANG KẾT NỐI ĐẾN TRANG COUPON ---")
    try:
        response = requests.get(API_URL)
        data = response.json()
        
        # In dữ liệu thô ra Log để bạn kiểm tra
        print(f"Dữ liệu nhận được từ web: {data}")

        if isinstance(data, list) and len(data) > 0:
            # Lấy cái coupon đầu tiên trong danh sách
            latest = data[0]
            code = latest.get('code')
            reward = latest.get('reward', 'Không có mô tả')
            
            print(f"Tìm thấy mã: {code} - Phần thưởng: {reward}")

            # Gửi lên Discord
            payload = {
                "username": "Máy Dò Coupon",
                "content": f"🔎 **KIỂM TRA DỮ LIỆU WEB:**\n✅ Bot thấy mã này trên trang chủ: `{code}`\n🎁 Phần thưởng: {reward}"
            }
            requests.post(DISCORD_WEBHOOK, json=payload)
        else:
            print("Trang web hiện tại không có mã nào (Danh sách trống).")
            requests.post(DISCORD_WEBHOOK, json={"content": "⚠️ Đã kết nối web thành công nhưng hiện tại không có mã coupon nào trên đó."})

    except Exception as e:
        print(f"Lỗi: {e}")

if __name__ == "__main__":
    run_bot()
