# Bot version 1.1
import requests
import os

DISCORD_WEBHOOK = "https://discord.com/api/webhooks/1482319676108308560/wfLvLJaZbWpvCZ0nrrNs-tvOrgVhYOTSSuwDBIbuDPOY6sb-DDpp6WwSW4qln3kChTPk"
API_URL = "https://coupon-manager.deno.dev/api/v1/coupons"
CACHE_FILE = "last_code.txt"
MSG_ID_FILE = "message_id.txt" # File mới để lưu ID tin nhắn

def run_bot():
    try:
        response = requests.get(API_URL)
        coupons = response.json().get('data', [])
        current_list = [c.get('couponCode') for c in coupons if c.get('couponCode')]
        current_list_str = ",".join(current_list)

        last_list_str = ""
        if os.path.exists(CACHE_FILE):
            with open(CACHE_FILE, "r") as f: last_list_str = f.read().strip()

        # Nếu có thay đổi (thêm/bớt mã)
        if current_list_str != last_list_str:
            # 1. Xóa tin nhắn cũ nếu có ID
            if os.path.exists(MSG_ID_FILE):
                with open(MSG_ID_FILE, "r") as f:
                    old_msg_id = f.read().strip()
                if old_msg_id:
                    requests.delete(f"{DISCORD_WEBHOOK}/messages/{old_msg_id}")

            # 2. Chuẩn bị nội dung tin nhắn mới
            if not current_list:
                content = "⚠️ **THÔNG BÁO:** Hiện tại không còn coupon nào khả dụng."
            else:
                content = "🔄 **DANH SÁCH COUPON MỚI NHẤT:**\n" + "\n".join([f"🎫 `{code}`" for code in current_list])

            # 3. Gửi tin nhắn mới (phải thêm ?wait=true để lấy được ID trả về)
            res = requests.post(f"{DISCORD_WEBHOOK}?wait=true", json={"content": content})
            
            if res.status_code == 200:
                new_msg_id = res.json().get('id')
                # Lưu ID mới và danh sách mã mới
                with open(MSG_ID_FILE, "w") as f: f.write(str(new_msg_id))
                with open(CACHE_FILE, "w") as f: f.write(current_list_str)
                print(f"Đã cập nhật tin nhắn mới: {new_msg_id}")

    except Exception as e:
        print(f"Lỗi: {e}")

if __name__ == "__main__":
    run_bot()
