```java
  private Matcher<String> layersAlreadyExist() {
        return new StringContains(
            false,
            String.format("Layer already exists: %s", this.image.layer())
        );
    }
```