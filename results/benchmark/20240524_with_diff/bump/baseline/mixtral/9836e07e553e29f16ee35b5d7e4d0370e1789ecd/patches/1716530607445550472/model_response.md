Here's the fixed version of the `layersAlreadyExist` method that should resolve the error:

```java
private Matcher<String> layersAlreadyExist() {
    String pattern = String.format("%%s: Layer already exists", this.image.layer());
    return new StringContains(pattern);
}
```

In the original code, the `StringContains` constructor was being called with two arguments, but the updated library version only accepts one argument. To fix the error, we need to pass a single `String` argument to the `StringContains` constructor. Therefore, we first format the pattern string using `String.format`, and then pass it as the argument to the `StringContains` constructor.