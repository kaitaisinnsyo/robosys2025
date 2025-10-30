#!/bin/bash
# SPDX-FileCopyrightText: 2025 Yuto Shibusawa
# SPDX-License-Identifier: BSD-3-Clause

ng () {
        echo ${1}行目が違うよ
        res=1
}

res=0
a=澁澤
[ "$a" = 上田 ] || ng "$LINENO"
[ "$a" = 澁澤 ] || ng "$LINENO"

exit $res
