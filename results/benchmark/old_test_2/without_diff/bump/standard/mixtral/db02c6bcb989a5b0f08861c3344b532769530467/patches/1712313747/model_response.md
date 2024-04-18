Here is a possible patch for the failing method:

```java
private static org.hamcrest.Matcher<java.lang.String> imagePulled(final java.lang.String image) {
    return org.hamcrest.CoreMatchers.containsString(String.format("Status: Downloaded newer image for %s", image));
}
```

In this patch, I replaced the `org.hamcrest.core.StringContains` constructor with the `org.hamcrest.CoreMatchers.containsString` method, which has a simpler signature and should be compatible with the expected type of the `Matcher` return value.