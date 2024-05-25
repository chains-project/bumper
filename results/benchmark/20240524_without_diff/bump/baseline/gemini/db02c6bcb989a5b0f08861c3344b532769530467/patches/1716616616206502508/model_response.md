```java
  private Matcher<String> layersAlreadyExist() {
        String message = String.format("%s: Layer already exists", this.image.layer());
        return new StringContains(false, message);
    }
```