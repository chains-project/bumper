Here is a possible patch for the failing method:

```java
private static Matcher<String> imagePulled(final String image) {
    return new CoreMatchers.containsString(
            String.format("Status: Downloaded newer image for %s", image)
    );
}
```

This patch replaces the `StringContains` constructor with a call to `CoreMatchers.containsString`, which is an added library method that can be used in place of the removed `StringContains` constructor. This should allow the code to compile and run successfully.