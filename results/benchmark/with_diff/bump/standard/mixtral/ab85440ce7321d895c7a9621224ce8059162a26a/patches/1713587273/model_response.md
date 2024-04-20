Here's the fixed `imagePulled` method:

```java
private static org.hamcrest.Matcher<java.lang.String> imagePulled(final java.lang.String image) {
    return org.hamcrest.MatcherAssert.assertThat(image, new org.hamcrest.core.StringContains(org.hamcrest.core.StringContains.containsString(java.lang.String.format("Status: Downloaded newer image for %s", image))));
}
```

The error was caused by the missing method invocation of `MatcherAssert.assertThat()`. I added the missing invocation and passed the input string `image` and the `StringContains` matcher as arguments.