```java
private org.hamcrest.Matcher<java.lang.String> layersPushed() {
    boolean pushed = this.image.layer();
    return new org.hamcrest.core.StringContains(false, java.lang.String.format("%s: Pushed", pushed ? "true" : "false"));
}
```