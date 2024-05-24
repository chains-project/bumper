```java
  private Matcher<String> layersAlreadyExist() {
        String layer = this.image.layer();
        return new StringContains(
            false,
            String.format("%s: Layer already exists", layer)
        );
    }
```