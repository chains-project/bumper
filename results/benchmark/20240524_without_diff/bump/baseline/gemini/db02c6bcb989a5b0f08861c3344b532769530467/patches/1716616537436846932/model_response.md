```java
  private Matcher<String> layersAlreadyExist() {
        return new StringContains(
            false,
            String.format(Locale.ROOT, "%s: Layer already exists", this.image.layer())
        );
    }
```