```java
private Matcher<String> layersAlreadyExist() {
    String errorMessage = String.format("%s: Layer already exists", this.image.layer());
    return Matchers.containsString(errorMessage);
}
```