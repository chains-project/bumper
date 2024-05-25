```java
  private Matcher<String> layersPushed() {
        return new StringContains(false, String.format("%s: Push", this.image.layer()));
    }
```