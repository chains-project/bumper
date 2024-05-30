Here is the proposed patch for the failing client code:

```java
private static org.hamcrest.Matcher<java.lang.String> imagePulled(final java.lang.String image) {
    return org.hamcrest.Matchers.containsString(
        java.lang.String.format("Status: Downloaded newer image for %s", image)
    );
}
```

The failure is caused by the removal of the `StringContains` constructor that takes a boolean argument in the new version of the library. I replaced it with the `containsString` method from the `Matchers` class, which takes a single `String` argument and checks if it contains the specified substring.