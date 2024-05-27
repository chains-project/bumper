Here is the proposed patch for the failing client code:
```java
private org.hamcrest.Matcher<java.lang.String> manifestPushed() {
    return org.hamcrest.Matchers.containsString(String.format("latest: digest: %s", this.image.digest()));
}
```
Explanation:
The error message indicates that the constructor for `StringContains` now requires only one argument (a `String`), whereas previously it accepted two arguments (a `boolean` and a `String`).
Therefore, we should use the new `containsString` method from `Matchers` class instead, which accepts a `String` argument.
Additionally, we can remove the `false` argument from the `String.format` method call, since it is not being used.