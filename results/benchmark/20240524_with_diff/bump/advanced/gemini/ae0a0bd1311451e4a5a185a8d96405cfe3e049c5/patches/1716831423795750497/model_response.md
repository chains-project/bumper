```java
private org.hamcrest.Matcher<java.lang.String> layersPushed() {
    String imageLayer = this.image.layer();
    return new org.hamcrest.core.StringContains(false, String.format("%s: Pushed", imageLayer));
}
```