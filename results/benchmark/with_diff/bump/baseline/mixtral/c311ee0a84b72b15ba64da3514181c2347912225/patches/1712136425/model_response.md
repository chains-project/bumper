Here's a possible patch for the given code:

```java
private static Matcher<String> imagePulled(final String image) {
    String containsString = String.format("Downloaded newer image for %s", image);
    return new StringContains(containsString);
}
```

In this patch, we create a new variable `containsString` that stores the substring we want to check for in the response. We then pass this variable to the `StringContains` constructor, which now only takes a single `String` argument. This should fix the error caused by the updated library version.