Here's the fixed version of the `imagePulled` method that should work with the new library version:

```java
private static Matcher<String> imagePulled(final String image) {
    return new StringContains(String.format("Downloaded newer image for %s", image));
}
```

In the new library version, the `StringContains` constructor no longer accepts a `boolean` parameter, so I have removed the `false` argument.