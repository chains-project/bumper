Here's a possible patch for the failing method:

```java
private static Matcher<String> imagePulled(final String image) {
    return new CoreMatchers.containsString(
        String.format("Status: Downloaded newer image for %s", image)
    );
}
```

In this patch, we replaced the `StringContains` constructor from the `org.hamcrest.core` package with the `containsString` method from the `org.hamcrest.CoreMatchers` package. It seems that the `StringContains` constructor has been removed in the new version of the library and replaced with a static method in the `CoreMatchers` class.