```java
private Matcher<String> layersPushed() {
    boolean isPush = this.image.layer().contains(": Pushed");
    return new StringContains(false, String.valueOf(isPush));
}
```