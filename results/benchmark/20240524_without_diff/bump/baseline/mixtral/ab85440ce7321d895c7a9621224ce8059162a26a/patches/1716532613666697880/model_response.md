Here's the fixed version of the `layersAlreadyExist` method that should resolve the error:

```java
private Matcher<String> layersAlreadyExist() {
    String pattern = String.format("%%s: Layer already exists", this.image.layer());
    return new StringContains(pattern);
}
```

The issue was that the `StringContains` constructor was being called with two arguments, while it only expects one argument in the updated library version. To fix this, I created a new variable `pattern` that stores the formatted string, and then passed it as the argument to the `StringContains` constructor.