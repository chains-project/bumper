```java
  private Matcher<String> layersPushed() {
        final String layer = this.image.layer();
        return new StringContains(false, String.format("%s: Pushed", layer));
    }
```