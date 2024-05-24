```java
private Matcher<String> layersAlreadyExist() {
    return CoreMatchers.containsString(
        String.format("%s: Layer already exists", this.image.layer())
    );
}
```