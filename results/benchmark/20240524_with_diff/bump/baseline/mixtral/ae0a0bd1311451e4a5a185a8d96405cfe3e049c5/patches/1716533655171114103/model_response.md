Here's the fixed version of the `imagePulled` method that should work with the new library version:

```java
private static Matcher<String> imagePulled(final String image) {
    return new StringContains(String.format("Downloaded newer image for %s", image));
}
```

In this version, I removed the `false` argument from the `StringContains` constructor, since it's not needed and is causing a compilation error with the new library version.