Here is the proposed patch for the failing client code:

```java
private static org.hamcrest.Matcher<java.lang.String> imagePulled(final java.lang.String image) {
    return org.hamcrest.Matchers.containsString(String.format("Status: Downloaded newer image for %s", image));
}
```

In this patch, we have replaced the use of `org.hamcrest.core.StringContains` with `org.hamcrest.Matchers.containsString`. This is because the constructor for `StringContains` has been removed in the new library version, and replaced with the `containsString` method in the `Matchers` class. The new method takes only a single `String` argument, which matches the expected argument type for the `Matcher` constructor.