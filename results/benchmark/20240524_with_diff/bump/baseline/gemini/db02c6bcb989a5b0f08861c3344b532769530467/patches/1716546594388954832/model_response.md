```java
  private Matcher<String> layersPushed() {
        boolean isLayerPushed = this.image.layer().contains("Pushed");
        return new StringContains(false, String.format("%s: %s", this.image.layer(), isLayerPushed ? "Pushed" : "Not Pushed"));
    }
```