# 越後湯澤跨年滑雪 — 交接文件

> 給下一個接手的 AI。讀完這份就能繼續做，不用重看之前的對話。
> 最後更新：2026-10-21（神立攻略完成）

## 1. 專案是什麼

- 使用者：**Jerry（陳冠文）**，用**繁體中文**溝通。
- 7 人跨年滑雪行程：**越後湯澤 12/30–1/5（2026–2027）**。
- 網站：**https://jerry-6969.github.io/ski-trip/** （GitHub Pages）
- Repo：**Jerry-6969/ski-trip**，整個網站只有一個檔案 `index.html`（HTML＋CSS＋JS 全部寫在裡面，約 4,400 行）。
- 改完直接 commit＋push 到預設分支，GitHub Pages 約 1–2 分鐘生效。

## 2. 使用者偏好（很重要）

- **沒確認的資訊不要寫上去**。估的、猜的金額或時間一律空白或標「待確認」。
- **大改動先討論再做**；小修正、他明確說「直接做」的就直接做。
- 預算表以**一個人**為單位（用 Jerry 的行程算，Phoebe 相同）。
- 字要大、手機要好讀；行程總表要維持「週曆格子」格式。
- 不能幫他登入、輸入個資或付款：訂票只開到付款前一頁給他看。
- 回覆用繁體中文、口語、精簡，用表格整理比較。

## 3. 成員

| 組 | 成員 | 備註 |
|---|---|---|
| A | Jerry、Phoebe（王淳筣） | 小 Su 教練 |
| B | Sandy（卜郡廷）、Vivi（張家薇） | 阿仙教練；1/3 晚去東京、1/4 回台 |
| C | 文凱（Vivi 老公） | 不上課、自己滑；12/30–1/3 跟 B 組加床；1/3 晚跟 B 組去東京後自己旅行，1/5 MM627 成田回台 |
| D | Jing（陳冠憬）、Lisa | Jing 跟 Michael 教練；**Lisa 不滑雪**；12/30–1/3 住天際溫泉，1/3 起住 HATAGO |

## 4. 目前確定的行程（雪場）

| 日期 | 雪場 | 誰 | 說明 |
|---|---|---|---|
| 12/30 | 抵達 | 全員 | Jing・Lisa 已在 Klook 預購 **Toki 331 上野 16:46→越後湯澤 17:56**（11/30 確認）；其他人新幹線**還沒買** |
| 12/31 | **神樂（三俁口）** | Jerry、Phoebe、文凱 | 小 Su 10:00–15:00 上課；田代組（Jing、Sandy、Vivi）在神樂田代 09:00–15:00 |
| 1/1 | **神樂（三俁口）**＋晚上**神立夜滑** | Jerry、Phoebe、文凱 | 小 Su 12:00–16:00；建議 11:00–11:15 出發（待跟小 Su 確認）；神立 18:00–22:00 |
| 1/2 | **石打丸山** | 6 人（Lisa 不滑） | 全員自由滑；17:00–18:00 還雪具 |
| 1/3 | 一日遊（地點未定） | 全員 | Sandy・Vivi・文凱晚上去東京 |
| 1/4 | 雪場未定 | Jerry、Jing | |
| 1/5 | 回程 | | Jerry・Phoebe BR195 成田 T1 20:20；Jing・Lisa JX805 成田 T2 20:10 |

## 5. 雪票（已決定的買法）

- **12/31、1/1 神樂**：WAmazing 22 雪場共通券，NT$1,482／張，Jerry、Phoebe、文凱**每人 2 張**，**12/10 前買**（限量、不能取消）。到三俁站窗口出示「我的頁面」換 Mt.Naeba 1 日券。
- **1/1 神立夜滑**：現場買。4 小時夜滑票 25/26 約 ¥3,000–3,800（SURF&SNOW 與新潟觀光協會數字不同），26/27 官網還沒公布。26/27 官網確認 12/30–1/2 連四晚有夜滑（18:00–翌 2:00）。**夜滑接駁 19:10 才有第一班**（越後湯澤站東口），所以 18:00 開始要小 Su 載或計程車。
- **1/2 石打**：Alpen Group 早割電子票 ¥5,800＋2%＝¥5,916，**12/14 前每人各自下單**；email 寄送、沒有 QR Code，到中央入口窗口換票（換票方式待問）。

## 6. 雪具（青達雪具）

- 已預約 5 人（Jerry、Phoebe、Sandy、Vivi、Jing）。**文凱還沒預約**（要租 12/31–1/2）。Jing 預約 1/2 歸還，要延長到 1/4。
- 青達回覆：可以在雪場**面交歸還**（GALA、湯澤高原、石打丸山「石口」、神立、湯澤中里、湯澤 PARK、NASPA、岩原、神樂「三俁口」），但時間配合接駁車，**最晚約 17:30 從雪場發車**；店裡 18:00 前還。

## 7. 網站結構（index.html）

