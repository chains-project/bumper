```java
  private Matcher<String> layersAlreadyExist() {
        String expectedMessage = String.format("%s: Layer already exists", this.image.layer());
        return new StringContains(
            false,
            expectedMessage
        );
    }
```