# GithubReadmeTexView

## 使用用途

reportをgithubで管理するときにREADME.mdでreportを表示してわかりやすくするためのcli toolです。
vscodeのrecipeとして登録しておくといいと思います。

## Install

```shell
pip install git+https://github.com/SnowDango/GithubReadmeTexView
pip install Pillow
```
Pillowは依存Packageです。
詳しくは[こっち](https://pillow.readthedocs.io/en/stable/)を見てください。

また、内部で[Tex2img](https://tex2img.tech/)を使用しているので、こちらもInstallをしてCLIツールを使えるようにしてください。


## Use

```shell
tex2gitmd hoge.tex [options]
```
これでtexを1枚のgit_md_report.pngに変換します。

-p,--partのoptionを指定すると連結しないまま残すことができます。

README.md側でgit_md_report.pngを埋め込んでください。
