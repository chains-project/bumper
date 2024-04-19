Here is a fixed version of the method that should work with the new library version:

```java
private static Matcher<String> imagePulled(final String image) {
    return new StringContains(String.format("Status: Downloaded newer image for %s", image));
}
```

The issue was that the `StringContains` constructor was being called with an additional boolean argument, which was not present in the new library version. By removing this argument, the code should now compile and run correctly.