```java
private org.hamcrest.Matcher<java.lang.String> layersPushed() {
    return new org.hamcrest.core.StringContains(this.image.layer() + ": Pushed");
}
```