分頁（`.nav-tab` → `showSection(id)`，支援 `#id` 網址）：
`itinerary`（每日行程，含桌機週曆 `.cal` 與手機版 `.mcal`）、`todo`、`restaurant`、`resorts`（雪場交通、雪票購買清單、決策表、接駁表）、`maps`（雪場地圖）、`gear`、`budget`、`daytrip`、`coach`。

重點元件：
- **週曆**：`.cal-b` 方塊用 `grid-row`，`row = 2 + round((時-7)*2)`（30 分一格），`grid-column` 2=12/30 … 8=1/5。手機版在 `.mcal-day#md0…md6`。改行程時桌機和手機版**都要改**。
- **預算**：`.bud-amt` input，`data-id="h0"…`、`data-st` = `ok`（已付/已訂）/`price`（定價還沒買）/`tbd`（待確認，空白）/`self`。空白不計入總額。localStorage key `budv3_`。目前每人已知總額 **NT$47,359**。
- **待辦**：`.td-item` checkbox，`data-id`，localStorage key `todo_`。已完成加 `td-done` 與 `checked`。
- **雪場地圖分頁 `#maps`**：
  - `#gps`：GPS 雪道定位（測試版）。Leaflet 1.9.4 動態載入（jsDelivr → unpkg 備援）、OSM 底圖、Overpass API 抓 `piste:type=downhill` 與 `aerialway`，存 localStorage `gps_v1_<key>`。函式：`gpsLoad('kagura'|'ishiuchi'|'kandatsu'|'here')`、`gpsToggle()`、`gpsRecenter()`。`GPS_AREAS` 的 bbox 是**估的座標**，沒實測；`GPS_ZH` 是日文雪道名→中文；`GPS_LIFT_TIME` 是神樂纜車末班。
  - `#g-kagura`、`#g-ishiuchi`、`#g-kandatsu`：雪場攻略卡（纜車時刻、雪道中日對照、新手路線、景點、餐廳、注意事項、票價），用 `<details class="gsec">` 收合。
  - 地圖圖片是**直接連官網圖片**（hotlink，`referrerpolicy="no-referrer"`），載不出來時 `mapFail()` 換成「開原圖」連結；點圖 `openMap()` 開全螢幕放大（`#mapbox`）。
- 雪票購買清單在 `resorts` 分頁「🎫 雪票購買清單」。

## 8. 開發方式與注意

- 編輯：用 Python 腳本做精確字串替換（先 `assert s.count(old)==1` 再 replace），比手動改安全。
- 驗證：用 Playwright（Chromium 已裝）開 `file:///…/index.html`，檢查每個分頁沒有 JS 錯誤、手機寬度 390px 沒有水平溢出，並截圖目視檢查。外部網站（官網圖片、Overpass、OSM 圖磚、CDN）在這個環境連不到，測試時用 `page.route` 回傳假資料。
- commit 訊息結尾加上工具要求的 Co-Authored-By／Session 行。
- 已確認的資料都要附來源；網站上的價格、時間要標明是 25/26 還是 26/27。

## 9. 待辦／下一步

**網站**
1. ✅ 神立攻略卡已完成（同格式）。如果 1/4 雪場決定了，照同樣格式補一張。
2. 請使用者在手機上確認：官網地圖圖片載得出來、GPS「載入神樂／石打丸山」有沒有抓到雪道（bbox 是估的，抓不到就改 `GPS_AREAS`）。
3. 26/27 官方地圖、石打各纜車末班、石打圓頂帳篷預約方式、神立 26/27 夜滑價格 → 開季前（11–12 月）更新。
4. 1/3 一日遊、1/4 雪場決定後更新行程與雪票。

**行程上還沒處理的（提醒使用者）**
- 12/30 新幹線：Jerry、Phoebe、文凱、Sandy、Vivi 還沒買（Klook 預售，11/30 確認；備案えきねっと 11/23 13:00 台灣時間事前受付）。曾討論 Jerry、Phoebe、文凱先搭較早班。
- 12/10 前買 WAmazing（3 人×2 張）；12/14 前買 Alpen 石打（6 人各自）。
- 問小 Su：1/1 能否 11:00–11:15 出發、神立夜滑要不要載。
- 文凱青達雪具預約；Jing 延長到 1/4。
- 12/31 跨年晚餐、1/2 全員聚餐訂位；Sandy・Vivi 東京住宿。
- BR195 回程機票金額（預算空白中）。

## 10. 主要資料來源

- 神樂官網：纜車 https://www.princehotels.co.jp/ski/kagura/winter/coursemap/?tab=lift ／ 票價 https://www.princehotels.co.jp/ski/kagura/winter/lift/ ／ 餐廳 https://www.princehotels.co.jp/ski/kagura/winter/store/
- 石打丸山官網：雪道 https://ishiuchi.or.jp/winter/ski/lift-course/ ／ THE VERANDA https://ishiuchi.or.jp/winter/facilities/snow-terrace/
- 神立官網：https://www.kandatsu.com/course-guide/
- WAmazing 共通券：https://tw.wamazing.com/snow/items/15083
- Alpen 石打電子票：https://alpen-group.stores.jp/items/6ab5d8f3015dd31dc879e36f
