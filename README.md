# kindle-notion-integration

## 環境構築

VSCodeのDev Containersで開く

## 事前準備

1. API_KEY の発行

[公式](https://www.notion.com/ja/help/create-integrations-with-the-notion-api)
や
[Notion API に入門してみた](https://qiita.com/ulxsth/items/3434471ac91f8fa311cf)
などを参考に, Notion の API_KEY の発行を行う.

2. インテグレーションの追加

引き続き
[Notion API に入門してみた](https://qiita.com/ulxsth/items/3434471ac91f8fa311cf)
を参考に, Notion ページにインテグレーションの追加を行う.

3. `.env` の作成

次のコマンドを実行し, `.env`を作成する.

```
cp src/.env.sample src/.env
```

作成したファイルに, 手順 1 で作成した`API_KEY`を記載する.

## 実行

1. ハイライトデータの抽出

デモ動画を参考に, kindle のハイライトとメモデータをコピーする.

> [!WARNING]
> コピーの先頭行は`~色のハイライト`であること.

<img src="kindle-memo.gif" width="400">

コピーした内容は`src`ディレクトリにファイルを作成しペーストする.

2. ページ ID の取得

[Notion API に入門してみた](https://qiita.com/ulxsth/items/3434471ac91f8fa311cf)
などを参考にページ ID をコピーしておく.

> [!WARNING]
> ページはあらかじめ作成しておくこと.

3. 実行

```
cd src
uv run python main.py <file_name> <page_id>
```

## 参考

Notion API

- https://developers.notion.com/reference/patch-block-children
