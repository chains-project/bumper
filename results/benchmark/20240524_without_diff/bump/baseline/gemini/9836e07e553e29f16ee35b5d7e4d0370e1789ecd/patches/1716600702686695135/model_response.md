```java
  private Matcher<String> layersAlreadyExist() {
        return new StringContains(
            false,
            String.format("%s and %s already exist", this.image.layer(), this.image.layer())
        );
    }
```