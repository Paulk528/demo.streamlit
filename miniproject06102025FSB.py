import re
import streamlit as st

# Tiêu đề trang
st.title("🎯 ĐĂNG KÝ TÀI KHOẢN")

# Ô nhập liệu
email = st.text_input(" 📧 Email của bạn:")
password = st.text_input("🔑 Mật khẩu:", type="password")

# Hàm kiểm tra email hợp lệ (theo định dạng Gmail)
def is_valid_email(email):
    pattern = r"^[a-zA-Z0-9._%+-]+@gmail\.com$"
    return re.match(pattern, email)

# Hàm kiểm tra độ mạnh của mật khẩu
def is_valid_password(password):
    if len(password) < 8:
        return False
    if not re.search(r"[A-Z]", password):  # có chữ hoa
        return False
    if not re.search(r"[a-z]", password):  # có chữ thường
        return False
    if not re.search(r"[0-9]", password):  # có số
        return False
    if not re.search(r"[@$!%*?&]", password):  # có ký tự đặc biệt
        return False
    return True

# Khi nhấn nút "Tạo tài khoản"
if st.button("Tạo tài khoản"):
    if not is_valid_email(email):
        st.error("❌ Email của bạn không hợp lệ. Vui lòng kiểm tra định dạng (ví dụ: ten.ban@gmail.com).")
    elif not is_valid_password(password):
        st.warning("⚠️ Mật khẩu không đáp ứng yêu cầu: tối thiểu 8 ký tự, có chữ hoa, thường, số và ký tự đặc biệt (một trong những ký tự sau: @$!%*?&).")
    else:
        st.success("✅ Tạo tài khoản thành công!")
        st.balloons()
