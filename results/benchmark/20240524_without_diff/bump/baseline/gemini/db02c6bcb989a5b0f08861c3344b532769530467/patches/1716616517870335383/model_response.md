```java
  private Matcher<String> layersAlreadyExist() {
        return new StringContains(
            false,
            String.format(
                "%s: Layer already exists",
                this.image.getLayer().toString()
            )
        );
    }
```