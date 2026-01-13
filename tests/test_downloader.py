import py3_downloader


def test_downloader():
    downloader = py3_downloader.downloader.Downloader()

    file_path = downloader.download(
        "https://www.baidu.com/",
        use_cache=True, use_tqdm=False
    )
    print(file_path)

    file_path = downloader.download(
        "https://www.baidu.com/img/PCtm_d9c8750bed0b3c7d089fa7d55720d6cf.png",
        use_cache=False, use_tqdm=True
    )
    print(file_path)


if __name__ == '__main__':
    test_downloader()
