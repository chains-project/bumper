```java
  private Matcher<String> layersPushed() {
        String layer = this.image.layer();
        boolean contains = false;
        return new StringContains(contains, String.format("%s: Pushed", layer));
    }
```