Here's a possible patch for the given code:

```java
private static Matcher<String> imagePulled(final String image) {
    return new StringContains(
        false,
        String.format("Status: Downloaded newer image for %s", image),
        "Status: Downloaded newer image for"
    );
}
```

In this patch, I added a new parameter `subString` in the `StringContains` constructor to specify the substring to be matched. This way, the `StringContains` constructor can be applied without causing any error.