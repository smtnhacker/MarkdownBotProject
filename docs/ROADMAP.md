# Road Map

Since the bot is still in its early developments, there are is still **lots** of things to implement.

## Formatting

Converting from one file format to another is quite complicated, especially since $\LaTeX$ is involved. Currently, the bot relies heavily on $\KaTeX$ and WebTex for rendering math equations, but each has their own limitations, especially when converting between file formats outside of HTML. There are things to consider so choosing between the proper command is important.

Things to look for:

- Cropped vs Full Page
- Single Image vs Muliple Image
- PNG vs SVG (for WebTex)
- Normal vs Large (for WebTex)

## Discord Interaction

- [ ] **Image Pagination**
    Sending multiple pictures might be seen as spamming sometimes. To account for this, there must be an option to only allow a single page to be viewed at a time using buttons and pagination.

- [ ] **Markdown Revision**
    Sometimes we might send messages that are incorrect and edit them, instead of sending a new message. It should be possible for the bot to detect changes (at least for within a specific time period) and update its images accordingly.

- [ ] **Original Message deletion**
    Like TeXit, there should be an option for deleting original messages to avoid redundancies.

- [ ] **Compilation Errors**
- [ ] **Draft Renders**
    Due to the nature of broadness of $\LaTeX$ and its successors, it is possible that the sent Markdown code might not render properly. Instead of merely saying that the file is invalid, showing the error log might be more helpful. Also, sending a draft render instead of nothing might also be a good idea.

## Quiz Feature

Might be useful since the bot renders markdown.