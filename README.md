# Markdown to PDF Bot

A discord bot that accepts markdown files (or messages) and displays them as images.

## Prerequisite

To install, you must have have :

#### Pandoc

Mainly used in rendering file conversion. If you're using windows, you can go to [here](https://pandoc.org/installing.html)

#### PDFLaTeX

Engine used in rendering $\LaTeX$ (maybe). You can get it from distributions such as:

- [MiKTeX](http://miktex.org/)

- [TeX Live](http://www.tug.org/texlive/)

#### wkhtmltopdf

Converts HTML to PDF that is capable of running JS to render LaTeX

#### Poppler

Contains necessary packages for the dependency [pdf2image](https://github.com/Belval/pdf2image) (Instructions on how to install is also there).

#### Other Dependencies

Use the `requirements.txt` by running the following command in the terminal:

```bash
pip install -r requirements.txt
```

_Note: Some packages are currently unused. Sorry for that._

## Disclaimer

This project is still in its _very early_ stages so expect lots of bugs. Feel free to contact us for any issues.

## License

Distributed under MIT License.

## Acknowledgement

Still under construction, but you know who you are!