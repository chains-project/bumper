```java
private org.hamcrest.Matcher<java.lang.String> layersPushed() {
    boolean pushed = this.image.layer().contains("Pushed");
    String message = String.format("%s: Pushed", this.image.layer());
    return new org.hamcrest.core.StringContains(pushed, message);
}
```