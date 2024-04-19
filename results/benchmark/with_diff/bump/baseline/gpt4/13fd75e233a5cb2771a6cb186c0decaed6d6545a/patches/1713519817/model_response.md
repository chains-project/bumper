```java
private Matcher<String> layersAlreadyExist() {
    return new StringContains(
        String.format("%s: Layer already exists", this.image.layer())
    );
}
```