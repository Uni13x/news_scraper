# Reuters Business News Scraper

スクレイピングツール for [Reuters ビジネスニュース](https://www.reuters.com/business/)。
Selenium＋BeautifulSoup を使って、タイトル・日付・URLを取得し、CSVとして保存します。

---

## 特徴

* 「Load more articles」ボタンを自動クリック（任意回数スクロール）
* タイトル・記事URL・公開日（日本時間）を取得
* CSV形式でローカル保存

---

## 使用技術

* Python 3.12
* Selenium
* BeautifulSoup4
* Pandas
* Chromedriver-autoinstaller
* lxml

---

## インストール方法

git clone https://github.com/your-username/reuters_scraper.git
cd reuters_scraper
pip install -r requirements.txt

---

## 🚀 実行方法

```bash
python main.py
```

実行すると、`reuters_business_articles.csv` がカレントディレクトリに生成されます。

---

## 📄 出力されるCSV内容

| title  | date     | url    |
| ------ | -------- | ------ |
| 記事タイトル | 公開日（JST） | 記事のURL |

---

## 📁 ファイル構成

```
reuters_scraper/
├── main.py                  # 実行スクリプト
├── requirements.txt         # 必要パッケージ
├── reuters_business_articles.csv  # 出力ファイル（任意）
└── README.md
```

---

## 💬 備考

* スクロール回数は `main.py` 内の `max_scrolls` で調整可能
* macOS / Windows / Linux 対応（chromedriverは自動で管理）

---

## 👤 Author

@your-username
