```java
  private Matcher<String> layersAlreadyExist() {
        return new StringContains(
            false,
            String.format("%s: Layer already exists", this.image.layer()),
            new StringContains(
                false,
                String.format("%s: Layer already exists", this.image.layer())
            )
        );
    }
```