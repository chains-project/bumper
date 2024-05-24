Here's the proposed patch for the given code:

```java
private static Matcher<String> imagePulled(final String image) {
    String contains = String.format("Downloaded newer image for %s", image);
    return new StringContains(contains);
}
```

In the updated library version, the constructor for `StringContains` no longer accepts a `boolean` argument. Therefore, the `false` argument has been removed. Also, the `String.format` call has been simplified and assigned to a separate variable `contains` for better readability.