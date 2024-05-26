Here is the proposed patch for the failing client code:

```java
private static org.hamcrest.Matcher<java.lang.String> imagePulled(final java.lang.String image) {
    return org.hamcrest.Matchers.containsString(String.format("Status: Downloaded newer image for %s", image));
}
```

In the new library version, the `StringContains` constructor has been removed and replaced with the `containsString` method in the `Matchers` class. The `containsString` method takes a single `String` argument, which is the substring to search for in the target string. This method is a more appropriate fit for the intended use case in the client code.