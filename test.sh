#!/bin/bash
# SPDX-FileCopyrightText: 2025 Yuto Shibusawa
# SPDX-License-Identifier: BSD-3-Clause
# test.sh: csvcountコマンドのテストスクリプト

# 期待される出力 (改行区切り)
EXPECTED_OUTPUT="value,count\nA,3\nB,1\nC,1"

# テストデータ（標準入力に渡すデータ）
INPUT_DATA="category,value\nA,10\nB,20\nA,30\nC,40\nA,50"

# csvcount.pyを引数 '1' (category列) で実行し、改行区切りで取得
ACTUAL_OUTPUT=$(echo -e "$INPUT_DATA" | python3 csvcount.py 1 | tr -d '\r') # CRLF対策として\rを削除

# 比較のために、行末の改行を削除
ACTUAL_OUTPUT=$(echo -e "$ACTUAL_OUTPUT" | tr '\n' ' ' | sed 's/ $//' | tr ' ' '\n')
EXPECTED_OUTPUT=$(echo -e "$EXPECTED_OUTPUT" | tr '\n' ' ' | sed 's/ $//' | tr ' ' '\n')

# 期待値と実際の結果を比較
if [ "$ACTUAL_OUTPUT" = "$EXPECTED_OUTPUT" ]; then
    echo "✅ Test Passed!"
    exit 0 # 成功
else
    echo "❌ Test Failed!"
    echo "--- Expected (Line by line) ---"
    echo -e "$EXPECTED_OUTPUT"
    echo "--- Actual (Line by line) ---"
    echo -e "$ACTUAL_OUTPUT"
    exit 1 # 失敗
fi
