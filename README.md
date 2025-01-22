# mypkg

[![test](https://github.com/ookami-koki/mypkg/actions/workflows/test.yml/badge.svg)](https://github.com/ookami-koki/mypkg/actions/workflows/test.yml)

このリポジトリはROS2のパッケージである。
このパッケージでは、ipアドレスをパブリッシュする。
また、このブランチでは、ipアドレスとホストネームをパブリッシュする。

## 実行例

```
---
hostname: ubuntu-linux-22-04-desktop
address: 127.0.1.1
---
hostname: ubuntu-linux-22-04-desktop
address: 127.0.1.1
---

```

## ノード

### get_ipaddress_pub

ipaddress.pyに実装されている、ipアドレス(address)を取得しip_addressトピックに送信するノード。

## トピック

### ip_address

ipaddress.pyに実装されている、get_ipaddress_pubノードからaddressを受け取るトピック。

## 使用方法

### 型のインストール

ホストネーム(hostname)とアドレス(address)は、独自の型であるIpAddressを使用している。
以下のリンクのパッケージをインストールしてから、実行する。


- https://github.com/ookami-koki/ip_address_msgs.git

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
- Python

## テスト環境
- Ubuntu 22.04 LST
    - ROS2 Humblie (GitHub actions)

- Ubuntu 24.04 LST
    - ROS2 Jazzy (作成者のPC)

## 参考
- https://www.bioerrorlog.work/entry/actions-clone-another-repo
- https://stackoverflow.com/questions/56837562/colcon-build-failure-could-not-find-a-package-configuration-file-provided-by

## ライセンス
- このソフトウェアパッケージの一部は、3条項BSDライセンスの下、再頒布および使用が許可されます。
- このパッケージのコードは、下記のスライド(CC-BY-SA 4.0 by Ryuichi Ueda)のものを、本人の許可を得て自身の著作としたものです。
    - (https://ryuichiueda.github.io/slides_marp/robosys2024/lesson8.html)
    - (https://ryuichiueda.github.io/slides_marp/robosys2024/lesson9.html)
    - (https://ryuichiueda.github.io/slides_marp/robosys2024/lesson10.html)
    - (https://ryuichiueda.github.io/slides_marp/robosys2024/lesson11.html)

- © 2024-2025 Koki Iwai
