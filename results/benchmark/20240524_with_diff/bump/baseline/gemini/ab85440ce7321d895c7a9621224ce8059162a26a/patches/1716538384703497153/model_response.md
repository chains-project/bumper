```java
  private Matcher<String> layersPushed() {
        String layer = this.image.layer();
        boolean contains = String.format("%s: Pushed", layer).contains(layer);
        return new StringContains(false, layer + ": Pushed");
    }
```