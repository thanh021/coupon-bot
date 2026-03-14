import requests
import sys

# Link Webhook của bạn
WEBHOOK = "https://discord.com/api/webhooks/1482305834288681021/qNiGE19jn9lXWe0VsR5ysP5BIKm3EwqKM86e8fLYXYXWn4Ixt2uFRmKEwMZsKkjhYEAC"

print("--- KHỞI CHẠY BOT KIỂM TRA ---")

try:
    # Gửi tin nhắn test
    data = {"content": "🚀 Bot Coupon đã được kích hoạt thành công!"}
    response = requests.post(WEBHOOK, json=data)
    
    if response.status_code == 204:
        print("✅ Thành công: Discord đã nhận được tin nhắn!")
    else:
        print(f"❌ Thất bại: Discord báo lỗi {response.status_code}")
        print(f"Nội dung lỗi: {response.text}")

except Exception as e:
    print(f"💥 Lỗi hệ thống: {e}")

print("--- KẾT THÚC ---")
