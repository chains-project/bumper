```java
  private Matcher<String> layersPushed() {
        String format = "%s: Pushed";
        Object[] args = new Object[]{this.image.layer()};
        return new StringContains(false, String.format(format, args));
    }
```