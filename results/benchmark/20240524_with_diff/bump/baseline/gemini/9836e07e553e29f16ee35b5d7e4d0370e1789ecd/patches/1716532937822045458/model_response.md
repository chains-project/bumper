```java
  private Matcher<String> layersAlreadyExist() {
    String layer = this.image.layer();
    String message = String.format("%s: Layer already exists", layer);
    return new StringContains(false, message);
  }
```