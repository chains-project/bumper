```java
private Matcher<String> layersAlreadyExist() {
    String expectedString = String.format("%s: Layer already exists", this.image.layer());
    return new StringContains(expectedString);
}
```