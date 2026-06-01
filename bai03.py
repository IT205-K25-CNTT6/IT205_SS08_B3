# Chỉ cần duy nhất 1 biến cờ hiệu để đánh dấu xem đã nhập đơn hàng ở Chức năng 1 chưa
is_data_imported = False

while True:
    # Giao diện menu đúng chuẩn hình hộp chữ nhật vuông vức như trong ảnh đề bài
    print("+===================================================+")
    print("|      HỆ THỐNG QUẢN LÝ NỘI DUNG ĐƠN HÀNG GRAB EXPRESS|")
    print("+===================================================+")
    print("|  1. Nhập dữ liệu đơn hàng và xem báo cáo thống kê |")
    print("|  2. Chuẩn hóa mã đơn hàng                         |")
    print("|  3. Ẩn số điện thoại khách hàng                   |")
    print("|  4. Tìm kiếm và thay thế từ khóa trong ghi chú     |")
    print("|  5. Thoát chương trình                             |")
    print("+===================================================+")
    
    choice = input("> Mời bạn chọn chức năng (1-5): ")
    
    match choice:
        case "1":
            # Vào việc trực tiếp, gõ đến đâu kiểm tra bẫy trống dữ liệu đến đó
            sender_name = input("Nhập tên người gửi: ")
            if sender_name.strip() == "":
                print("Tên người gửi không được bỏ trống")
                continue

            sender_phone = input("Nhập số điện thoại người gửi: ")
            if sender_phone.strip() == "":
                print("Số điện thoại người gửi không được bỏ trống")
                continue

            pickup_address = input("Nhập địa chỉ lấy hàng: ")
            if pickup_address.strip() == "":
                print("Địa chỉ lấy hàng không được bỏ trống")
                continue

            receiver_name = input("Nhập tên người nhận: ")
            if receiver_name.strip() == "":
                print("Tên người nhận không được bỏ trống")
                continue

            receiver_phone = input("Nhập số điện thoại người nhận: ")
            if receiver_phone.strip() == "":
                print("Số điện thoại người nhận không được bỏ trống")
                continue

            delivery_address = input("Nhập địa chỉ giao hàng: ")
            if delivery_address.strip() == "":
                print("Địa chỉ giao hàng không được bỏ trống")
                continue

            delivery_note = input("Nhập ghi chú giao hàng: ")
            if delivery_note.strip() == "":
                print("Ghi chú giao hàng không được bỏ trống")
                continue

            # Khi người dùng vượt qua hết các bước nhập liệu trên -> Bật cờ hiệu thành công
            is_data_imported = True

            print("\n--- BÁO CÁO THỐNG KÊ ĐƠN HÀNG ---")
            print(f"Tên người gửi sau khi chuẩn hóa: {sender_name.strip().title()}")
            print(f"Tên người nhận sau khi chuẩn hóa: {receiver_name.strip().title()}")
            
            # Mẹo nhỏ băm chuỗi xóa sạch khoảng trắng thừa ở giữa địa chỉ
            pickup_clean = " ".join(pickup_address.split())
            delivery_clean = " ".join(delivery_address.split())
            print(f"Địa chỉ lấy hàng sau khi chuẩn hóa: {pickup_clean}")
            print(f"Địa chỉ giao hàng sau khi chuẩn hóa: {delivery_clean}")
            
            print(f"Ghi chú giao hàng sau khi loại bỏ khoảng trắng: {delivery_note.strip()}")
            print(f"Độ dài ghi chú giao hàng: {len(delivery_note)}")
            
            # Đếm số lượng từ chính xác bằng .split()
            word_count = len(delivery_note.split())
            print(f"Số lượng từ trong ghi chú giao hàng: {word_count}")
            print(f"Ghi chú giao hàng dạng chữ thường: {delivery_note.lower()}")
            print(f"Ghi chú giao hàng dạng chữ hoa: {delivery_note.upper()}\n")

        case "2":
            # Chức năng này độc lập, đề không bắt phải nhập chức năng 1 trước nên cho chạy luôn
            order_code = input("Nhập mã đơn hàng cần chuẩn hóa: ")
            if order_code.strip() == "":
                print("Mã đơn hàng không được bỏ trống")
                continue
                
            print(f"Mã đơn hàng ban đầu: {order_code}")
            
            # Viết hoa toàn bộ và xử lý khoảng trắng thừa
            code_clean = order_code.strip().upper()
            code_dash = "-".join(code_clean.split())
            
            # Tự động thêm tiền tố GRAB- nếu người dùng quên nhập
            if not code_dash.startswith("GRAB-"):
                code_final = "GRAB-" + code_dash
            else:
                code_final = code_dash
                
            print(f"Mã đơn hàng sau khi được chuẩn hóa: \"{code_final}\"")

        case "3":
            # Bẫy dữ liệu: Nếu chưa nhập thông tin ở chức năng 1, cờ hiệu đang là False -> Chặn lại luôn
            if not is_data_imported:
                print("Cảnh báo: Vui lòng chạy Chức năng 1 để nhập thông tin đơn hàng trước!")
                continue
            
            valid_phones = True
            
            # Kiểm tra bẫy số điện thoại người gửi (chỉ được chứa số và phải đúng 10 số)
            if not sender_phone.isdigit():
                print("Số điện thoại không hợp lệ")
                valid_phones = False
            elif len(sender_phone) != 10:
                print("Số điện thoại không hợp lệ: Số điện thoại phải có đúng 10 ký tự")
                valid_phones = False
                
            # Kiểm tra tiếp số điện thoại người nhận
            if valid_phones:
                if not receiver_phone.isdigit():
                    print("Số điện thoại không hợp lệ")
                    valid_phones = False
                elif len(receiver_phone) != 10:
                    print("Số điện thoại không hợp lệ: Số điện thoại phải có đúng 10 ký tự")
                    valid_phones = False

            # Nếu cả 2 số điện thoại đều sạch lỗi, tiến hành cắt chuỗi ẩn thông tin ở giữa
            if valid_phones:
                hidden_sender = sender_phone[0:3] + "*****" + sender_phone[8:10]
                hidden_receiver = receiver_phone[0:3] + "*****" + receiver_phone[8:10]
                print(f"SĐT người gửi: {hidden_sender}")
                print(f"SĐT người nhận: {hidden_receiver}")

        case "4":
            # Bẫy số 4 của đề bài: Chọn chức năng 4 khi chưa nhập ghi chú ở chức năng 1
            if not is_data_imported:
                print("Chưa có ghi chú giao hàng để tìm kiếm")
                continue
                
            find_word = input("Nhập từ khóa cần tìm: ")
            replace_word = input("Nhập từ khóa thay thế: ")
            
            # Đếm số lần trùng từ khóa trực tiếp trên biến delivery_note
            count_word = delivery_note.count(find_word)
            
            if count_word > 0:
                delivery_note = delivery_note.replace(find_word, replace_word)
                print(f"Số lần xuất hiện của từ khóa: {count_word}")
                print(f"Ghi chú đơn hàng sau khi thay thế: {delivery_note}")
            else:
                print("Không tìm thấy từ khóa cần tìm trong ghi chú đơn hàng")

        case "5":
            print("Thoát chương trình")
            break

        case _:
            # Giải quyết gọn Bẫy số 5 (Lựa chọn ngoài 1-5) và Bẫy số 6 (Nhập chữ 'abc', '@', '2.5')
            print("Lựa chọn không hợp lệ!")


