Here's the proposed patch to fix the error:

```java
private static org.hamcrest.Matcher<java.lang.String> imagePulled(final java.lang.String image) {
    return new org.hamcrest.core.StringContains(org.hamcrest.core.StringStartsWith.startsWith(image).describedAs(java.lang.String.format("Status: Downloaded newer image for %s", image)));
}
```

This patch replaces the `StringContains` constructor that takes a boolean and a string with the `StringStartsWith` matcher, which only takes a string. This is then passed to the `StringContains` constructor that takes a `Matcher` and a description. This should fix the error caused by the removal of the `StringContains` constructor that takes a boolean and a string.