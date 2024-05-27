Here's a fixed version of the code that should resolve the error:

```java
private static org.hamcrest.Matcher<java.lang.String> imagePulled(final java.lang.String image) {
    return org.hamcrest.Matchers.containsString(String.format("Status: Downloaded newer image for %s", image));
}
```

In this version, I replaced the `org.hamcrest.core.StringContains` constructor with the `org.hamcrest.Matchers.containsString` method, which only takes a single `String` argument. This should resolve the error message you were seeing.