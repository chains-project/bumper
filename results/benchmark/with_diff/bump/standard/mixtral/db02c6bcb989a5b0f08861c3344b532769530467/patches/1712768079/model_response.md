Here is the proposed patch for the failing method:

```java
private static org.hamcrest.Matcher<java.lang.String> imagePulled(final java.lang.String image) {
    return org.hamcrest.CoreMatchers.stringContains(String.format("Status: Downloaded newer image for %s", image));
}
```

In this patch, I replaced the usage of `org.hamcrest.core.StringContains` with `org.hamcrest.CoreMatchers.stringContains`. This is because the constructor for `StringContains` has changed in the new library version, and now only takes a single `String` argument instead of a `boolean` and a `String`. The `CoreMatchers` class provides a `stringContains` method that can be used with a single `String` argument.