```java
  private Matcher<String> layersAlreadyExist() {
        boolean layerExists = this.image.layer().exists();
        return new StringContains(
            false,
            String.format("%s: Layer already exists: %s", this.image.layer(), layerExists)
        );
    }
```