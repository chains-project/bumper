```java
private org.hamcrest.Matcher<java.lang.String> layersPushed() {
    String expected = String.format("%s: Pushed", this.image.layer());
    return new org.hamcrest.core.StringContains(false, expected);
}
```