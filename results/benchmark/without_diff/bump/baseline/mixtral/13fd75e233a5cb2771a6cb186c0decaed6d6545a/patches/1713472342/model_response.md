Here's a possible patch for the failing client code:

```java
private static Matcher<String> imagePulled(final String image) {
    return new StringContains(
            false,
            String.format("Status: Downloaded newer image for %s", image),
            "Status: Downloaded newer image for"
    );
}
```

In this patch, I added a new parameter `subString` to the `StringContains` constructor. This parameter is used to match the beginning of the string. I set `subString` to `"Status: Downloaded newer image for"` so that it matches the beginning of the target string.

Note that the `StringContains` constructor with the `subString` parameter is an added library method identified with `++`, which means it's available in the new version of the library.