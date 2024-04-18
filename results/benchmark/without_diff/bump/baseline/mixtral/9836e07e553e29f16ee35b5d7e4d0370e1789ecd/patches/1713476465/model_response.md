Here's a possible patch for the failing code:
```java
private static Matcher<String> imagePulled(final String image) {
    return new CoreMatchers.stringContains(
            String.format("Status: Downloaded newer image for %s", image)
    );
}
```
In this patch, we're using the `stringContains` method from the `CoreMatchers` class instead of the `StringContains` constructor. This is because the `StringContains` constructor has been removed in the new version of the library, and the `stringContains` method has been added instead.

Note that this patch assumes that the new version of the library includes the `CoreMatchers` class with the `stringContains` method. If this is not the case, a different solution may be necessary.