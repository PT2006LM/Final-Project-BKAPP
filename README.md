# Final-Project-BKAPP


## Làm việc qua github

Để lấy code về local, soạn theo cú pháp  
> git clone https://github.com/PT2006LM/Final-Project-BKAPP.git

Để lưu các thay đổi tại local sau khi làm việc  
1. Dùng cú pháp `git add .` để git track các thay đổi. Trong đó, dấu `.` ý track thay đổi ở tất cả các file, không thì có thể thay `.` bằng đường dẫn tới file. 
2. Dùng cú pháp `git commit -m <message>` để lưu (commit) các thay đổi ở bước trên. Lưu ý để lại `message` về nội dung commit (sau đẩy lên có thể coi ở phần commit ở repos)

Để đưa phần code đã được thay đổi (và committed) về github.
1. Tạo đường dẫn remote cho git với `git remote add origin <url>`. Cú pháp này sẽ tạo 1 branch remote (mặc định ở local tên là master) tên là `origin`. Chú ý về đường dẫn:  
    *  Đường dẫn này khác với url clone ban đầu. Cụ thể sẽ chứa thông tin để xác nhận tài khoản github (chứ k liên quan gì tới git).
    *  Cú pháp đường dẫn nếu dùng HTTPS (repos này chưa thiết lập SSL): `https://<tên-đăng-nhập-github>:<mật-khẩu-github>@github.com/<tên-repos>`, ở đây `tên-repos` = `PT2006LM/Final-Project-BKAPP.git`
    *  Cú pháp để đổi đường dẫn remote: `git remote set-url origin <url-mới>`
    *  Cú pháp để kiểm tra tất các remote url ở tất cả các branch ở local: `git remote -v`
    
2. Đẩy code lên với cú pháp `git push origin master`. Trong đó `origin` là tên nhánh đích để đẩy vào, còn `master` là tên nhánh chứa code, commit cần đẩy

Trong quá trình làm việc, trường hợp đồng đội có sửa code và đã commit lên, có thể lấy code từ github về mà không phải thiết lập lại từ đầu (`git clone`, `git remote add...`) với cú pháp
> git pull origin master

Bên cạnh việc lưu các thay đổi (thêm sửa xóa), có thể cài đặt để git 'bơ' một số thư mục, tức là các thư mục này sẽ không được tracked và do đó không thể `add` `commit` hay `push` các file này. Điều này giúp tránh đẩy các file không cần thiết (như môi trường ảo, thường thông tin về các dependencies sẽ được gói lại trong 1 số file đặc biệt để local cài lại như `requirements.txt`, `Pipfile` hay `packages.json`; hay như các file config để bảo mật)  
Để làm được điều này cần tạo 1 file `.gitignore` ở root directory, trong file này mỗi hàng để tên 1 file ta muốn git bỏ qua. Trên Visual studio code, các file được ghi trong `.gitignore` sẽ bị mở đi, thể hiện là không bị đẩy lên remote.


**Lưu ý**: Mỗi khi làm việc nhớ kiểm tra commit để cân nhắc có nên pull trước khi làm việc không.
  
  
  
## Về setup và chạy project trong quá trình làm việc

*Repository này sử dụng môi trường ảo python, nhằm mục đích đồng bộ về phiên bản các thư viện, dependencies trong quá trình làm việc*

Một số lưu ý về môi trường ảo trong python (tập trung vào `env`, bên cạnh loại môi trường ảo này có `pipenv` cũng được sử dụng rộng rãi)

  * Để tạo môi trường ảo trong 1 thư mục, mở terminal/prompt trỏ vào thư mục đó rồi dùng `python -m venv env`. Trường hợp dùng Powershell trên VisualCode thì chỉnh sửa cài đặt chút theo [hương dẫn trên stackoverflow](https://stackoverflow.com/questions/56199111/visual-studio-code-cmd-error-cannot-be-loaded-because-running-scripts-is-disabl) để kích hoạt môi trường.  

  * Để kích hoạt môi trường, chạy file `active` theo đường dẫn, `.env/Scripts/active`. Trên windows, paste đường dẫn file `active` sẽ kích hoạt môi trường ảo tại thư mục tương ứng. Khi môi trường được kích hoạt thành công, `(env)` sẽ hiện lên phía trước lệnh trên terminal/prompt.  

  * Sau khi môi trường ảo được kích hoạt, các thư viện được cài trong folder đó được cô lập với hệ thống. Tức là nếu hệ thống cài thư viện A mà môi trường ảo chưa cài thì không thể import được, ngược lại nếu môi trường cài thư viện B mà hệ thống không cài thì vẫn import được thư viện B. Ngoài ra nếu cùng 1 thư viện A, hệ thống dùng bản a mà môi trường dùng bản b thì tại môi trường ta sẽ làm việc với b, tránh được trường hợp mâu thuẫn về phiên bản của dependencies.

  * Trong khi môi trường ảo hoạt động, các lệnh pip như `pip install <tên-thư-viên>`, `pip uninstall <tên-thư-viên>`, `pip freeze` sẽ tác dụng lên môi trường ảo thay vì hệ thống như mọi khi.

Một số lưu ý khi làm việc sử dụng môi trường ảo qua `env`:

  * Trong thư mục làm việc, đảm bảo có thư mục `env` tạo bởi `python -m venv env`.
  
  * Tải các thư viện cần thiết nếu thiếu, các thư viện kèm theo phiên bản tương ứng sẽ được ghi trong file `requriements.txt`. Để cài nhanh các thư viện từ file này dùng:
  > pip install -r requirements.txt
  File này có thể được tạo ra qua việc dùng `pip freeze > requirements.txt`.
  
  * Nếu sử dụng git, nhớ đưa `env` vào `.gitignore`, và chuẩn bị 1 file `requirements.txt` để cài lại thư viện trên local.
  
  
*Project này sử dụng framework django làm ứng dụng web*

Để chạy server, sau khi cài các thư mục cần thiết qua môi trường ảo. Trên terminal/prompt, trở vào thư mục chứa file `manage.py` và chạy `python manage.py runserver`.
Web app được chạy trên [localhost:8000](http://localhost:8000/) 
