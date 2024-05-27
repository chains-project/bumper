Here's a fixed version of the code that should resolve the error:

```java
private static org.hamcrest.Matcher<java.lang.String> imagePulled(final java.lang.String image) {
    return new org.hamcrest.core.StringContains(java.lang.String.format("Status: Downloaded newer image for %s", image));
}
```

The issue was caused by passing two arguments (boolean and String) to the `StringContains` constructor, while it only expects a single String argument. The boolean argument was removed.