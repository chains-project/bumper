```java
private org.hamcrest.Matcher<java.lang.String> layersPushed() {
    String message = String.format("%s: Pushed", this.image.layer());
    return new org.hamcrest.core.StringContains(false, message);
}
```