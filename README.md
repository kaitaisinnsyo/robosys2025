# robosys2025- csvstats
muzukasi
- このソフトウェアパッケージは，3条項BSDライセンスの下，再頒布および使用が許可されます．
- このパッケージは，robosys2025由来のコード（© 2025 Ryuichi Ueda）を利用しています．
- このパッケージのコードは，下記のスライド（CC-BY-SA 4.0 by Ryuichi Ueda）のものを，本人の許可を得て自身の著作としたものです．
    - [ryuichiueda/my_slides robosys_2025](https://github.com/kaitaisinnsyo/robosys2025/actions/workflows/test.yml/badge.svg)
- © 2025 Yuto Shibusawa

このリポジトリは、千葉工業大学「ロボットシステム学」の第7回課題用です。CSVデータの特定の列から統計情報を算出するコマンドを提供します。

## 📊 csvstats コマンド
標準入力からCSVデータを受け取り、指定された列の「合計」「平均」「最大」「最小」を計算してCSV形式で出力します。

### 使い方
```bash
$ cat <ファイル名> | python3 csvstats.py <列番号>
必要なソフトウェア
Python

テスト済みバージョン: 3.10, 3.12

テスト環境
Ubuntu 24.04 LTS
