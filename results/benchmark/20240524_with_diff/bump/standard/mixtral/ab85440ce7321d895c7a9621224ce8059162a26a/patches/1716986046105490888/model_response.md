Here is the proposed patch for the failing client code:
```java
private org.hamcrest.Matcher<java.lang.String> layersAlreadyExist() {
    return org.hamcrest.CoreMatchers.containsString(java.lang.String.format("%s: Layer already exists", this.image.layer()));
}
```
Explanation:
The error message indicates that the constructor for `StringContains` now requires only one argument, instead of two. The new library version includes a method `containsString` in `CoreMatchers` that can be used as a replacement.