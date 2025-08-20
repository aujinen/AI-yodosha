# Chapter5内のimages_TMDU.zipデータの移植について
注意：２つ上のフォルダChapter5内の```images_TMDU.zip```データをダウンロードし解凍していることが前提条件となります。<br>
このフォルダ内の変換ソフトを使って、直下の３つのフォルダ(AI_Yodosha_train, AI_Yodosha_valid, AI_Yodosha_test)内のdataフォルダに、上記のデータへのハードリンクを埋め込みます。<br>
※コピーしても良いのですが、ハードリンクの方が媒体の容量を余計に利用しないので推奨します。<br>
index.csvは8:2の割合でtrainとvalidをランダムにデータ配分しています。<br>
※8:2の割合を保ったまま、割当を変更しても良いです。<br>
### windowsの場合
変換ソフトの```mk_hardLink_from_AI-yodosya-content_to_nncd_bucket-datasets.ipynb```にてdataフォルダ内に元画像へのハードリンクが作成されたことを確認後<br>
直下の３つのフォルダ(AI_Yodosha_train, AI_Yodosha_valid, AI_Yodosha_test)以下を```C:\Users\[ユーザ名]\nncd_bucket\datasets```直下にコピー（ないし移動）して下さい。<br>
### Linuxの場合
各フォルダ内の```index.csv```の改行コードを```nkf -d index.csv```にて変換する。<br>
さらに、下記のコマンドでパス区切りのバックスラッシュをスラッシュに変換する。<br>
```sed -i 's|\\|/|g' index.csv```<br>
```mk_hardLink_from_AI-yodosya-content_to_nncd_bucket-datasets.ipynb```はWindows用なので、パス区切りを修正すれば、Linuxでも使えます。<br>
上記にてdataフォルダ内に元画像へのハードリンクが作成されたことを確認後<br>
直下の３つのフォルダ(AI_Yodosha_train, AI_Yodosha_valid, AI_Yodosha_test)以下を```/home[ユーザ名]/nncd_bucket/datasets```直下にコピーする。<br>
