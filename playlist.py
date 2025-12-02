songs = []

def add_song():
    print("\n--- THÊM BÀI HÁT MỚI ---")
    title = input("Nhập tên bài hát: ").strip()
    artist = input("Nhập tên ca sĩ: ").strip()
    duration_str = input("Nhập thời lượng (giây): ").strip()

    # Chuyển thời lượng sang số nguyên, xử lý trường hợp nhập sai
    try:
        duration = int(duration_str)
    except ValueError:
        print("Thời lượng không hợp lệ, đặt mặc định = 0 giây.")
        duration = 0

    song = {
        "title": title,
        "artist": artist,
        "duration": duration
    }

    songs.append(song)
    print("Đã thêm bài hát vào playlist.")

def view_playlist():
    print("\n--- DANH SÁCH PHÁT ---")

    if not songs:
        print("Playlist hiện đang trống.")
        return

    for index, song in enumerate(songs, start=1):
        print(f"{index}. {song['title']} - {song['artist']} ({song['duration']}s)")

def search_by_artist():
    print("\n--- TÌM BÀI HÁT THEO CA SĨ ---")
    artist_name = input("Nhập tên ca sĩ: ").strip()

    found = False
    for index, song in enumerate(songs, start=1):
        if artist_name.lower() in song['artist'].lower():
            if not found:
                print(f"Các bài hát tìm được với ca sĩ chứa: '{artist_name}':")
            print(f"{index}. {song['title']} - {song['artist']} ({song['duration']}s)")
            found = True

    if not found:
        print("Không tìm thấy bài hát nào của ca sĩ này trong playlist.")

def main():
    while True:
        print("\n--- MUSIC PLAYLIST MANAGER ---")
        print("1. Thêm bài hát")
        print("2. Xem danh sách phát")
        print("3. Tìm bài hát theo ca sĩ")
        print("4. Thoát")

        choice = input("Chọn chức năng: ")

        if choice == '1':
            add_song()
        elif choice == '2':
            view_playlist()
        elif choice == '3':
            search_by_artist()
        elif choice == '4':
            print("Kết thúc chương trình.")
            break
        else:
            print("Lựa chọn không hợp lệ.")
if __name__ == "__main__":
    main()