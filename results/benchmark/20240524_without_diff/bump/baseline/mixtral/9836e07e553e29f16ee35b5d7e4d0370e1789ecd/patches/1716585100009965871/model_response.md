Here is the proposed patch:

```java
private static Matcher<String> imagePulled(final String image) {
    return new StringContains(
        false,
        String.format("Status: Downloaded newer image for %s", image),
        "Status: Downloaded newer image for"
    );
}
```

In this patch, I added a new parameter to the `StringContains` constructor, which is the substring that should be present in the string being matched. In this case, I used the prefix "Status: Downloaded newer image for" to ensure that the matcher only matches the correct log message. This should fix the error you encountered.