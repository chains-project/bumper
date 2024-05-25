```java
  // TODO: review this AI generated patch!
  private Matcher<String> layersPushed() {
        String layerName = getImage().layer();
        return new StringContains(false, String.format("%s: Pushed", layerName));
    }
```