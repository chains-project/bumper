Here's a proposed patch to fix the error:
```java
private static Matcher<String> imagePulled(final String image) {
    return new StringContains(
        false,
        "Downloaded newer image for " + image
    );
}
```
In this patch, I removed the `String.format` method call and directly concatenated the string instead. The `StringContains` constructor expects a `CharSequence` as its second argument, so there should be no issue with this change.