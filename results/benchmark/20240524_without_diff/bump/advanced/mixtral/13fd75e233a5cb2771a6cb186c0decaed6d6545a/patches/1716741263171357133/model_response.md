Here is the proposed patch:
```java
private org.hamcrest.Matcher<java.lang.String> manifestPushed() {
    return org.hamcrest.CoreMatchers.containsString(String.format("latest: digest: %s", this.image.digest()));
}
```
Explanation:
The error message indicates that the constructor `StringContains` requires a single argument of type `String`, but is being passed two arguments: a `boolean` and a `String`. The `StringContains` constructor that takes two arguments was added in a later version of Hamcrest.

To fix the error, we can use the `containsString` method from `CoreMatchers` instead, which takes a single `String` argument. This method is equivalent to the `StringContains` constructor that takes a single `String` argument.