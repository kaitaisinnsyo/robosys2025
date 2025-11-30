#!/usr/bin/env python3
import sys
import csv
from collections import Counter

def main():
    # コマンドライン引数から集計対象の列番号を取得（1オリジン）
    if len(sys.argv) < 2 or not sys.argv[1].isdigit():
        # 標準エラー出力に出力
        sys.stderr.write("Usage: python csvcount.py <column_index (1-based)>\n")
        sys.exit(1)

    # Pythonは0オリジンなので、-1する
    try:
        col_index = int(sys.argv[1]) - 1
    except ValueError:
        sys.stderr.write("Error: Column index must be an integer.\n")
        sys.exit(1)

    # 標準入力から読み込み、csv.readerで処理
    reader = csv.reader(sys.stdin)

    # 標準出力に書き出すためのcsv.writer
    writer = csv.writer(sys.stdout)

    data_values = []

    # ヘッダー行をスキップ
    try:
        header = next(reader)
    except StopIteration:
        # 入力が空の場合
        return

    # データを読み込み、指定列の値をリストに格納
    for row in reader:
        try:
            data_values.append(row[col_index])
        except IndexError:
            # 行が短すぎる場合はスキップ (エラーは標準エラー出力に出すのが望ましい)
            pass

    # Counterで度数分布を計算
    counts = Counter(data_values)

    # 結果のヘッダーを出力
    writer.writerow(['value', 'count'])

    # 結果を出力 (value, count)
    for value, count in counts.items():
        writer.writerow([value, count])

if __name__ == "__main__":
    main()
