Here's a possible patch for the failing method:

```java
private static Matcher<String> imagePulled(final String image) {
    return new CoreMatchers.stringContains(
        String.format("Status: Downloaded newer image for %s", image)
    );
}
```

This patch replaces the `StringContains` constructor with the equivalent constructor from the `CoreMatchers` class, which is part of the added `hamcrest-library` version 2.2.

Note that the `false` argument passed to the original constructor is not needed, as the `CoreMatchers.stringContains` constructor does not have this parameter.