Here is a fixed version of the method using a `contains` method from `StringUtils` class that was added in the latest version of the library:

```java
private static Matcher<String> imagePulled(final String image) {
    import org.apache.commons.lang3.StringUtils;
    return new StringContains(
        false,
        StringUtils.contains(String.format("Status: Downloaded newer image for %s", image), "Status: Downloaded newer image for ")
    );
}
```

This code checks if the string "Status: Downloaded newer image for " is a substring of the formatted string. If it is, then the test passes.