```java
  private Matcher<String> layersPushed() {
        String layer = getImage().layer();
        return new StringContains(false, String.format("%s: Pushed", layer));
    }
```