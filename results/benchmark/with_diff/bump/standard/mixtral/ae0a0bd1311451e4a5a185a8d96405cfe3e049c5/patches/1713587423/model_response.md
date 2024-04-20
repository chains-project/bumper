Here is the proposed patch for the client code:
```java
private static org.hamcrest.Matcher<java.lang.String> imagePulled(final java.lang.String image) {
    return new org.hamcrest.core.StringContains.StringContains(java.lang.String.format("Status: Downloaded newer image for %s", image));
}
```
Explanation:
The error message indicates that the constructor for `StringContains` now requires only one argument, while the original client code is passing two arguments. The new library version has removed the overloaded constructor that takes a boolean and a string, and added a new constructor that takes only a string. Therefore, the client code should be updated to match the new constructor signature.