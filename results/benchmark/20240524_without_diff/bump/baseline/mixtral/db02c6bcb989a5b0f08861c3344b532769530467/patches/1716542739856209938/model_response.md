Here's the fixed version of the `layersAlreadyExist` method:

```java
private Matcher<String> layersAlreadyExist() {
    StringContains stringContains = StringContains.containsString(
            String.format("%s: Layer already exists", this.image.layer())
    );
    return stringContains;
}
```

The original constructor `StringContains(boolean, String)` has been removed in the new library version. Instead, you can use the `StringContains.containsString(String)` method to create a `StringContains` matcher.