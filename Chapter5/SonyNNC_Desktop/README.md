Chapter5の演習モデル2種類をSonyのNeural Network Console Desktopに移植しました。<br>
※参照：<a href="https://techhub.developer.sony.com/ja/neural-network-console">Neural Network Console</a><br>
Neural Network Consoleでは、グラフィカルな環境で各レイヤーを接続することで簡単にモデル構築可能です。<br><br>
オリジナルのプロジェクトファイル（モデル定義ファイル）でドロップアウト前の版```AI-Yodosha.sdcproj```、ドロップアウトを組み入れた版を```AI-Yodosha_dropout.sdcproj```としてこちらにアップしてあります。<br>
また、ソースコードを　```NNabla```ライブラリ利用前提でのPythonコードとしてエクスポートし、こちらに置きました。<br>
ドロップアウト前の版を```AI-Yodosha.py```、ドロップアウトを組み入れた版を```AI-Yodosha_dropout.py```としています。<br>
なお、こちらの版では、入力画像（1024x1024）を「64x64」のサイズに変更する過程を```Interpolate```というレイヤー（関数）で処理しています。<br>
Sony Neural Network Libraryを使う前提でのソースコードですが、テキストのKerasのライブラリを使った版と比較すれば、内容的にほぼおなじであることが分かります。<br>
※参照：<a href="https://nnabla.org/ja/">Neural Network Libraries</a><br><br>
ドロップアウトレイヤーの挿入前後での構築後のモデル、学習曲線、および評価時のConfusion Matrix、さらにテスト画像の評価結果の図を置いておきます。<br>
<a href="https://github.com/aujinen/AI-yodosha/blob/main/Chapter5/SonyNNC_Desktop/Sony%20Neural%20Network%20Console%20Desktop%E7%A7%BB%E6%A4%8D.pdf">Sony Neural Network Console Desktop移植.pdf</a><br>
※SonyのNeural Network Console Desktopでのバグ<br>
※EvaluationタグではValidationを使い混同行列を取得し、InferenceではTestを使うのが良い<br>
https://groups.google.com/g/neural_network_console_users_jp/c/GNMgrjcrXAE/m/tPmhghQxCwAJ<br>
覚え書き<br>
1．NNC-Windows版では、「*.sdcproj」ファイルは既にファイルとして保存されているが、NNC-Desktop(Windows)版では、ダウンロードしないとローカルでのファイルとしては見えていない（編集もできない）。<br>
2．「*.sdcproj」ファイル内に「Varidation」という単語が多数あるが、今回の対象は下記であることをNNC-Windows版で確認して修正した。<br>
＝＝＝<br>
[Executor_0]<br>
Executor_Name=Executor<br>
Executor_NetworkName=MainRuntime<br>
Executor_DatasetName=Validation<br>
＝＝＝<br>
<br>
3．Projectの「import」で修正された「CONFIG」設定ごと取り込めるが、データセットそのもののリンク（割当）は解除されており、当然、学習データ（の結果）は空の状態になる。また同じファイル名であっても「*.sdcproj」拡張子が付いたプロジェクト名になるため、編集元のファイルへの上書きはされない（できない）。<br>


