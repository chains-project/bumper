Here's a possible patch for the failing method:

```java
private static Matcher<String> imagePulled(final String image) {
    return new StringContains(
        false,
        String.format("Status: Downloaded newer image for %s", image),
        "Downloaded newer image for"
    );
}
```

In this patch, we added a third argument `"Downloaded newer image for"` to the `StringContains` constructor. This is because the `StringContains` constructor with two arguments is deprecated and has been removed in newer versions of Hamcrest. The third argument is used to specify the substring to search for in the target string. In this case, we are looking for the substring `"Downloaded newer image for"`, which is the prefix of the full message.

Note that the third argument was added in Hamcrest version 1.3, so if you are using an earlier version of Hamcrest, this patch may not work. In that case, you may need to upgrade to a newer version of Hamcrest or use a different approach to match the target string.