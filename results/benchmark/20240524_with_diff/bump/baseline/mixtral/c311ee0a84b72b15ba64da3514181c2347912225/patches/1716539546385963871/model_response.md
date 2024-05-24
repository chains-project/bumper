Here is a possible patch for the failing code:

```java
private Matcher<String> layersAlreadyExist() {
    String message = String.format("%s: Layer already exists", this.image.layer());
    return new StringContains(message);
}
```

In this patch, I created a new variable `message` to store the formatted string. Then, I passed this variable as an argument to the `StringContains` constructor. This way, the code is compatible with the new version of the library, which requires only one argument for the constructor.