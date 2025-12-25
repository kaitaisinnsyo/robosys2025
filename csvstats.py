#!/usr/bin/env python3
# SPDX-FileCopyrightText: 2025 Yuto Shibusawa
# SPDX-License-Identifier: MIT

import sys
import csv

def main():
    if len(sys.argv) < 2 or not sys.argv[1].isdigit():
        sys.stderr.write("Usage: python3 csvstats.py <column_index(1-based)>\n")
        sys.exit(1)

    col_idx = int(sys.argv[1]) - 1
    data = []

    # 標準入力からCSVを読み込み
    reader = csv.reader(sys.stdin)
    try:
        header = next(reader) # ヘッダーを飛ばす
    except StopIteration:
        return

    for row in reader:
        try:
            if len(row) > col_idx:
                data.append(float(row[col_idx]))
        except ValueError:
            continue # 数値でない場合は飛ばす

    if not data:
        sys.stderr.write("Error: No valid numerical data found in column.\n")
        sys.exit(1)

    # 統計の計算
    res_sum = sum(data)
    res_avg = res_sum / len(data)
    res_max = max(data)
    res_min = min(data)

    # 標準出力へCSV形式で結果を出力
    writer = csv.writer(sys.stdout)
    writer.writerow(["metric", "value"])
    writer.writerow(["sum", res_sum])
    writer.writerow(["average", res_avg])
    writer.writerow(["max", res_max])
    writer.writerow(["min", res_min])

if __name__ == "__main__":
    main()
