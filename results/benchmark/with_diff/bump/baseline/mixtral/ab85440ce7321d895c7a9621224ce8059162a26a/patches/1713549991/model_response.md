Here's the proposed patch for the given code:

```java
private static Matcher<String> imagePulled(final String image) {
    String containsString = String.format("Downloaded newer image for %s", image);
    return new StringContains(containsString);
}
```

In this patch, I created a new variable `containsString` to store the substring to be checked. The `StringContains` constructor now only takes a single string argument, which is consistent with the updated library version.