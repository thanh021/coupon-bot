import requests

# Link Webhook của bạn
DISCORD_WEBHOOK = "https://discord.com/api/webhooks/1482305834288681021/qNiGE19jn9lXWe0VsR5ysP5BIKm3EwqKM86e8fLYXYXWn4Ixt2uFRmKEwMZsKkjhYEAC"
API_URL = "https://coupon-manager.deno.dev/api/v1/coupons"

def run_test():
    print("--- ĐANG BẮT ĐẦU KIỂM TRA ---")
    
    # 1. Thử gửi tin nhắn chào hỏi
    payload_test = {"content": "👋 Chào bạn! Bot đã kết nối thành công rồi đây."}
    r_test = requests.post(DISCORD_WEBHOOK, json=payload_test)
    print(f"Kết quả gửi tin nhắn chào: {r_test.status_code}")

    # 2. Thử lấy Coupon
    try:
        response = requests.get(API_URL)
        data = response.json()
        if data:
            code = data[0].get('code')
            payload_coupon = {"content": f"🔥 Mã Coupon hiện tại là: `{code}`"}
            requests.post(DISCORD_WEBHOOK, json=payload_coupon)
            print(f"Đã gửi mã coupon: {code}")
    except Exception as e:
        print(f"Lỗi khi lấy API: {e}")

if __name__ == "__main__":
    run_test()
