```java
  // TODO: review this AI generated patch!
  private Matcher<String> layersPushed() {
        String layer = this.image.layer();
        return new StringContains(false, String.format("%s: Pushed", layer));
    }
```