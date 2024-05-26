```java
private org.hamcrest.Matcher<java.lang.String> layersPushed() {
    org.hamcrest.core.StringContains contains = org.hamcrest.core.StringContains.containsString(java.lang.String.format("%s: Pushed", this.image.layer()));
    return contains;
}
```