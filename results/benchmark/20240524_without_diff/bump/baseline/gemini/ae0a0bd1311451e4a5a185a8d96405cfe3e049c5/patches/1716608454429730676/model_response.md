```java
  private Matcher<String> layersPushed() {
        return new StringContains(false, String.format("%s: pushed", this.image.layer()));
    }
```