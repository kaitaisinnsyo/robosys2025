# robosys2025: CPU使用率監視パッケージ

[![test](https://github.com/kaitaisinnsyo/robosys2025/actions/workflows/test.yml/badge.svg)](https://github.com/kaitaisinnsyo/robosys2025/actions/workflows/test.yml)

本パッケージは、ROS 2を用いてPCのCPU使用率を定期的に取得し、トピックとして配信するものです。千葉工業大学 先進工学部 未来ロボティクス学科「ロボットシステム学」の第2回課題用として作成されました。

## 実行コマンド

環境をセットアップ（ビルドおよび `source`）した後、以下のコマンドでノードを起動します。

```bash
ros2 run robosys2025 cpu_publisher
動作確認環境
OS: Ubuntu 24.04 LTS (WSL2)

ROS 2 Version: Jazzy Jalisco

動作確認結果
実行時、以下の通りCPU使用率が1秒ごとに配信されます。

Plaintext

[INFO] [cpu_publisher]: Publishing: 1.9%
[INFO] [cpu_publisher]: Publishing: 0.2%
ライセンス
このソフトウェアは BSD 3-Clause License の下で公開されています。

© 2025 shibu0907
