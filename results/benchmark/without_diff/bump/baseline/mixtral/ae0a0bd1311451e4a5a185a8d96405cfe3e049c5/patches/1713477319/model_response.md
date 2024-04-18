Here's the proposed patch for the failing client code:

```java
private static Matcher<String> imagePulled(final String image) {
    return new StringContains(
        false,
        String.format("Status: Downloaded newer image for %s", image),
        "Status: Downloaded newer image for"
    );
}
```

The patch adds a new parameter to the `StringContains` constructor, which is the substring that should be contained in the examined string. In this case, it is the prefix "Status: Downloaded newer image for" of the expected log message. This way, the `StringContains` matcher will only check if the substring exists in the examined string, and not whether the examined string starts with the substring. This should fix the error caused by the updated version of the Hamcrest library.