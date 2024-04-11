Here is the proposed patch for the failing method:

```java
private static org.hamcrest.Matcher<java.lang.String> imagePulled(final java.lang.String image) {
    return new org.hamcrest.core.StringContains.StringContains(java.lang.String.format("Status: Downloaded newer image for %s", image));
}
```
In the new version of the library, the `StringContains` constructor no longer takes a `boolean` parameter. Instead, the constructor takes a single `String` argument. The patch reflects this change by removing the `false` argument from the constructor call.