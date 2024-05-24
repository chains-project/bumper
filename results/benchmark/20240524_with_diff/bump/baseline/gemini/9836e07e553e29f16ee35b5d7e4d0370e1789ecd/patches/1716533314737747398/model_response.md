```java
  private Matcher<String> layersPushed() {
        String layer = this.image.layer();
        return new StringContains(false, layer + ": Pushed");
    }
```