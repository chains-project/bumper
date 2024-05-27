Here is the proposed patch for the failing client code:
```java
private org.hamcrest.Matcher<java.lang.String> manifestPushed() {
    return org.hamcrest.Matchers.containsString(String.format("latest: digest: %s", this.image.digest()));
}
```
Explanation:
The error message indicates that the constructor for `StringContains` is expecting only one argument, but is receiving two. Looking at the library changes, we can see that the `StringContains` constructor has been removed and replaced with the `containsString` method in the `Matchers` class. We can use this method to replace the failing code and achieve the desired functionality.