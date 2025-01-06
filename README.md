# mypkg

[![test](https://github.com/ookami-koki/mypkg/actions/workflows/test.yml/badge.svg)](https://github.com/ookami-koki/mypkg/actions/workflows/test.yml)

授業用
授業内で作成したプログラムの保存や課題で作成したプログラムの保存を行う｡

このリポジトリはROS2のパッケージである。

## get_ipaddress_pub (ノード)

ipaddress.pyに実装されている、ホストネーム(hostname)とipアドレス(address)を取得しip_addressトピックに送信するノード。

## ip_address (トピック)

ipaddress.pyに実装されている、get_ipaddress_pubノードからhostnameとaddressを受け取るトピック。

## 使用方法

### 型の作成、またはインストール

ホストネーム(hostname)とアドレス(address)は、独自の型であるIpAddressを使用している。
そのため、自身でパッケージを作成するか、以下のリンクのパッケージをインストールしてから、実行する。

(https://github.com/ookami-koki/mypkg.git)


### 実行方法

以下のコマンドを入力し実行する。

```
$ ros2 run mypkg ipaddress
```

別の端末を立ち上げ、以下のコマンドを入力し実行する。

```
$ ros2 topic echo /ip_address
```

### 実行例

```
---
hostname: ubuntu-linux-22-04-desktop
address: 127.0.1.1
---
hostname: ubuntu-linux-22-04-desktop
address: 127.0.1.1
---

```

## 必要なソフトウェア
- python

## テスト環境
- Ubuntu 24.04LST

## ライセンス
- このソフトウェアパッケージの一部は、3条項BSDライセンスの下、再頒布および使用が許可されます。
- このパッケージのコードは、下記のスライド(CC-BY-SA 4.0 by Ryuichi Ueda)のものを、本人の許可を得て自身の著作としたものです。
    - (https://ryuichiueda.github.io/slides_marp/robosys2024/lesson8.html)
    - (https://ryuichiueda.github.io/slides_marp/robosys2024/lesson9.html)
    - (https://ryuichiueda.github.io/slides_marp/robosys2024/lesson10.html)
    - (https://ryuichiueda.github.io/slides_marp/robosys2024/lesson11.html)

- © 2024-2025 Koki Iwai
