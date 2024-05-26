```java
private org.hamcrest.Matcher<java.lang.String> layersPushed() {
    boolean pushed = this.image.layer().isPresent();
    return new org.hamcrest.core.StringContains(false, java.lang.String.format("%s: Pushed", pushed ? this.image.layer().get() : "Unknown"));
}
```