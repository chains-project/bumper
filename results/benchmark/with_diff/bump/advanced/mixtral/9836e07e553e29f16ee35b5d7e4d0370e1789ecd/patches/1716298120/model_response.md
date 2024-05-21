Here is the proposed patch for the failing client code:
```java
private static org.hamcrest.Matcher<java.lang.String> imagePulled(final java.lang.String image) {
    return org.hamcrest.CoreMatchers.containsString(
        java.lang.String.format("Status: Downloaded newer image for %s", image)
    );
}
```
The failure is caused by the change in the constructor signature of the `StringContains` class in the new library version. Instead, we can use the `containsString` method from the `CoreMatchers` class to achieve the same functionality.