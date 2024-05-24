```java
  private Matcher<String> layersPushed() {
        boolean isNegative = false;
        String layer = this.image.layer();
        String message = String.format("%s: Pushed", layer);
        return new StringContains(isNegative, message);
    }
```