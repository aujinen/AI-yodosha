# Neural Network Console - Desktop への移植について
Chapter5の演習モデル2種類をSonyのNeural Network Console Desktopに移植しました。<br>
Neural Network Consoleでは、グラフィカルな環境で各レイヤーを接続することで簡単にモデル構築可能です。<br><br>
オリジナルのプロジェクトファイル（モデル定義ファイル）でドロップアウト前の版```AI-Yodosha.sdcproj```、ドロップアウトを組み入れた版を```AI-Yodosha_dropout.sdcproj```としてこちらにアップしてあります。<br>
### 2種類ある「Sony Neural Network Console」に注意
SonyのNeural Network Consoleは2種類あります。<br>
<a href="https://nnabla.org/ja/nnc/">Neural Network Console</a><br>
今回のものは2つめの「Neural Network Console - Desktop」への移植版となります。<br>
1. Neural Network Console - Windows（以下、NNC-Windows）<br>
   Windows環境専用で2017年8月にリリースされver 1.0からver 3.3.1(2025/5/27現在)まで複数回アップデートされています。書籍も比較的あり、ビデオ資料も豊富です。こちらはオープンソースソフトウェア（OSS）ではありません。<br>
   <a href="https://www.youtube.com/c/NeuralNetworkConsole">ビデオ資料</a><br>
   参考資料：足立悠. ソニー開発のNeural Network Console 入門──数式なし、コーディングなしのディープラーニング. リックテレコム; 2018. <br>
2. Neural Network Console - Desktop（以下、NNC-Desktop）<br>
   オンライン版が廃止になる少し前にOSSのソフトとして（オンライン版の移植版として）出てきました。<br>
   githubのサイトは下記になります。<br>
   <a href="https://github.com/sony/nnc-desktop">nnc-desktop</a><br>
### オリジナルの版と異なる点
1. 入力画像のサイズ変換について<br>
   こちらの版では、入力画像（1024x1024）を「64x64」のサイズに変更する過程を```Interpolate```というレイヤー（関数）で処理しています。<br>
2. コードの細かな違いについて<br>
   Sony Neural Network Libraryを使う前提でのソースコードですが、テキストのKerasのライブラリを使った版と比較すれば、内容的にほぼおなじであることが分かります。<br>
※参照：<a href="https://nnabla.org/ja/">Neural Network Libraries</a><br>
### 学習時の状態
ドロップアウトレイヤーの挿入前後での構築後のモデル、学習曲線、および評価時のConfusion Matrix、さらにテスト画像の評価結果の図を置いておきます。<br>
<a href="https://github.com/aujinen/AI-yodosha/blob/main/Chapter5/SonyNNC_Desktop/Sony%20Neural%20Network%20Console%20Desktop%E7%A7%BB%E6%A4%8D.pdf">Sony Neural Network Console Desktop移植.pdf</a><br>
### 学習後に各種画像をテストデータとして投入する方法について
NNC-Desktopでは、Windows専用のSNNC（NNC-Windows）とはデータの取り扱い関連が異なります。
NNC-Windowsでは、Training 後の ```Evaluation```タグ実行時の対象となるDatasetをconfigの設定画面から簡単に変更できます。デフォルトがValidationですが、新たに追加したデータセット名がTestであればTestに変更することで、比較的簡単に混同行列などの結果を取得できていました。しかしながらNNC-Desktopでは、別途```Inference```タグが備わっていて、Testデータはこちらを使うのが良い様です<br>
※具体的な使用法の例：```Inference```タグにて実行をクリックし、アップロードエリアに複数枚のテストデータ画像をドロップする
<br>
※NNC-Windowsのように```Evaluation```タグを使ってのTestデータ評価も可能ですが、複雑な手順を踏む必要があります。＝＝＞後述する「覚え書き」を参照願います。<br>
### 補遺・NNabla版のソースコード
ソースコードを　```NNabla```ライブラリ利用前提でのPythonコードとしてエクスポートし、こちらに置きました。<br>
ドロップアウト前の版を```AI-Yodosha.py```、ドロップアウトを組み入れた版を```AI-Yodosha_dropout.py```としています。<br>
### 覚え書き
※SonyのNeural Network Console Desktopでのバグ（ないし仕様）<br>
https://groups.google.com/g/neural_network_console_users_jp/c/GNMgrjcrXAE/m/tPmhghQxCwAJ<br>
CONFIG -> Datasetにて, Executeデータを「Validation」から変更できない。
https://groups.google.com/g/neural_network_console_users_jp/c/GNMgrjcrXAE/m/gvtOTyDjBQAJ<br>
NNC-Desktop版での
1．NNC-Windows版では、「*.sdcproj」ファイルは既にファイルとして保存されているが、NNC-Desktop(Windows)版では、ダウンロードしないとローカルでのファイルとしては見えていない（編集もできない）。<br>
2．「*.sdcproj」ファイル内に「Varidation」という単語が多数あるが、今回の対象は下記であることをNNC-Windows版で確認して修正した。<br>
＝＝＝<br>
[Executor_0]<br>
Executor_Name=Executor<br>
Executor_NetworkName=MainRuntime<br>
Executor_DatasetName=Validation<br>
＝＝＝<br>
3．Projectの「import」で修正された「CONFIG」設定ごと取り込めるが、データセットそのもののリンク（割当）は解除されており、当然、学習データ（の結果）は空の状態になる。また同じファイル名であっても「*.sdcproj」拡張子が付いたプロジェクト名になるため、編集元のファイルへの上書きはされない（できない）。<br>


