Here is a possible patch for the failing code:

```java
private static Matcher<String> imagePulled(final String image) {
    return new CoreMatchers.containsString(
        String.format("Status: Downloaded newer image for %s", image)
    );
}
```

This patch uses the `containsString` method from the `CoreMatchers` class, which is an added library method in the Hamcrest library (indicated by `++`). The `StringContains` class is no longer available in the Hamcrest library, hence the need for this patch.