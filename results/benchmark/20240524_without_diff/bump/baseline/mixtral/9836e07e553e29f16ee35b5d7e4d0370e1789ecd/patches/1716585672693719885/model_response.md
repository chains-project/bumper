Here's the proposed patch for the given client code:

```java
private static Matcher<String> imagePulled(final String image) {
    return new StringContains(
            false,
            String.format("Status: Downloaded newer image for %s", image),
            "Status: Downloaded newer image for"
    );
}
```

This patch includes the new `StringContains` constructor that accepts a third argument, which is the substring to search for. This constructor is available in the latest version of the Hamcrest library (2.2), but it seems that the client code is using an older version that doesn't have this constructor.

By including the third argument, the code should work with both older and newer versions of the Hamcrest library.