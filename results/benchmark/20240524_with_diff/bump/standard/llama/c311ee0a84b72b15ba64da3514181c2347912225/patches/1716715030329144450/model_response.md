```java
private org.hamcrest.Matcher<java.lang.String> layersPushed() {
    return org.hamcrest.core.StringContains.containsString(java.lang.String.format("%s: Pushed", this.image.layer()));
}
```