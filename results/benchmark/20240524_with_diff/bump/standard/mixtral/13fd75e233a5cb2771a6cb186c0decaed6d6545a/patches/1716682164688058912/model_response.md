Here is the proposed patch for the given client code:

```java
private static org.hamcrest.Matcher<java.lang.String> imagePulled(final java.lang.String image) {
    return org.hamcrest.Matchers.containsString(String.format("Status: Downloaded newer image for %s", image));
}
```

In this patch, I replaced the `StringContains` constructor with the `containsString` method from the `org.hamcrest.Matchers` class, which is an added method in the new library version. This method takes a single argument of type `String`, which matches the argument required by the `org.hamcrend.Matcher` functional interface.