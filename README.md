# mypkg

[![test](https://github.com/ookami-koki/mypkg/actions/workflows/test.yml/badge.svg)](https://github.com/ookami-koki/mypkg/actions/workflows/test.yml)

このリポジトリはROS2のパッケージである。
このパッケージでは、ipアドレスをパブリッシュする。
また、another-pkgブランチでは、ipアドレスとホストネームをパブリッシュする。

## 実行例

```
---
data: 127.0.1.1
---
data: 127.0.1.1
---

```

## ブランチ
このリポジトリには複数のブランチが作成されている。この内、ipアドレスを送信する機能を持つブランチは以下のブランチである。
### main
今いるこのブランチ。ipアドレスのみを送信するノードが実装されている。
### another-pkg
独自の型を使用し、ホストネームとipアドレスを送信するノードが実装されている。

## ノード
### get_ipaddress_pub

ipaddress.pyに実装されている、ipアドレスを取得しip_addressトピックに送信するノード。

## トピック
### ip_address

ipaddress.pyに実装されている、get_ipaddress_pubノードからaddressを受け取るトピック。


## 実行方法

以下のコマンドを入力し実行する。

```
$ ros2 run mypkg ipaddress
```

別の端末を立ち上げ、以下のコマンドを入力し実行する。

```
$ ros2 topic echo /ip_address
```

## 実行例

```
---
data: 127.0.1.1
---
data: 127.0.1.1
---

```

## テスト環境
- Ubuntu 22.04 LST
    - ROS2 Humble (GitHub actions)

- Ubuntu 24.04 LST
    - ROS2 Jazzy (作成者のPC)
## ライセンス
- このソフトウェアパッケージの一部は、3条項BSDライセンスの下、再頒布および使用が許可されます。
- このパッケージのコードは、下記のスライド(CC-BY-SA 4.0 by Ryuichi Ueda)のものを、本人の許可を得て自身の著作としたものです。
    - (https://ryuichiueda.github.io/slides_marp/robosys2024/lesson8.html)
    - (https://ryuichiueda.github.io/slides_marp/robosys2024/lesson9.html)
    - (https://ryuichiueda.github.io/slides_marp/robosys2024/lesson10.html)
    - (https://ryuichiueda.github.io/slides_marp/robosys2024/lesson11.html)

- © 2024-2025 Koki Iwai
