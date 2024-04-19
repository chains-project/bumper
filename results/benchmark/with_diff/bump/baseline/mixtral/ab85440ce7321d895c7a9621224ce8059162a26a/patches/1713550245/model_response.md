Here's a fixed version of the `layersAlreadyExist` method that should work with the new version of the library:

```java
private Matcher<String> layersAlreadyExist() {
    return new StringContains(String.format("%s: Layer already exists", this.image.layer()));
}
```

In the original code, the `StringContains` constructor was being called with two arguments, but the updated constructor only accepts one argument. Therefore, we can remove the `false` argument to make the code compatible with the new library version.