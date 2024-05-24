Here's the proposed patch to fix the error:

```java
private Matcher<String> layersPushed() {
    String layer = this.image.layer();
    return new StringContains(String.format("%s: Pushed", layer));
}
```

The change is to create a separate variable for the image layer and pass it directly to the `StringContains` constructor. This way, the boolean argument is not included in the constructor call, which is causing the error.