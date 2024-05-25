```java
  private Matcher<String> layersAlreadyExist() {
    final String layer = this.image.layer();
    return new StringContains(
        false,
        String.format("%s: Layer already exists", layer)
    );
  }
```