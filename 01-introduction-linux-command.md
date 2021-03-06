# OSにおけるユーザーについて
現在の一般的なOSでは一台のPCを複数名で共有できます。

あえて冗長に表現しておくと、AさんBさんという人がいたとします。AさんにはAさんの使いやすい設定
などがあるはずで、それはBさんも同様です。
Aさんが使っていない間、その同じ画面を文字通り『そのまま』Bさんが使い続けるのではなく、Bさん専用の設定などをAさんとは別に用意することができるという意味です

`
$ id
`

というコマンドで「現在ログインしている」ユーザーに関する情報を取得できます。

ユーザーIDは番号として管理されており、それだと流石にわかりにくいので、便宜上割り当てているのがユーザー名です。

上記のコマンドに、オプションを指定できます。オプションには様々なものがありますが、主なものをあげれば、-n や-u

`
$id -u
`

と実行すれば、(現在ログインしているユーザーの)番号が返されます。

またオプションを指定して

`$id -n -u`


と実行すれば、そのユーザーのユーザー名で返されます。


# OSにおけるグループについて
ある条件をみたすユーザーに対して、なにか処理をしたい(許可や禁止をしたい)ということが考えられます。
そのようなときに設定できるのが、グループです。

`$id -G`


と実行すれば、そのユーザーが属しているグループを番号として一覧で取得できます。

また

`$id -g`


と実行すれば、「現在はどのグループとして実行しているのか」、そのグループの番号を取得できます。

# ファイル・ディレクトリの権限について
ファイルの権限は次のコマンドで確認します。

`$ ls-l ファイル名`


10文字の内訳は以下のようになっています。
1. 一番左一桁:ファイル種別

   \- がファイル、dがディレクトリ、lがシンボリックリンク


2. 以下、9桁はユーザー自身、所属グループ、全くの他人についてそれぞれ、読み・書き・実行に対する許可や禁止を表しています。

「-rw-r--r--」の場合だと、種別はファイル、そのログインしているユーザーは、開くのと編集は可能、実行はできない、 グループのメンバーとその他の人は読み込みしかできないという意味です。

権限、パーミッションの変更方法は一般に

`$chmod [変更内容(形式はいくつかある)] ファイル名`



のコマンドで実行します。

変更内容の指定の仕方は大きく2つ方法があります。

1. 合計値で指定

読み取り、書き込み、実行にはそれぞれ数値が4、2、1と割り当てられているので、その合計値で指定する方法が一つ目の方法です。

例えば、

`$ chmod 444 ファイル名`



実行するのではあれば、すべてのユーザーに開くことのみしか許可しないような変更になります。

2. ユーザー種別ごとに指定する方法

ユーザー範囲の指定一文字、変更方法一文字、内容一文字の三要素で変更します。
ユーザー範囲については、ユーザーはu、グループはg、その他はo、全ユーザーはaと文字が割り当てられています。
変更方法は、+が指定した権限の付与、-が除去、=が指定した権限に変更。
変更内容はrが読み取り、wが書き込み、xが実行
となります。

例えば、

`$chmod u+x ファイル名`

であれば、ユーザーに実行権限を付与となります。

`$chmod a+rw ファイル名`

であれば、全ユーザーに読み込みと書き込み権限を付与となります。

user user の意味は、最初の方が所有ユーザー名で、後ろの方が所有グループ名を表しています。
