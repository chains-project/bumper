```java
private org.hamcrest.Matcher<java.lang.String> layersPushed() {
    String format = "%s: Pushed";
    String message = String.format(format, this.image.layer());
    return new org.hamcrest.core.StringContains(false, message);
}
```