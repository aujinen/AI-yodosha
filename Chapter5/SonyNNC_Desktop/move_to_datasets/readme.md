### windowsの場合
直下の３つのフォルダ以下を```C:\Users\[ユーザ名]\nncd_bucket\datasets```直下にコピーする。<br>
各フォルダ内のindex.csvの内容に従って、dataフォルダ内にハードリンクを埋め込む。<br>
変換ソフトは mk_hardLink_from_AI-yodosya-content_to_nncd_bucket-datasets.ipynb<br>

### Linuxの場合
直下の３つのフォルダ以下を```/home[ユーザ名]/nncd_bucket/datasets```直下にコピーする。<br>
各フォルダ内の```index.csv```の改行コードを```nkf -d index.csv```にて変換する。<br>
さらに、下記のコマンドでパス区切りのバックスラッシュをスラッシュに変換する。<br>
```sed -i 's|\\|/|g' index.csv```<br>
各フォルダ内のindex.csvの内容に従って、dataフォルダ内にハードリンクを埋め込む。<br>
変換ソフトはwindows用のmk_hardLink_from_AI-yodosya-content_to_nncd_bucket-datasets.ipynbでのパス区切りを修正すれば、使える。<br>
