```java
private org.hamcrest.Matcher<java.lang.String> layersPushed() {
    boolean contains = this.image.layer().toString().contains("Pushed");
    return new org.hamcrest.core.StringContains(false, java.lang.String.format("%s: %s", this.image.layer(), contains));
}
```