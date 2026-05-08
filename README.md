# Delete Arc Note Accuracy

## English

Delete Arc Note Accuracy is a small Python utility for cleaning `.aff` files. It removes numeric accuracy suffixes from Arc note parameters while keeping the boolean value unchanged.

For example:

```text
false,3.00 -> false
true,6.00  -> true
false,-1.5 -> false
```

The script can process either one `.aff` file or every `.aff` file under a directory.

### Usage

Preview changes without writing files:

```bash
python deleteArcNoteAcc.py path/to/chart_or_folder --dry-run
```

Apply changes:

```bash
python deleteArcNoteAcc.py path/to/chart_or_folder
```

The program prints how many suffixes were removed from each file, plus a final summary.

## 中文

Delete Arc Note Accuracy 是一个用于清理 `.aff` 文件的小型 Python 工具。它会删除 Arc note 参数里附带的数字 accuracy 后缀，同时保留原本的布尔值。

例如：

```text
false,3.00 -> false
true,6.00  -> true
false,-1.5 -> false
```

这个脚本可以处理单个 `.aff` 文件，也可以递归处理某个文件夹下面的所有 `.aff` 文件。

### 使用方法

只预览修改，不写入文件：

```bash
python deleteArcNoteAcc.py path/to/chart_or_folder --dry-run
```

实际写入修改：

```bash
python deleteArcNoteAcc.py path/to/chart_or_folder
```

程序会输出每个文件删除了多少个 accuracy 后缀，并在最后给出总计。
