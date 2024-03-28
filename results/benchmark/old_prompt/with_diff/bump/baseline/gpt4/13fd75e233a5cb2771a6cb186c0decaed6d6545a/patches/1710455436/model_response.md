```java
private Matcher<String> layersAlreadyExist() {
    String expectedSubstring = String.format("%s: Layer already exists", this.image.layer());
    return new StringContains(expectedSubstring);
}
```