# 1. PHÂN TÍCH ĐẦU VÀO VÀ ĐẦU RA (INPUT / OUTPUT)
#    - Để mấy chức năng 3 và 4 không bị lỗi sập app (NameError) khi mới mở chương trình lên,
#      tụi mình sẽ tạo sẵn 7 cái hộp rỗng đặt ở ngoài vòng lặp để chứa dữ liệu xài chung cho đơn hàng.
#    - Giao diện Menu:
#      + Đầu vào: Người dùng gõ một phím chọn từ bàn phím (biến choice).
#      + Đầu ra: Hiện ra cái bảng menu hình hộp chữ nhật vuông vức sạch sẽ của hệ thống Grab.
#    - Chọn số 1 (Nhập đơn hàng và xem thống kê):
#      + Đầu vào: Nhập liên tiếp 7 thông tin gồm tên, SĐT, địa chỉ của cả người gửi/nhận và ghi chú đơn hàng.
#      + Đầu ra: Hiện ra ngay 9 dòng kết quả sau khi đã lọc sạch khoảng trắng với định dạng hoa đầu từ.
#    - Chọn số 2 (Chuẩn hóa mã đơn hàng):
#      + Đầu vào: Người dùng gõ vào một mã đơn bất kỳ (order_code).
#      + Đầu ra: Hiện ra mã đơn ban đầu kèm mã mới viết hoa hoàn toàn, biến dấu cách thành '-' và bù chữ 'GRAB-'.
#    - Chọn số 3 (Ẩn số điện thoại khách hàng):
#      + Đầu vào: Lấy dữ liệu 2 số điện thoại đã lưu từ chức năng 1.
#      + Đầu ra: Hiện chữ báo lỗi nếu dính ký tự chữ hoặc độ dài không bằng 10; nếu hợp lệ thì in ra dạng 098*****21.
#    - Chọn số 4 (Tìm và đổi từ trong ghi chú giao hàng):
#      + Đầu vào: Gõ từ muốn tìm (find_word) và từ mới muốn thế chỗ (replace_word).
#      + Đầu ra: Cập nhật lại chuỗi ghi chú mới và đếm xem từ đó có mặt mấy lần.
#    - Chọn số 5 (Thoát chương trình):
#      + Đầu ra: Hiện chữ "Thoát chương trình" và tắt app luôn.
#
# 2. ĐỀ XUẤT CÁCH LÀM (MẸO DÙNG CÁC LỆNH CHUỖI TRONG PYTHON)
#    - Bẫy menu nhập bậy (Bẫy 5 & 6): Tụi mình giữ nguyên biến choice là chuỗi `str`, không ép sang int().
#      Xong rồi xài match-case. Ai gõ chữ 'abc', số phẩy '2.5' hay phím lạ thì tự động rơi vào cái ngách mặc định `case _` để bắt nhập lại.
#    - Bắt lỗi bỏ trống (Bẫy 1): Dùng lệnh `.strip() == ""`. Nếu người dùng nhấn Enter hay cố tình gõ toàn phím Space trắng, 
#      mình phát hiện ra ngay để chặn lại và báo thông báo lỗi cụ thể cho từng trường dữ liệu.
#    - Chuẩn hóa địa chỉ ở chức năng 1 và mã đơn ở chức năng 2: Mình xài mẹo nhỏ là dùng `.split()` để băm chuỗi thành danh sách các từ,
#      xong dùng `" ".join()` hoặc `"-".join()` để dính tụi nó lại. Cách này vừa nhanh vừa giải quyết triệt để bẫy nhiều khoảng trắng ở giữa.
#    - Check lỗi số điện thoại ở chức năng 3: Dùng phương thức `.isdigit()` để kiểm tra xem chuỗi có thuần số hay không (bắt bẫy 2).
#      Dùng lệnh `len() != 10` để kiểm tra độ dài đúng 10 ký tự (bắt bẫy 3). Để ẩn số, tụi mình dùng kỹ thuật cắt chuỗi (string slicing)
#      lấy 3 số đầu `[0:3]`, cộng chuỗi `"*****"`, rồi cộng tiếp 2 số cuối `[8:10]`.
#
# 3. LUỒNG ĐI CỦA CHƯƠNG TRÌNH (TỪ TRÊN XUỐNG DƯỚI)
#    BƯỚC 1: Đặt sẵn 7 biến chuỗi rỗng ngoài vòng lặp.
#    BƯỚC 2: Chạy một vòng lặp mãi mãi (while True):
#        In cái bảng Menu hình hộp chữ nhật bắt mắt.
#        Nhập lựa chọn choice từ bàn phím (kiểu chữ).
#        So khớp choice bằng lệnh MATCH-CASE:
#            NẾU choice LÀ "1":
#                Cho nhập 7 thông tin đơn hàng. Nếu có bất kỳ ô nào bị trống -> Báo lỗi [Trường dữ liệu] không được bỏ trống.
#                In ra 9 dòng kết quả thống kê dữ liệu trực tiếp bằng các lệnh .strip(), .title(), .lower(), .upper().
#            NẾU choice LÀ "2":
#                Cho nhập mã đơn hàng. Tiến hành cắt chuỗi, viết hoa, biến dấu cách thành '-' và bù chữ 'GRAB-' vào đầu nếu thiếu.
#            NẾU choice LÀ "3":
#                Nếu thông tin SĐT ở chức năng 1 đang trống -> Báo lỗi bắt chạy chức năng 1 trước.
#                Tiến hành kiểm tra xem SĐT có chứa chữ không, có đúng 10 số không. Nếu chuẩn bài thì cắt ghép chuỗi hiển thị dạng bảo mật.
#            NẾU choice LÀ "4":
#                Nếu chuỗi ghi chú đang trống -> Kích hoạt Bẫy 4 báo lỗi: "Chưa có ghi chú giao hàng để tìm kiếm".
#                Cho gõ từ cần tìm và từ thay thế. Đếm tần suất xuất hiện bằng `.count()`. Nếu có thì thế chỗ bằng `.replace()` và in ra.
#            NẾU choice LÀ "5":
#                In chữ "Thoát chương trình" và dùng lệnh break để dừng hẳn vòng lặp kết thúc.
#            TRƯỜNG HỢP CÒN LẠI (case _):
#                In "Lựa chọn không hợp lệ!" rồi tự động đẩy vòng lặp quay lại giao diện Menu ban đầu.