# Timberpile:wood:
Given three CSV files, [Author List](src/person.csv), [Paper List](src/paper.csv), and [Author Paper Relationship](src/paper_author.csv), this script generates paper lists in various styles.

## Usage
- Prepare python.
- Edit CSV files under [src](src).
- Run the following to generate `output.md`. In addition to `md`, there are options `html` and `bibtex`.
```console
git clone https://github.com/matsui528/timberpile.git
cd timberpile
python main.py --output_type md --output output.md
```
- To generate and delete all at once, do the following.
````console
make all # create all at once
make clean # delete all at once
````


## Example of output
See the followings.

### `output.md`
```md
- John Smith, Taro Tanaka, Hanako Yamada, "Building Rome in Five Years", CVPR, 2021.
- Taro Tanaka, John Smith, "Weighted Least Squares are All You Need", ICLR, 2022.
- John Smith, Lebron James, Cixin Liu, "Tha Case for non-Learned Index Structures", ICCV, 2023.
```

### `output.html`
```html
<ul>
	<li><a href="http://www.example.com">スミスジョン</a>, 田中太郎, <a href="http://www.google.com">山田花子</a>, "Building Rome in Five Years", CVPR, 2021.</li>
	<li>田中太郎, <a href="http://www.example.com">スミスジョン</a>, "Weighted Least Squares are All You Need", ICLR, 2022.</li>
	<li><a href="http://www.example.com">スミスジョン</a>, <a href="https://twitter.com/KingJames">ジェームズレブロン</a>, <a href="https://en.wikipedia.org/wiki/Liu_Cixin">劉慈欣</a>, "Tha Case for non-Learned Index Structures", ICCV, 2023.</li>
</ul>
```

### `output.bib`
```bibtex
@inproceedings{CVPR_2021_0,
	author={John Smith and Taro Tanaka and Hanako Yamada},
	title={Building Rome in Five Years},
	booktitle={Computer Vision and Pattern Recognition (CVPR)},
	year={2021}
}

@inproceedings{ICLR_2022_1,
	author={Taro Tanaka and John Smith},
	title={Weighted Least Squares are All You Need},
	booktitle={International Conference on Learning Representations (ICLR)},
	year={2022}
}

@inproceedings{ICCV_2023_2,
	author={John Smith and Lebron James and Cixin Liu},
	title={Tha Case for non-Learned Index Structures},
	booktitle={International Conference on Computer Vision (ICCV)},
	year={2023}
}
```

## Notes
- CSV+python imitates RDBMS.
- Using [paper_author.csv](src/paper_author.csv), we do something like a normalization in DB.
- Switching between Japanese and English can be freely programmed.
- Please edit files/sources according to your desired output format (applications, budget, etc).


---

# 木材の山:wood:

[著者一覧](src/person.csv)、[論文一覧](src/paper.csv)、[著者論文関係](src/paper_author.csv)、の３つのcsvファイルを準備し、そこから色々なスタイルで論文リストを生成するスクリプトです。

## 使い方
- pythonを準備します。
- [src](src)以下を編集します。
- 下記を実行すると`output.md`が生成されます。`md`の他にも`html`および`bibtex`のオプションがあります。
```console
git clone https://github.com/matsui528/timberpile.git
cd timberpile
python main.py --output_type md --output output.md
```
- 一括生成・削除するには以下のようにします。
```console
make all    # 一括生成
make clean  # 一括削除
```


## 生成物の例
以下のようなものが出来ます。

### `output.md`
```md
- John Smith, Taro Tanaka, Hanako Yamada, "Building Rome in Five Years", CVPR, 2021.
- Taro Tanaka, John Smith, "Weighted Least Squares are All You Need", ICLR, 2022.
- John Smith, Lebron James, Cixin Liu, "Tha Case for non-Learned Index Structures", ICCV, 2023.
```

### `output.html`
```html
<ul>
	<li><a href="http://www.example.com">スミスジョン</a>, 田中太郎, <a href="http://www.google.com">山田花子</a>, "Building Rome in Five Years", CVPR, 2021.</li>
	<li>田中太郎, <a href="http://www.example.com">スミスジョン</a>, "Weighted Least Squares are All You Need", ICLR, 2022.</li>
	<li><a href="http://www.example.com">スミスジョン</a>, <a href="https://twitter.com/KingJames">ジェームズレブロン</a>, <a href="https://en.wikipedia.org/wiki/Liu_Cixin">劉慈欣</a>, "Tha Case for non-Learned Index Structures", ICCV, 2023.</li>
</ul>
```

### `output.bib`
```bibtex
@inproceedings{CVPR_2021_0,
	author={John Smith and Taro Tanaka and Hanako Yamada},
	title={Building Rome in Five Years},
	booktitle={Computer Vision and Pattern Recognition (CVPR)},
	year={2021}
}

@inproceedings{ICLR_2022_1,
	author={Taro Tanaka and John Smith},
	title={Weighted Least Squares are All You Need},
	booktitle={International Conference on Learning Representations (ICLR)},
	year={2022}
}

@inproceedings{ICCV_2023_2,
	author={John Smith and Lebron James and Cixin Liu},
	title={Tha Case for non-Learned Index Structures},
	booktitle={International Conference on Computer Vision (ICCV)},
	year={2023}
}
```

## ポイント
- RDBMSをCSV+pythonで真似しています。
- [paper_author.csv](src/paper_author.csv)を用いて、データベースでいう正規化を行っています。
- 日本語・英語の切り替えは自由にプログラミングできます。
- 希望する出力形式（公募や予算のフォーマット）にあわせて、自由に改造して使ってください。






