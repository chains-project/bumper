```
private Matcher<String> layersPushed() {
    String layer = String.format("%s: Pushed", this.image.layer());
    return Matchers.containsString(layer);
}
```