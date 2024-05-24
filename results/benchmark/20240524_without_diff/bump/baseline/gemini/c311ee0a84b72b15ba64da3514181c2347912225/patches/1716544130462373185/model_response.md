```java
  private Matcher<String> layersPushed() {
        String expected = String.format("%s: Pushed", this.image.layer());
        return new StringContains(false, expected);
    }
```