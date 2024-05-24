```java
  private Matcher<String> layersPushed() {
    String message = String.format("%s: Pushed", this.image.layer());
    return new StringContains(false, message);
  }
```