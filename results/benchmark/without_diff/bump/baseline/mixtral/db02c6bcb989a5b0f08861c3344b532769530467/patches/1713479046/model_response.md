Here is a possible patch for the code you provided:

```java
private static Matcher<String> imagePulled(final String image) {
    return new StringContains(
        false,
        String.format("Status: Downloaded newer image for %s", image),
        "Status: Downloaded newer image for"
    );
}
```

This patch adds a new argument to the `StringContains` constructor, which is a prefix that will be matched before the actual expected substring. This way, the `StringContains` matcher will still match the expected string, but it will also check that the prefix "Status: Downloaded newer image for" is present in the input string.

This patch should fix the error you are seeing, because it uses a constructor of `StringContains` that is compatible with the version of Hamcrest you are using.

Note that this patch assumes that the error you are seeing is caused by a change in the `StringContains` constructor. If the error is caused by a different issue, this patch may not be sufficient to fix the problem. In that case, you may need to investigate the issue further and try a different approach.