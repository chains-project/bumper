```java
  private Matcher<String> layersPushed() {
        boolean isPushed = this.image.layer().contains("Pushed");
        return new StringContains(false, String.format("%s: %s", this.image.layer(), isPushed ? "Pushed" : "Not Pushed"));
    }
```