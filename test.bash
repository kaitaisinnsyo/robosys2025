#!/bin/bash
# SPDX-FileCopyrightText: 2025 Yuto Shibusawa
# SPDX-License-Identifier: MIT

dir=~
[ "$1" != "" ] && dir="$1"

# テストデータ作成
echo -e "name,score\nAlice,80\nBob,90\nCharlie,70" > test_data.csv

# 正常系テスト: 2列目のスコアを集計
out=$(cat test_data.csv | python3 csvstats.py 2)
res=$?

# 期待される出力の確認（averageが80.0であるか等）
if [ $res -eq 0 ] && echo "$out" | grep -q "average,80.0"; then
    echo "✅ Test Passed!"
    rm test_data.csv
    exit 0
else
    echo "❌ Test Failed!"
    rm test_data.csv
    exit 1
fi
