```java
  private Matcher<String> layersPushed() {
        return new StringContains(String.format("%s: Pushed", this.image.layer()));
    }
```