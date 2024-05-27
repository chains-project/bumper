Here is the proposed patch for the failing client code:

```java
private static org.hamcrest.Matcher<java.lang.String> imagePulled(final java.lang.String image) {
    return org.hamcrest.Matchers.containsString(String.format("Status: Downloaded newer image for %s", image));
}
```

The patch replaces the use of `org.hamcrest.core.StringContains` constructor with `org.hamcrest.Matchers.containsString` method, which has a compatible signature.