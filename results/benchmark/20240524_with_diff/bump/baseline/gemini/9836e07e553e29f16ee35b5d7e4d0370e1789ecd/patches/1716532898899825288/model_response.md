```java
  private Matcher<String> layersAlreadyExist() {
        boolean layerExists = false;
        String layer = this.image.layer();
        String message = String.format("%s: Layer already exists", layer);
        if (layerExists) {
            return new StringContains(message);
        } else {
            return new StringDoesNotContain(message);
        }
    }
```