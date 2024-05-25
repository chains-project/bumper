```java
private Matcher<String> layersPushed() {
    return org.hamcrest.CoreMatchers.containsString(String.format("%s: Pushed", this.image.layer()));
}
```