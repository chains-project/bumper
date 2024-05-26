```java
private org.hamcrest.Matcher<java.lang.String> layersPushed() {
    String expected = String.format("%s: Pushed", this.image.layer());
    if (expected.contains("sha256:")) {
      expected = expected.substring(0, expected.indexOf("sha256:"));
    }
    return new org.hamcrest.core.StringContains(false, expected);
}
```