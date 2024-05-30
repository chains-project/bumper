Here is the proposed patch for the failing client code:

```java
private static org.hamcrest.Matcher<java.lang.String> imagePulled(final java.lang.String image) {
    return org.hamcrest.Matchers.containsString(
        String.format("Status: Downloaded newer image for %s", image)
    );
}
```

The failure is caused by the change in the constructor signature of `StringContains` in the new version of the library. The new version only accepts a single argument, while the old version accepted two arguments. To fix this, we can use the `containsString` method from the `Matchers` class, which accepts a single argument and checks if the given string contains the specified substring.