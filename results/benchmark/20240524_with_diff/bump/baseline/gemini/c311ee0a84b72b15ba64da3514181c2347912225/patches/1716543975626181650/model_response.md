```java
  private Matcher<String> layersPushed() {
        return new StringContains(false, this.image.layer() + ": Pushed");
    }
```