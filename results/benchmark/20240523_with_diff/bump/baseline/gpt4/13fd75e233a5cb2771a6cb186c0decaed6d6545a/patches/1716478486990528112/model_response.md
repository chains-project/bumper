```java
private Matcher<String> layersPushed() {
        return CoreMatchers.containsString(String.format("%s: Pushed", this.image.layer()));
    }
```