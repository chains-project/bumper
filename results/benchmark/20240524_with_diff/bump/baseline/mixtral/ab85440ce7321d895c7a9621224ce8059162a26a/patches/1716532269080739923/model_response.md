Here's a possible patch for the failing code:

```java
private static Matcher<String> imagePulled(final String image) {
    String contains = String.format("Downloaded newer image for %s", image);
    return new StringContains(contains);
}
```

I removed the `false` argument from the `StringContains` constructor since it's not needed anymore in the new library version. Also, I extracted the formatted string to a separate variable to make the code more readable.