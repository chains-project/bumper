```java
private Matcher<String> layersAlreadyExist() {
    return new StringContains(
        false,
        this.image.layer() + ": Layer already exists"
    );
}
```