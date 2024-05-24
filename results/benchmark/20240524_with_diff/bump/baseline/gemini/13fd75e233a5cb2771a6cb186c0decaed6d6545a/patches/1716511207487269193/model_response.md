```java
  private Matcher<String> layersPushed() {
        boolean contains = false;
        String layer = this.image.layer();
        String format = String.format("%s: Pushed", layer);
        return new StringContains(contains, format);
    }
```