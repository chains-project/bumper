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

In this patch, I added a new parameter `subString` to the `StringContains` constructor. This parameter is used to match the prefix of the expected string. This change is necessary because the `StringContains` constructor that takes only two arguments has been removed in a newer version of Hamcrest.

Note that the `subString` parameter is set to the prefix of the expected string, which is "Status: Downloaded newer image for". This ensures that the matcher still behaves the same way as before.

Also, note that the `StringContains` constructor that takes three arguments was added in a newer version of Hamcrest. Therefore, it is safe to use this constructor.