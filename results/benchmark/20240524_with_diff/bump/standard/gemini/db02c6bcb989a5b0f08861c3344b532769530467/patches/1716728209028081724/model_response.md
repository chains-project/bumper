```java
private org.hamcrest.Matcher<java.lang.String> layersPushed() {
    return new org.hamcrest.core.StringContains(false, "%s: Pushed", this.image.layer());
}
```