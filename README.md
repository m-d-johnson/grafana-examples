# Grafanalib Examples

I'm starting to compile a collection of [grafanalib](https://github.com/weaveworks/grafanalib) examples.  

Grafanalib does have some examples, they're listed in [this directory](https://github.com/weaveworks/grafanalib/tree/master/grafanalib/tests/examples)

In terms of compiling: Install grafanalib using 'pip3 install --user grafanalib'

Then, in the same directory as example.py:

```bash
generate-dashboard -o dash.json example.py && cat dash.json
```

This compiles the dashboard to JSON that Grafana understands. You can then Add a New Dashboard and import from JSON.

Tip: I use pbcopy to put the resulting JSON straight to my Mac's clipboard, ready to paste straight into the text field.

```bash
generate-dashboard -o dash.json example.py && cat dash.json | pbcopy
```

I have no connection with WeaveWorks. This is not an official grafanalib/weaveworks project.
