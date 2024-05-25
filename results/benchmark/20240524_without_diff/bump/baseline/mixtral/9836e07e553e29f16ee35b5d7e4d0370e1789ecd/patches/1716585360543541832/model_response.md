Here is a potential fix for the issue:

```java
private static Matcher<String> imagePulled(final String image) {
    return new CoreMatchers.StringContains(
        String.format("Status: Downloaded newer image for %s", image)
    );
}
```

This fix involves changing the `StringContains` constructor call to use the fully-qualified name of the class, `CoreMatchers.StringContains`, instead of just `StringContains`. This is necessary because the `StringContains` class has been moved to a different package (`org.hamcrest.core` to `org.hamcrest.CoreMatchers`) in the newer version of the Hamcrest library. By using the fully-qualified name, we ensure that the correct version of the class is used.